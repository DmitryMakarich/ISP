import inspect
import re


class GeneralSerializer:
    def get_dict(self, obj):
        if type(obj) in (int, float, bool):
            return obj
        elif type(obj) is dict:
            for key in obj.keys():
                obj[key] = self.get_dict(obj[key])
            return obj
        elif type(obj) in (list, tuple):
            new_list = list()
            for elem in obj:
                new_list.append(self.get_dict(elem))
            if type(obj) is tuple:
                return str(tuple(new_list))
            return new_list
        elif type(obj) is str:
            return obj
        elif inspect.isfunction(obj):
            globs = {}
            name = obj.__name__
            func_code = inspect.getsource(obj)
            if func_code.__contains__('global'):
                subs = func_code.split('global')
                for i in range(1, len(subs)):
                    glob_key = subs[i].lstrip().split("\n")[0]
                    globs.update(dict([(glob_key, obj.__globals__[glob_key])]))
            elif func_code.__contains__('lambda'):
                func_code = re.findall(r'lambda[\s\w:+{}()\'""-\/*]+', func_code)[0]


                func_code = "f = " + func_code
                name = "f"
            return {'function': {
                'func_name': name,
                'globals': globs,
                'code': func_code}}
        elif inspect.isclass(obj):
            all_attributes = inspect.getmembers(obj, lambda a: not (inspect.isroutine(a)))
            fields = dict([a for a in all_attributes if not (a[0].startswith('__') and a[0].endswith('__'))])
            methods = dict(inspect.getmembers(obj, predicate=inspect.isfunction))

            for key in methods.keys():
                methods[key] = self.get_dict(methods[key])

            for key in fields.keys():
                fields[key] = self.get_dict(fields[key])

            str_class = {'class': {'class_name': obj.__name__,
                                   'fields': fields,
                                   'methods': methods
                                   }}
            return str_class

    def get_obj(self, s):
        if type(s) != dict:
            return s

        for value in s.keys():
            if value == "function":
                func = s[value]["globals"]
                s_func = s[value]["code"].split("\n")
                if s_func[0].count("    ") == 1:
                    s_func[0] = s_func[0].lstrip() + "\n"
                    for i in range(1, len(s_func) - 1):
                        tabs = int(s_func[i].count("    ") - 1)
                        s_func[i] = "    " * tabs + s_func[i].lstrip() + "\n"
                    exec("".join(s_func), func)
                else:
                    exec(s[value]["code"], func)

                return func[s[value]["func_name"]]
            elif value == "class":
                cls_name = ""
                attr = {}
                cls = s[value]
                for key in cls.keys():
                    if key == "class_name":
                        cls_name = cls[key]
                    elif key == "fields" and cls[key] is not {}:
                        for field in cls[key]:
                            cls[key][field] = self.get_obj(cls[key][field])
                        attr.update(cls[key])
                    elif key == "methods" and cls[key] is not {}:
                        for func in cls[key]:
                            cls[key][func] = self.get_obj(cls[key][func])
                        attr.update(cls[key])
                return type(cls_name, (), attr)
            elif type(s[value]) is str and s[value].startswith("("):
                s[value] = eval(s[value])
            else:
                s[value] = self.get_obj(s[value])

        return s

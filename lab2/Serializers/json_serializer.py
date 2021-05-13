import inspect
from general_serializer import GeneralSerializer


class Json(GeneralSerializer):
    def dumps(self, obj):
        return str(self.get_dict(obj))


    def dump(self, obj, fp):
        with open(fp, "w") as f:
            f.write(self.dumps(obj))


    def loads(self, s):
        return self.get_obj(eval(s))


    def load(self, fp):
        with open(fp, "r") as f:
            return self.loads(f.read())






























            # elif type(q) == dict:
            #     for value in q.keys():
            #         if type(q[value]) == dict:
            #             for key in q[value].keys():
            #                 q[value][key] = self.loads(str(q[value][key]))
            #             return q[value]
            #         elif type(q[value]) == str and q[value].startswith("(") and q[value].startswith(")"):  # кортеж
            #             eval(q[value])
            #             new_list = list()
            #             for elem in q[value]:
            #                 new_list.append(str(self.loads(elem)))
            #             return tuple(str(new_list))
            #         elif type(q[value]) == list:
            #             for i in range(0, len(q[value])):
            #                 q[value][i] = self.loads(str(q[value][i]))
            #             return q[value]








































# if type(obj) is int or type(obj) is float:
#    return str(obj)
# elif type(obj) is bool:
#    return str(obj).lower()
# elif type(obj) is dict:
#    for key in obj.keys():
#        obj[key] = Json.dumps(obj[key])
#    return str(obj)
# elif type(obj) is list or type(obj) is tuple:
#    new_list = list()
#    for elem in obj:
#        if type(elem) is int or type(elem) is float:
#            new_list.append(elem)
#        else:
#            new_list.append(Json.dumps(elem))
#    if type(obj) is tuple:
#        return str(tuple(new_list))
#    return str(new_list)
# elif type(obj) is str:
#    return obj.replace('\'', '\"')
# elif inspect.isfunction(obj):
#    return inspect.getsource(obj)
# elif inspect.isclass(obj):
#    all_attributes = inspect.getmembers(obj, lambda a: not (inspect.isroutine(a)))
#    fields = dict([a for a in all_attributes if not (a[0].startswith('__') and a[0].endswith('__'))])
#    methods = dict(inspect.getmembers(obj, predicate=inspect.isfunction))

#    for key in methods.keys():
#        methods[key] = Json.dumps(methods[key])

#    for key in fields.keys():
#        fields[key] = Json.dumps(fields[key])

#    str_class = {"class": {"class_name": obj.__name__,
#                           "fields": fields,
#                           "methods": methods
#                           }}
#    return str(str_class)


# -------------------------------------------------------------------------------


# if type(obj) is int:
#     return str({'int': obj})
# elif type(obj) is float:
#     return str({'float': obj})
# elif type(obj) is bool:
#     return str({'bool': obj})
# elif type(obj) is dict:
#     for key in obj.keys():
#         obj[key] = Json.dumps(obj[key])
#     return str({'dict': obj})
# elif type(obj) is list or type(obj) is tuple:
#     new_list = list()
#     for elem in obj:
#         new_list.append(Json.dumps(elem))
#     if type(obj) is tuple:
#         return str({'tuple': tuple(new_list)})
#     return str({'list': new_list})
# elif type(obj) is str:
#     return str({'str': obj})
# elif inspect.isfunction(obj):
#     globs = {}
#     func_code = inspect.getsource(obj)
#     if func_code.find('global') != -1:
#         subs = func_code.split('global')
#         for i in range(1, len(subs)):
#             glob_key = subs[i].lstrip().split("\n")[0]
#             globs.update(dict([(glob_key, obj.__globals__[glob_key])]))
#     return str({'function': {
#         'func_name': obj.__name__,
#         'globals': globs,
#         'code': func_code}})
# elif inspect.isclass(obj):  # доделать с наследованием
#     all_attributes = inspect.getmembers(obj, lambda a: not (inspect.isroutine(a)))
#     fields = dict([a for a in all_attributes if not (a[0].startswith('__') and a[0].endswith('__'))])
#     methods = dict(inspect.getmembers(obj, predicate=inspect.isfunction))
#
#     for key in methods.keys():
#         methods[key] = Json.dumps(methods[key])
#
#     for key in fields.keys():
#         fields[key] = Json.dumps(fields[key])
#
#     str_class = {'class': {'class_name': obj.__name__,
#                            'fields': fields,
#                            'methods': methods
#                            }}
#     return str(str_class)


# ---------------------------------------------------------------------------------------------------------
# @staticmethod
#     def get_dict(obj):
#         if type(obj) is int:
#             return {'int': obj}
#         elif type(obj) is float:
#             return {'float': obj}
#         elif type(obj) is bool:
#             return {'bool': obj}
#         elif type(obj) is dict:
#             for key in obj.keys():
#                 obj[key] = Json.get_dict(obj[key])
#             return {'dict': obj}
#         elif type(obj) is list or type(obj) is tuple:
#             new_list = list()
#             for elem in obj:
#                 new_list.append(Json.get_dict(elem))
#             if type(obj) is tuple:
#                 return {'tuple': tuple(new_list)}
#             return {'list': new_list}
#         elif type(obj) is str:
#             return {'str': obj}
#         elif inspect.isfunction(obj):
#             globs = {}
#             func_code = inspect.getsource(obj)
#             if func_code.find('global') != -1:
#                 subs = func_code.split('global')
#                 for i in range(1, len(subs)):
#                     glob_key = subs[i].lstrip().split("\n")[0]
#                     globs.update(dict([(glob_key, obj.__globals__[glob_key])]))
#             return {'function': {
#                 'func_name': obj.__name__,
#                 'globals': globs,
#                 'code': func_code}}
#         elif inspect.isclass(obj):  # доделать с наследованием
#             all_attributes = inspect.getmembers(obj, lambda a: not (inspect.isroutine(a)))
#             fields = dict([a for a in all_attributes if not (a[0].startswith('__') and a[0].endswith('__'))])
#             methods = dict(inspect.getmembers(obj, predicate=inspect.isfunction))
#
#             for key in methods.keys():
#                 methods[key] = Json.get_dict(methods[key])
#
#             for key in fields.keys():
#                 fields[key] = Json.get_dict(fields[key])
#
#             str_class = {'class': {'class_name': obj.__name__,
#                                    'fields': fields,
#                                    'methods': methods
#                                    }}
#             return str_class
# ------------------------------------------------------------------------------------------------
# q = eval(s)
#        for value in q.keys():
#            if type(q[value]) == dict:
#                for key in q[value].keys():
#                    q[value][key] = Json.loads(str(q[value][key]))
#                return q[value]
#            elif type(q[value]) == str and q[value].startswith("(") and q[value].startswith(")"):
#                eval(q[value])
#                new_list = list()
#                for elem in q[value]:
#                    new_list.append(str(Json.loads(elem)))
#                return tuple(str(new_list))
#            elif type(q[value]) == list:
#                for i in range(0, len(q[value])):
#                    q[value][i] = Json.loads(str(q[value][i]))
#                return q[value]
#            elif value == "function":
#                func = q[value]["globals"]
#                s_func = q[value]["code"].split("\n")
#                if s_func[0].count("    ") == 1:
#                    s_func[0] = s_func[0].lstrip() + "\n"
#                    for i in range(1, len(s_func) - 1):
#                        tabs = int(s_func[i].count("    ") - 1)
#                        s_func[i] = "    " * tabs + s_func[i].lstrip() + "\n"
#                    exec("".join(s_func), func)
#                else:
#                    exec(q[value]["code"], func)
#
#                return func[q[value]["func_name"]]
#            elif value == "class":  # class deserialization
#                cls_name = ""
#                attr = {}
#                cls = q[value]
#                for key in cls.keys():
#                    if key == "class_name":
#                        cls_name = cls[key]
#                    elif key == "fields" and cls[key] is not {}:
#                        for field in cls[key]:
#                            cls[key][field] = Json.loads(str(cls[key][field]))
#                        attr.update(cls[key])
#                    elif key == "methods" and cls[key] is not {}:
#                        for func in cls[key]:
#                            cls[key][func] = Json.loads(str(cls[key][func]))
#                        attr.update(cls[key])
#                return type(cls_name, (), attr)

import unittest

from Serializers.json_serializer import Json


class Person:
    test = "1"

    def __init__(self, name):
        self.name = name
        self.age = 1

    def display_info(self):
        print("Name", self.name, "Age", self.age)


class Prived:
    def __init__(self, c, m, pr):
        self.color = c
        self.mood = m
        self.rozrachnost = pr


    leng = 5


    def displ_i(self):
        print('Hi')
        print(self.mood, self.rozrachnost, self.color)


x = 1
y = 2
z = 3


def hello():
    return "hello"


def _sum(a, b):
    return a + b


def do_anything():
    print("do anything")


def func_1():
    global x
    return x + 1


def func_2():
    global y
    global x
    f = x + y
    return f


def func_3():
    global x
    global y
    global z

    return str(x + y + z + 1)


class SerializerTest(unittest.TestCase):
    def test_functions(self):
        js = Json()
        hello_str = js.dumps(hello)
        sum_str = js.dumps(_sum)
        do_str = js.dumps(do_anything)
        self.assertEqual(js.loads(hello_str)(), "hello")
        self.assertEqual(js.loads(sum_str)(1, 2), 3)
        self.assertEqual(js.loads(do_str)(), None)

    def test_functions_with_globals(self):
        js = Json()
        func1_str = js.dumps(func_1)
        func2_str = js.dumps(func_2)
        func3_str = js.dumps(func_3)
        self.assertEqual(js.loads(func1_str)(), 2)
        self.assertEqual(js.loads(func2_str)(), 3)
        self.assertEqual(js.loads(func3_str)(), "7")


    def test_with_lambda(self):
        js = Json()
        func1_str = js.dumps(lambda i: i + 1)
        func2_str = js.dumps({"a": lambda i: {"i": i}})
        print(func2_str)
        self.assertEqual(js.loads(func1_str)(1), 2)
        self.assertEqual(js.loads(func2_str)["a"](3), 27)


    def test_class(self):
        js = Json()
        class1_str = js.dumps(Person)
        class2_str = js.dumps(Prived)
        self.assertEqual(js.loads(class1_str)("tom").name, Person("tom").name)
        self.assertEqual(js.loads(class2_str)("1", "2", "3").color, Prived("1", "2", "3").color)


    def test_objects(self):
        js = Json()
        a = {"a": 5, "b": 3, "t": "12"}
        object1 = js.dumps(a)
        self.assertEqual(js.loads(object1), a)





if __name__ == '__main__':

    unittest.main()

    # a = Json().load("file.json")
    # print(a())

    # print(Json().dumps({"a": lambda name: f'Hello {name}'}))

    #o = {"a": lambda name: f'Hello {name}', "b": 2}
    #b = lambda i: i + 1
    #c = {"a": lambda i: {"i": i}}

    #i = inspect.getsource(b)
    #s = i[i.find("lambda"):]
    #left = 0
    #right = 0
    #for ind in range(len(s)):
    #    if s[ind] in ('{', '['):
    #        left += 1
    #    elif s[ind] in (')', '}', ','):
    #        right += 1
    #diff = right - left
    #for i in range(diff):
    #    if s.rfind(',') > s.rfind('}'):
    #        s = s[:s.rfind(',')]
    #    else:
    #        s = s[:s.rfind('}')]

    #print(s)
















    # a = {"a": Prived, "b": hello, "c": {"k": ("w", 5, "ghhjfjf", False, [1, 2, 5, "str"]), "t": "12"}}
    # object1 = Json().dumps(a)
    # print(object1)
    # print(Json().loads(object1))




























































    # func1_str = Json().dumps(lambda i: i + 1)
    # func2_str = Json().dumps({"a": lambda i: i ** i})
    # func3_str = Json().dumps(lambda first, last: f'Full name: {first.title()} {last.title()}')
    #
    #
    # print(Json().loads(func1_str)(1))
    # print(Json().loads(func2_str)(2))
    # print(Json().loads(func3_str)("2", "1"))





    # a = {"a": 1, "b": 'afaf', "f": 3}
    #
    #
    # b = Json().dumps(hello)
    # print(b)
    #
    # print(Json().loads(b)())

























    # a = Json().dumps(lambda e: e ** e)
    # print(a)
    # b = Json().loads(a)

    # for key in b.keys():
    #     for key1 in b[key]:
    #         print(b[key][key1])








    # str = 'asdsad.sad(stuff)'
    # pattern = r'\(\w+\)'
    # print(re.findall(pattern, str))



    # func = {}
    #
    # f = lambda e: e ** e
    # o = inspect.getsource(f)
    # print(o)
    # exec(o.lstrip(), func)
    # print(func["f"](3))
















    # o = inspect.getsource(hello)
    # print(o)
    # exec(o, func)
    #
    # print(func["hello"]())



    # a = Pickle().dumps(Person)
    # print(a)
    #
    # b = Pickle().loads(a)
    #
    # print(b)
    # print(b)

    # a = Person("Tom")
    # print(a)

    # a = {'a': Prived, 'b': Person, 'c': {'k': ('w', 5, 'ghhjfjf', False, [1, 2, 5, 'str']), 't': '12'}}
    # q = {"k": ("w", 5, "ghhjfjf", False, [1, 2, 5, "str"]), "t": "12"}
    # a1 = ("w", 5, "ghhjfjf", False, [1, 2, 5, "str"])

    # o = Json().dumps(d)
    # print(o)
    # print(type(o))
    # with open("file.json", "w") as f:
    #     Json().dump(a, f)
    #
    # p = Json().loads(o)
    # print(p)

    # print(str(i).__contains__("object"))
    # for arg in i.__dir__():
    # for a in i.__dir__():
    #     if not (a.startswith('__') and a.endswith('__')):
    #         print(a)
    # l_arg = [a for a in i.__dir__() if not (a.startswith('__') and a.endswith('__'))]
    # print(l_arg)
    # print(Person)

    # o = Json.dumps(i)
    # print(o)
    # print(type(o))
    # with open("file.json", "w") as f:
    #     Json().dump(a, f)
    #
    # p = Json.loads(o)
    # print(p())

# print(inspect.getmembers(Person, predicate=inspect.isfunction))
# print(inspect.getmembers(Person, lambda a: not (inspect.isroutine(a))))
# inspect.ismemberdescriptor(Person)
#
# def say_hello():
#     print("hello")
#
#
# k = inspect.getsource(say_hello)
# print(k)
# func = {}
# exec(k, {}, func)
# print(func)
# print(say_hello.__name__)
# func['say_hello']()
#
# for val in func.values():
#     val()
#
# a = (1, 2), (3, 4)
# b = list(range(10))
# c = {"a": say_hello, "b": {"c": 3}}
# d = "hello"
#
# print(say_hello)
# o = Json.dumps(c)
# print(o)
#
# with open("data_file".format(), "w") as write_file:
#     Json.dump(b, write_file)

# print("dict")
# for key in c.items():
#   print(key)

# print("list")
# for elem in b:
#    print(elem)

# r = str(b)
# k = str(a)
# print(r)
# print(k)

# print(type(a))


# x = 1
# y = 2
# z = 3
#
#
# def hello(a, b):
#     print("hi")
#     return a + b
#
#
# def g_func():
#     global x
#     global y
#     global z
#     return x + y + z


# i = Json.dumps(g_func)

# u = Json.loads(i)

# print(u())


# with open("file.json", "w") as f:
#    Json.dump(g_func.__globals__, f)


# func = {"x": 2}
# print(g_func.__globals__)
# i = inspect.getsource(g_func)
# exec(i, func)
# print(func[g_func.__name__]())


# print(i)


# def fooooh(n):
#     if n == 1:
#         return 1
#     return n * fooooh(n - 1)
#
#
#
# a = {"a": Prived, "b": True, "c": {"k": ("w", 5, "ghhjfjf", False, [1, 2, 5, "str"]), "t": "12"}}
#
# print(pickle.dumps(a))
#
# with open('data.pickle', 'wb') as f:
#     pickle.dump(a, f)
#
# with open('data.pickle', 'rb') as f:
#     data_new = pickle.load(f)
#
# print(data_new)


# func = {}
# exec(a, func)
# print(func["fooooh"])
# print(func["fooooh"](5))


# o = Json.dumps(fooooh)
# print(o)
#
# u = Json.loads(o)
# print(u)


# b = func["hi"]
# l = inspect.getsource(b)
# print(b)


# loc = {}
# glob = {}
# t = inspect.getsource(fooooh)
# exec(t, glob)
# print(glob["fooooh"](5))

# a = {"a": Prived, "b": hi, "c": {"k": ("w", 5, "ghhjfjf", False, [1, 2, 5, "str"]), "t": "12"}}
# b = Json.dumps(a).replace("\\","")
#
# with open("file.json", "w") as f:
#     Json.dump(a, f)

# print(fooooh.__code__)

# attr = {}
# s = inspect.getsource(fooooh)


# exec(s, {fooooh.__name__: fooooh}, attr)
# print(attr.popitem()[1](6))


# print(s.count("fooooh"))

# with open("file.json", "w") as f:
#    Json.dump(Prived, f)

# with open("file.json", "r") as f:
#    p = Json.load(f)

# print(p)


# print(loc)
# print(glob)

# for i in loc.keys():
# print(loc[i](5))


# c = Json.dumps(fooooh)
# print(c)
# d = Json.loads(c)

# print(d)


# with open("file.json", "w") as f:
#    Json.dump(a, f)


# e = Json.dumps(Prived)

# with open("file.json", "w") as f:
#    Json.dump(Prived, f)

# print(e)
# print(Prived.__name__)
# print(type(Prived))
# w = Json.loads(e)

# print(w.__name__)
# print(type(w))
# p = w("Tom", "zhopa", "ok")

# print(type(p.leng))

# p.displ_i()


# p = type("Person", (), q)

# print(q)
# for key in q.keys():
# print(q[key])


# with open("file.json", "w") as f:
#    f.write(Json.dumps(Person))


# def say_hello(a, b):
# print("hello")
# return a + b


# def add(c, t):
# print("hello")
# return c + t


# serialization
# k = inspect.getsource(say_hello)
# print(k)

# deserializition
# func = {}
# exec(k, {}, func)
# print(func)

# for val in func.values():
#    val()

# o = {"g": add, "l": say_hello, "p": True}

# with open("file.json", "w") as f:
#    f.write(serialize(o))


# a = [say_hello, add, 1, "hi",  {"g": add, "l": say_hello, "p": True}]
# print(a)

# with open("file.json", "w") as f:
#    f.write(str(a))

# with open("file.json", "r") as f:
# s = f.read()


# methods1 = inspect.getmembers(Person, predicate=inspect.isfunction)
# attributes = inspect.getmembers(Person, lambda a: not(inspect.isroutine(a)))
# var1 = [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]


# all_attributes = inspect.getmembers(Person, lambda a: not (inspect.isroutine(a)))
# fields = dict([a for a in all_attributes if not (a[0].startswith('__') and a[0].endswith('__'))])
# methods = dict(inspect.getmembers(Person, predicate=inspect.isfunction))

# fields.update(methods)
# print(fields)

# for func in q[key]:
#    meth = q[key][func].split("\n")
#    meth[0] = meth[0].lstrip() + "\n"
#    for i in range(1, len(meth) - 1):
#        meth[i] = "    " + meth[i].lstrip() + "\n"
# return "".join(meth)


# a = {"a": Prived, "b": True, "c": {"k": ("w", 5, "ghhjfjf", False, [1, 2, 5, "str"]), "t": "12"}}
# q = {"k": ("w", 5, "ghhjfjf", False, [1, 2, 5, "str"]), "t": "12"}
# a1 = ("w", 5, "ghhjfjf", False, [1, 2, 5, "str"])
# b = [1, 2, 3, 4, 5, 6]


# y = Json.dumps(a)
# print(y)
# i = Json.loads(y)

# print(i)
# print(type(i))

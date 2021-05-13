import toml
from general_serializer import GeneralSerializer


class Toml(GeneralSerializer):
    def dumps(self, obj):
        s = self.get_dict(obj)
        return toml.dumps(s)


    def dump(self, obj, fp):
        with open(fp, "w") as f:
            f.write(self.dumps(obj))


    def loads(self, s):
        return self.get_obj(toml.loads(s))


    def load(self, fp):
        with open(fp, "r") as f:
            info = f.read()

        return self.loads(info)

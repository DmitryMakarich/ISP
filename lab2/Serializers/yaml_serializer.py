import yaml
from general_serializer import GeneralSerializer


class Yaml(GeneralSerializer):
    def dumps(self, obj):
        s = self.get_dict(obj)
        return yaml.dump(s)


    def dump(self, obj, fp):
        with open(fp, "w") as f:
            yaml.dump(self.dumps(obj), f)


    def loads(self, s):
        return self.get_obj(yaml.load(s, Loader=yaml.FullLoader))


    def load(self, fp):
        with open(fp, "rb") as f:
            info = yaml.load(f, Loader=yaml.FullLoader)

        return self.loads(info)

import pickle
from general_serializer import GeneralSerializer


class Pickle(GeneralSerializer):
    def dumps(self, obj):
        s = self.get_dict(obj)
        return pickle.dumps(s)


    def dump(self, obj, fp):
        with open(fp, "wb") as f:
            pickle.dump(self.dumps(obj), f)


    def loads(self, s):
        return self.get_obj(pickle.loads(s))


    def load(self, fp):
        with open(fp, "rb") as f:
            byt = pickle.load(f)

        return self.loads(byt)


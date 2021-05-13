from os import path
from Serializers.json_serializer import Json
from Serializers.yaml_serializer import Yaml
from Serializers.pickle_serializer import Pickle
from Serializers.toml_serializer import Toml


class Serializer:
    @staticmethod
    def serialize(target_fp, obj):
        extension = path.splitext(target_fp)[1]

        if extension == ".json":
            Json().dump(obj, target_fp)
        elif extension == ".pickle":
            Pickle().dump(obj, target_fp)
        elif extension == ".yaml":
            Yaml().dump(obj, target_fp)
        elif extension == ".toml":
            Toml().dump(obj, target_fp)


    @staticmethod
    def deserialize(source_fp):
        extension = path.splitext(source_fp)[1]

        if extension == ".json":
            return Json().load(source_fp)
        elif extension == ".pickle":
            return Pickle().load(source_fp)
        elif extension == ".yaml":
            return Yaml().load(source_fp)
        elif extension == ".toml":
            return Toml().load(source_fp)
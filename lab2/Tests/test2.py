from Serializers.json_serializer import Json

x = 5




def _sum():
    global x

    return x + 5


if __name__ == '__main__':

    Json().dump(_sum, "file.json")


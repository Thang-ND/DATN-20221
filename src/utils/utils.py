import json

class Utils():
    def saveFileToLocal(self, filename, data):
        with open(filename, 'w') as f:
            f.write(json.dumps(data))
            f.close()

    @classmethod
    def json_serializer(cls, data):
        return json.dumps(data).encode('utf-8')
    
    @classmethod
    def json_deserializer(cls, data):
        return json.loads(data).decode('utf-8')
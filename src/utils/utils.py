import json

class Utils():
    def saveFileToLocal(self, filename, data):
        with open(filename, 'w') as f:
            f.write(json.dumps(data))
            f.close()
            
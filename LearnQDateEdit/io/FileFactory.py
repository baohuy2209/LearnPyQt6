import json
import os
class FileFactory:
    def writeData(self, path, arrData):
        jsonString = json.dumps([item.__dict__ for item in arrData], default=str)
        jsonFile = open(path, "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    def readData(self, path, ClassName):
        if os.path.isfile(path) == False:
            return []
        file = open(path, "r")
        self.arrData = json.loads(file.read(), object_hook=lambda d: ClassName(**d))
        file.close()
        return self.arrData
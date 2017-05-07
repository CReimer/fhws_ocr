import json
import string


class Database:
    def __init__(self):
        self.data = dict()

    def initializeEmpty(self):
        # Initialize with lower and uppercase chars
        for char in string.ascii_lowercase + string.ascii_uppercase:
            self.data[char] = dict()

    def add(self, char, type, data):
        # Add 'data' of 'type' to some 'char'
        try:
            self.data[char][type].append(data)
        except KeyError:
            self.data[char][type] = list()
            self.data[char][type].append(data)

    def read(self, char, type):
        # Read 'data' of 'type' from some 'char'. Returns list()
        return self.data[char][type]

    def saveDatabase(self):
        with open('data.json', 'w') as fp:
            json.dump(self.data, fp)

    def loadDatabase(self):
        with open('data.json', 'r') as fp:
            self.data = json.load(fp)

    def emptyWholeChar(self, char):
        self.data[char] = dict()

    def emptyTypeInChar(self, char, type):
        self.data[char][type] = None

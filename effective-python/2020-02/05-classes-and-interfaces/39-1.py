class InputData:
    def read(self):
        raise NotImplementedError

class PathInputData:
    def __init__(self, path):
        super().__init__():
        self.path = path

    def read(self):
        with open(self.path) as f:
            return f.read()

class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reducet(self, other):
        raise NotImplementedError
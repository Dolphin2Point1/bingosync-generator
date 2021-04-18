import json


class BingoEntry:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def __repr__(self):
        return json.dumps(self.__dict__)

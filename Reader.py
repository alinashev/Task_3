import json


class Reader:
    def __init__(self, path):
        self.path = path

    def open_json_file(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            self.text = json.load(f)
        return self.text

    def get_json(self):
        return Reader.open_json_file(self)

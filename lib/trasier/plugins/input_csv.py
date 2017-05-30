import csv

from .input_base import InputPlugin


class InputCsv(InputPlugin):
    def init_plugin(self, path: str, delimiter=",", encoding='utf-8', fieldnames=None):

        if path is None or type(path) != str:
            raise ValueError("url is required and must be string")

        self._path = path
        self._delimiter = delimiter
        self._encoding = encoding
        self._fieldnames = fieldnames

    def load(self):
        with open(self._path, newline='', encoding=self._encoding) as f:
            reader = csv.DictReader(f, fieldnames=self._fieldnames, delimiter=self._delimiter)
            ret = [row for row in reader]
        return ret


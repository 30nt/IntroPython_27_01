import json
import csv


class Reader:
    def __init__(self, filename):
        self._filename = filename

    def __repr__(self):
        return self._filename

    def read(self):
        ext = self._filename.rsplit(".", 1)[-1]
        if ext == "txt":
            return self._read_txt_file()
        elif ext == "json":
            return self._read_json_file()
        elif ext == "csv":
            return self.__read_csv_file()
        else:
            return []

    def _read_txt_file(self):
        with open(self._filename, "r") as file:
            data = []
            for line in file.readlines():  # предпочтительный способ
                data.append(line.strip())
        return data

    def _read_json_file(self):
        with open(self._filename, "r") as json_file:
            data = json.load(json_file)
        return data

    def __read_csv_file(self):
        data = []
        with open(self._filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                data.append(row)
        return data




reader = Reader("test.json")
print(dir(json))

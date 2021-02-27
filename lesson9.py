# Работа с файлами. Формат txt, json
import json


def read_txt_file(filename):
    with open(filename, "r") as file:
        # data = file.read()    # read, readlines  - одноразовое действие
        # data = data.split("\n")
        data = []
        for line in file.readlines():  # предпочтительный способ
            data.append(line.strip())
    return data

def read_json_file(filename):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
    return data


def write_txt_file(filename, data):
    with open(filename, "w") as file:
        data = "\n".join(data)
        file.write(data)
        # data = [f"{line}\n" for line in data]
        # file.writelines(data)

def write_json_file(filename, data):
    with open(filename, "w") as json_file:
        json.dump(data, json_file)

# data = read_txt_file("Homeworks/lesson7.txt")
# print(data)
# data.append("TEST TEXT")
# write_txt_file("Homeworks/lesson7_test.txt", data=data)

# person = read_json_file("test.json")
# person = person[0]
# person = json.loads(person)
# print(type(person), person)

write_json_file("test_2.json", {'name': ('John', True, None)})
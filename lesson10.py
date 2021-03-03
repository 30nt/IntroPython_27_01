# Работа с файлами csv. Импорт из файла, исключения (assert), практическая работа

import csv


def read_csv(filename):
    data = []
    with open(filename, 'r') as csv_file:
        # reader = csv.reader(csv_file, delimiter=";")
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)
    return data


def write_csv(filename, data):
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file)  # delimiter=";"
        writer.writerows(data)


print(__name__)

if __name__ == "__main__":
    filename = "test_csv.csv"
    data = read_csv(filename)
    print("...........", data)

    # header = data[0]
    # data = data[1:]
    #
    # header.insert(3, "total")
    #
    # for row in data:
    #     for index in range(3):
    #         row[index] = int(row[index])
    #     total = row[1] + row[2]
    #     # if len(row) == 3:
    #     #     row.append(total)
    #     # else:
    #     row.insert(3, total)
    #
    # # print(data)
    #
    # # data = [header] + data
    # data.insert(0, header)
    # print(data)
    # write_csv("write_csv.csv", data)
    #

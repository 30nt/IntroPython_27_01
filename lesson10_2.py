import csv


def read_csv_dict(filename):
    data = []
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(dict(row))
    return data


def write_csv_dict(filename, data):
    with open(filename, 'w') as csv_file:
        # fieldnames = ["month","sum","increase","total"]
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

print(__name__)

# filename = "test_csv.csv"
# data = read_csv_dict(filename)
# print(data)

# for row in data:
#     row["total"] = int(row["sum"]) + int(row["increase"])
#
# write_csv_dict("write_csv.csv", data)

import re


def key_sort_by_age(obj_dict):
    return obj_dict["age"]


def key_sort_by_name(obj_dict):
    return len(obj_dict["name"]), obj_dict["name"]


def key_sort_by_yers(obj_dict):
    years = obj_dict["years"]
    dates = re.findall("[0-9]+", years)  # list
    # date = years.split()[-1]
    return int(dates[-1])


my_list_int = [12, 3, -10, 2, 12]
my_list_str = ["John", "qwe", "aaaaa", "QWE", "2021", "..."]
my_list_mix = [1, 2, 3, "1", "11", "111"]  # плохой список
my_list_dict = [{"name": "John", "years": "1834 - 1846"},
                {"name": "Jack", "years": "1934 - 1953"},
                {"name": "Jacob", "years": "1854 - 1890"},
                {"name": "Max", "years": "1879 - 1946"},
                {"name": "Euclid", "years": "379 BC - 246"}, ]
# result = sorted(my_list_int)  # reverse=True, key=abs
# result = sorted(my_list_str)  # reverse=True, key=len
# result = sorted(my_list_mix, key=str)
result = sorted(my_list_dict, key=key_sort_by_yers)
print(result)

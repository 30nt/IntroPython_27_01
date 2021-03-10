my_list_1 = [1, 2, 3, 4]
my_list_2 = [10, 20, 30]
my_list_3 = [5, 6]
# test = list(zip(my_list_1, my_list_2, my_list_3))
test = list(zip(my_list_3, my_list_2, my_list_1))
print(test)

# import requests
#
# r = requests.get('http://api.forismatic.com/api/1.0/')
# print(r.status_code)
# print(r.json())


import requests

url = "http://api.forismatic.com/api/1.0/"



for number in range(1, 20):
    params = {"method": "getQuote",
              "format": "json",
              "key": number,
              "lang": "ru"}
    responce = requests.get(url, params=params)
    data = responce.json()
    print(data["quoteAuthor"], ">>>>>>>>", data["quoteText"])



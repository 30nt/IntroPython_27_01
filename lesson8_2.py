def stepen(osnova=2, pokazatel=2, stroka="text"):
    result = osnova ** pokazatel
    return f"{stroka}-{result}"


value = stepen(osnova=5, stroka="aaa")

print(value)

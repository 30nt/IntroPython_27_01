# 1. Написать функцию, которая генерирует и возвращает строку случайной длинны.
# Минимальную и максимальную длину строки ограничить с помощью параметров min_limit, max_limit, передаваемых в функцию.

# 2. Написать функцию (или последовательность нескольких функций), которые преобразуют случайную строку,
# полученную в п 1 по следующим правилам:
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы,
# знаки препинания, символ перехода на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Под словом будем понимать набор случайных букв от одной до 10.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять отдельно.
# Знаки препинания всегда идут в конце слова.
import random
import string


def create_random_string(min_limit, max_limit):
    rand_len = random.randint(min_limit, max_limit)
    return "".join([random.choice(string.ascii_lowercase) for _ in range(rand_len)])


def create_spaces(my_str):
    finish = False
    new_str = ""
    word_index = 0
    while not finish:
        r_step = random.randint(1, 10)
        word = my_str[word_index: word_index + r_step]
        new_str += f"{word} "
        word_index += r_step + 1
        if len(new_str) > len(my_str):
            finish = True
    return new_str


def modify_first_letter(word):
    return word.capitalize()


def modify_last_letter(word):
    word = word[:-1] + random.choice(',.!?')
    return word

def random_modificator(word):
    case = random.randint(1, 5)
    if case == 1:
        word = modify_last_letter(word)
    elif case == 2:
        word = modify_first_letter(word)
    return word

def modify_text(my_str):
    new_words = []
    for word in my_str.split():
        if len(word) > 1:
            new_words.append(random_modificator(word))
    return " ".join(new_words)


min_limit = 100
max_limit = 200
result = create_random_string(min_limit, max_limit)
result = create_spaces(result)
result = modify_text(result)
print(result)

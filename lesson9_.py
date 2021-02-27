################################################
# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.
import string
import os
import random

def create_dir(dir):
    try:
        os.mkdir(dir)
    except FileExistsError:
        pass


def create_file(dir, symbol, alphabet):
    # filename = f"{dir}/{symbol}.txt"
    filename = os.path.join(dir, f"{symbol}.txt")
    with open(filename, "w") as file:
        file.write(alphabet.replace(symbol, symbol.upper()))


def create_alphabet_files(dir):
    alphabet = string.ascii_lowercase
    for symbol in alphabet:
        create_file(dir, symbol, alphabet)


def do_tanos_click(dir):
    files = sorted(os.listdir(dir))
    # files = list(set(files))
    random.shuffle(files)
    files = files[: len(files) // 2]
    for file in files:
        os.remove(os.path.join(dir, file))


dir = "alphabet"
create_dir(dir)
create_alphabet_files(dir)
do_tanos_click(dir)

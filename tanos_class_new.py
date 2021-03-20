################################################
# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.
import string
import os
import random


class FileInteraction:
    def __init__(self, dir_name):
        self._dir_name = dir_name
        self._create_dir()

    @property
    def dir_name(self):
        return self._dir_name

    def _create_dir(self):
        try:
            os.mkdir(self._dir_name)
        except FileExistsError:
            pass

    def _create_file(self, symbol, alphabet):
        filename = os.path.join(self._dir_name, f"{symbol}.txt")
        with open(filename, "w") as file:
            file.write(alphabet.replace(symbol, symbol.upper()))

    def create_alphabet_files(self):
        alphabet = string.ascii_lowercase
        for symbol in alphabet:
            self._create_file(symbol, alphabet)

    def do_tanos_click(self):
        files = sorted(os.listdir(self._dir_name))
        random.shuffle(files)
        files = files[: len(files) // 2]
        for file in files:
            os.remove(os.path.join(self._dir_name, file))


test_interaction = FileInteraction("test")

# test_interaction.create_alphabet_files()
test_interaction.do_tanos_click()

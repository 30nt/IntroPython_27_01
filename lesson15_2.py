import random
import string
from utils import create_random_str


class EmailCreator:
    def __init__(self, ):
        self._email = self.create_email()

    @property  # защита от записи
    def email(self):
        return self._email

    # @staticmethod
    # def create_random_str(min_limit, max_limit):
    #     len_str = (random.randint(min_limit, max_limit))
    #     alpabet = string.ascii_lowercase
    #     rand_list = [random.choice(alpabet) for _ in range(len_str)]
    #     return "".join(rand_list)

    def create_email(self):
        number = random.randint(100, 999)

        names = ("arrow", "williams", "funny", "king")
        new_name = random.choice(names)

        domains = "com", "ua", "ru", "net"
        new_domain = random.choice(domains)

        rand_str = create_random_str(5, 7)
        create_email = f"{new_name}.{number}@{rand_str}.{new_domain}"
        return create_email

test_create = EmailCreator()
email = test_create.email
print(email)


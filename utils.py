import random
import string


def create_random_str(min_limit, max_limit):
    len_str = (random.randint(min_limit, max_limit))
    alpabet = string.ascii_lowercase
    rand_list = [random.choice(alpabet) for _ in range(len_str)]
    return "".join(rand_list)


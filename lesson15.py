import random
import time


def time_decorator(some_function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = some_function(*args, **kwargs)
        print(f"Time: {time.time() - start_time}")
        return result

    return wrapper


@time_decorator
def random_sum(number):
    int_list = [random.randint(1, 100) for _ in range(number)]
    return sum(int_list)

# start_time = time.time()
result = random_sum(1000000)
# print(f"Time: {time.time() - start_time}")

print(result)











# def decorator(some_function):
#     def wrapper():
#         print("Bla-bla-bla")
#         some_function()
#         print("...........")
#
#     return wrapper
#
# @time_decorator
# @decorator
# def my_func():
#     print("I'm a function")
#
# @decorator
# def new_f():
#     print("2+2")

# print("Bla-bla-bla")
# my_func()

# my_func = decorator(my_func)

# my_func()
# new_f()
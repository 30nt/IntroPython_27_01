import random
import string

PRINT_MODE = False


def create_point(min_limit, max_limit):
    point = (random.randint(min_limit, max_limit),
             random.randint(min_limit, max_limit))
    return point


def create_random_bbox(text, print_mode=PRINT_MODE):
    x0, y0 = create_point(0, 10)
    min_limit = max(x0, y0)
    x1, y1 = create_point(min_limit + 1, min_limit + 11)
    bbox = {"text": text,
            "x0": x0,
            "y0": y0,
            "x1": x1,
            "y1": y1}
    if print_mode:
        print(bbox)
    return bbox


def create_random_str(len_str=10):
    alpabet = string.ascii_lowercase
    rand_list = [random.choice(alpabet) for _ in range(len_str)]
    return "".join(rand_list)


def create_bboxs_list(number=10):
    bboxes = []
    for _ in range(number):
        text = create_random_str()
        bboxes.append(create_random_bbox(text))
    return bboxes


# text = "qwerty"
# text_2 = "asd"
# bbox = create_random_bbox(text=text)
# bbox_2 = create_random_bbox(text=text_2)
result = create_bboxs_list()
print(result)

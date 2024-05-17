import random


def random_id():
    return "".join([str(random.randint(0, 9)) for _ in range(7)])

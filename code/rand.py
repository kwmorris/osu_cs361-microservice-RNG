import random

def rand(count = 1):
    """
    Seeds the random number generator and generates a list of pseudo-random numbers in the range [0.0, 1.0).
    The list has a length of 'count' elements, and is returned to the calling function.
    """

    random.seed()
    return [random.random() for _x in range(count)]


if __name__ == '__main__':
    test_count = 10
    print(rand(test_count))
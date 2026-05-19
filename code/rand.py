import random, math

def rand(count = 1):
    """
    Seeds the random number generator and generates a list of pseudo-random numbers in the range [0.0, 1.0).
    The list has a length of 'count' elements, and is returned to the calling function.
    """

    random.seed()
    return [random.random() for _x in range(count)]

def convert_to_range(nums: list, min, max, bin = None):
    """
    Converts a list of randomly generated numbers between [0, 1) to lie within
    the range of [min, max) according to a range and bin size.
    """
    factor = max - min

    for i in range(len(nums)):
        num = nums[i]
        num *= factor
        if bin is not None and bin > 0:
            num = (num // bin) * bin
        num += min
        nums[i] = num


def generate_even(bin_count, range, count):
    """
    Generates a list of floats with an even bin distribution.
    """
    # determine bin size
    if bin_count != 0:
        bin = (range[1] - range[0]) / bin_count
    else:
        bin = None

    # generate random floats between (0, 1]
    nums = rand(count)

    # map floats to correct bins within the provided range
    convert_to_range(nums, range[0], range[1], bin)

    return nums


def generate_ints(range, count):
    """
    Generates a list of integers.
    """
    # generate random floats between (0, 1]
    nums = rand(count)

    # scale floats across range
    convert_to_range(nums, range[0], range[1])

    # Convert floats to lower int
    for i, num in enumerate(nums):
        nums[i] = math.floor(num)

    return nums


if __name__ == '__main__':
    test_count = 10
    print(rand(test_count))
    print(generate_even(20, [0, 10], test_count))
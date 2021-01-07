def basic_euclidean_algorithm(a, b):
    while a != b and a > 0 and b > 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def optimized_euclidean_algorithm(a, b):
    smallest = 0
    while b != 0:
        smallest = b
        b = a % b
        a = smallest
    return a


def recursive_euclidean_algorithm(a, b):
    if b != 0:
        return recursive_euclidean_algorithm(a, a % b)
    return a


if __name__ == "__main__":
    a = 12
    b = 24
    print(basic_euclidean_algorithm(a, b))
    print(optimized_euclidean_algorithm(a, b))
    print(recursive_euclidean_algorithm(a, b))

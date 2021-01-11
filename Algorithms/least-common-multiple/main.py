from math import gcd


def lcm(a, b):
    return a*b//gcd(a, b)


if __name__ == "__main__":
    print(lcm(54, 24))

# coding: utf-8

import numpy as np


def add(x, y):
    return x + y


def print_ten():
    for i in range(10):
        print(i)


def multi(x, y):
    return x * y


def main():
    data = np.array([1, 2, 3, 4])
    print(data)


if __name__ == '__main__':
    main()

# coding: utf-8

import numpy as np


def add(x, y):
    return x + y

class Test():
    def __init__(self, data):
        self.data = data

def print_ten():
    for i in range(10):
        print(i)


def multi(x, y):
    return x * y


def main():
    data = np.array([1, 2, 3, 4])
    print(data)
    # test
    print("take out")


if __name__ == '__main__':
    main()

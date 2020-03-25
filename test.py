# coding: utf-8

import numpy as np


class Test():
    def __init__(self, data):
        self.data = data

    def print_data(self):
        print(self.data)


def mult(a, b):
    return a * b


def main():
    print("ok")
    a = [np.sqrt(d) for d in range(10)]
    print(a)
    mult(3, 4)
    for i in range(10):
        print(i)


if __name__ == '__main__':
    main()

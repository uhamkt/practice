# coding: utf-8

import numpy as np


def add(x, y):
    return x + y


def print_ten():
    for i in range(10):
        print(i)


def main():
    print("ok")
    sum = add(4, 5)
    print(sum)
    print_ten()


if __name__ == '__main__':
    main()

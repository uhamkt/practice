# coding: utf-8

import numpy as np


def add(a, b):
    return a + b


def main():
    print("ok")
    a = [np.sqrt(d) for d in range(10)]
    print(a)
    print("data")
    add(1, 2)


if __name__ == '__main__':
    main()

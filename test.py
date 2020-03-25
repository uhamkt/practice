# coding: utf-8

import numpy as np


def mult(a, b):
    return a * b


def main():
    print("ok")
    a = [np.sqrt(d) for d in range(10)]
    print(a)
    mult(3, 4)


if __name__ == '__main__':
    main()

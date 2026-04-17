"""
this program performs matrix operations
it validates dimensions before operations
"""

import numpy as np

def input_matrix(rows, cols):
    return np.array([list(map(int, input().split())) for _ in range(rows)])


def matrix_operations(m1, m2, r1, c1, r2, c2):
    # addition and subtraction
    if m1.shape == m2.shape:
        print("\naddition:\n", m1 + m2)
        print("\nsubtraction:\n", m1 - m2)
    else:
        print("matrices not same size for addition or subtraction")

    # multiplication
    if c1 == r2:
        print("\nmultiplication:\n", np.dot(m1, m2))
    else:
        print("matrices not compatible for multiplication")


def main():
    try:
        r1 = int(input("enter rows of matrix 1: "))
        c1 = int(input("enter cols of matrix 1: "))
        print("enter elements:")
        m1 = input_matrix(r1, c1)

        r2 = int(input("enter rows of matrix 2: "))
        c2 = int(input("enter cols of matrix 2: "))
        print("enter elements:")
        m2 = input_matrix(r2, c2)

        matrix_operations(m1, m2, r1, c1, r2, c2)

    except Exception as e:
        print("error:", e)


if __name__ == "__main__":
    main()
"""
this program creates random numpy array
it sorts the array and reshapes it into matrix form
"""

import numpy as np

def create_and_reshape():
    arr = np.random.randint(1, 100, 12)
    arr.sort()
    matrix = arr.reshape(3, 4)

    print("original array:", arr)
    print("\nreshaped matrix:")
    print(matrix)


def main():
    create_and_reshape()


if __name__ == "__main__":
    main()
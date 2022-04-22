# Write a Python program that writes out a table of the function sin(x) vs. x, where x is tabulated between 0 and 2 with a thousand entries. Follow the basic Python program structure, including a main program function.
from tabulate import tabulate
import numpy as np


def main():
    x = np.linspace(0, 2 * np.pi, 1000)
    sinX = np.sin(x)

    result = {x[i]: sinX[i] for i in range(len(x))}

    print(tabulate(result.items(), headers=["x", "sin(x)"]))


if __name__ == '__main__':
    main()
    
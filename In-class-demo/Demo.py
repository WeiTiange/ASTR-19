# For the demonstration, you should write a python script that executes from the command line and does the following things:

# a) Import the sys and numpy modules.

#     b) Defines a main() function.

#     c) In the main() function:
#     i. Define variable x and initializes its value to 0.0.
#     ii. Use a for loop to iterate a variable i from 0 to 19 inclusive.
#     iii. For each value of i, set the value of x to be twice i plus 19 as a float.
#     iv. Use an f-string to print() out the value of x, including the text string ”The value of x is = “.

#     d) Use the if __name__ ==“__main__”: conditional to call main().

import sys
import numpy as np

def main():
    x = 0.0
    for i in range(20):
        x = float(2*i + 19)
        print(i)
    
    # print(f"The value of x is = {x}")

if __name__ == '__main__':
    main()
    
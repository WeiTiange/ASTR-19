import numpy as np

def main():
    i = 0
    n = 10
    x = 19.0

    # Use numpy to declare arrays 
    y = np.zeros(n, dtype=float) # Declares 10 0.0's

    # Use for loops to iterate with a variable
    for i in range(n): # loop from i = 0 to i = n-1
        y[i] = 2.0 * float(i) + 1 # Set y[i] = 2 * i + 1 as floats
    
    for y_ele in y:
        print(y_ele)

    print("y.shape ", y.shape)


if __name__ == '__main__':
    main()
    
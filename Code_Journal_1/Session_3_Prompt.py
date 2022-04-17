# Write a Python program that 
# defines a function f(x) 
def calculation(x) :
    # that returns x**3 + 8. 
    return x ** 3 + 8

# In the main function of the program, call f(x) with x = 9 and print the result.  
def main():
    result = calculation(9)
    print(f"The result of x**3 + 8 is: {result}")

# Use an if statement that executes if the result is larger than 27 and prints “YAY!”.
    if result > 27 :
        print("YAY!")


if __name__ == '__main__':
    main()
    
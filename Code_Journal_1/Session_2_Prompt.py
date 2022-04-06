# In each case, have the program print out the data type of the resulting answer.
# Write a Python that 

# prints the sum of two floating point numbers
from calendar import different_locale
from imaplib import Int2AP


def Sum(num1, num2):
    result = num1 + num2
    print("The sum of the two floating point numbers is:")
    print(result)
    print(type(result))
    print()

# the difference between two integers, 
def Difference(num1, num2):
    result = num1 - num2
    print("The difference between the two integers is:")
    print(result)
    print(type(result))  
    print()

# and the product of a floating point number and an integer. 
def Product(num1, num2):
    result = num1 * num2
    print("The product of the integer and the floating point number is:")
    print(result)
    print(type(result))
    print()

def main():
    floatNum1 = 114.514
    floatNum2 = 19.19
    intNum1 = 233   
    intNum2 = 666

    Sum(floatNum1, floatNum2)
    Difference(intNum1, intNum2)
    Product(floatNum1, intNum1)



if __name__ == '__main__':
    main()
    
# Write a Python program that declares a class describing your favorite animal. 

class Animal:
    #Write an initialization function that sets the values of the data members when an instance of the class is created. 
    def __init__(self, armLen, legLen, eyeNum, tail, furry):
        self.armLength = float(armLen) # length of the arms (float)
        self.legLength = float(legLen) # length of the legs (float)
        self.eyeNumber = int(eyeNum)   # number of eyes (int)
        self.haveTail = tail           # does it have a tail? (bool)
        self.isFurry = furry           # is it furry? (bool)
    
    # Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal.
    def DescribeAnimal(self):
        tail = "doesn't have"
        furry = "is not"

        if self.haveTail: 
            tail = "has"
        if self.isFurry:
            furry = "is"

        print(f"The length of the animal's arm is {self.armLength}m, the length of the animal's leg is {self.legLength}m. The animal has {self.eyeNumber} eyes. It {tail} a tail. It {furry} furry.")

def main():
    animal = Animal(1, 2, 6, True, False)
    animal.DescribeAnimal()

if __name__ == '__main__':
    main()
    
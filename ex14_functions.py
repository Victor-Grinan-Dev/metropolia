# samples
def print_price():
    print(price)
price = 100
print_price()

# GLOBALS

fancy_comp = {x:(lambda x:x**x)(x) for x in range(5)}

# ex 1
def subfuction():
    print("Hello there!")
    
def main1():
    print("Lets call the subfunction:")
    subfuction()
    print("Quitting.")
    

# ex 2
def poweroftwo(n):
    print("The result is", 2**n)

def main2():
    value = int(input("Give a number: "))
    poweroftwo(value)



# ex 3

def tester(givenstring="Too short"):
    print(givenstring)

def main3():
    while True:
        text = input("Write something (quit ends): ")
        if text == "quit":
            break
        if len(text) > 10:
            tester(text)
        else:
            tester()


#´ex 4
"""
Modify the function tester so that, besides testing if the length of the given string is more than ten characters, 
it also tests if there is the character "X" (capital X) in the given string. 
If the string is longer than 10 characters and it has X in it, 
the tester subfunction returns a value True to the main function, otherwise False.

If the subfunction returns True to the main function, 
the program prints "X spotted!". 
As earlier, if the user inputs "quit", 
the program terminates. When working correctly, the program prints something like this:
"""

# def tester(givenstring):
#     print(givenstring.find("X") != -1)
#     if len(givenstring) < 10:
#         return "Too short"
#     elif len(givenstring) > 9:
#         print(givenstring.find("X") != -1)
#         if givenstring.find("X") != -1:
           
#             return True
#         return False

def tester(givenstring):
    if len(givenstring) < 10:
        return "Too short"
    else: 
        if givenstring.find("X") != -1:
            return givenstring + "\nX spotted!"
        return givenstring

def main4():
    while True:
        text = input("Write something (quit ends): ")
        if text == "quit":
            break
            
        response = tester(text)
        print(response)


if __name__ == "__main__":
    givenstring = "Is Xavier here?"
    print(tester(givenstring))
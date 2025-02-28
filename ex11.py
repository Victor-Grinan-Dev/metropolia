"# -*- coding: cp1252 -*-" 

# 11.1
# Example output:
# Give a number: 2
# The given number was even.

def ex1():
    num = int(input("Give a number:"))
    if num % 2 == 0:
        print("The given number was even.")

# 11.2
"""
if [selection]:
	[code]
	
	if [selection]:
		[code]
	else:
		[code}
else:
	[code]

The idea is to create a program which asks for a user name and password. 
If the given name is wrong, the program prints "The given name is wrong". 
If the name is acceptable, the program asks for the password. 
If the password is correct, the system prints "Both inputs are correct!", 
otherwise "The password is incorrect.". The correct inputs should be "John" and the password "ABC123". Overall, 
the program should print the following:

Give name: Peter
The given name is wrong.

or alternatively
Give name: John
Give password: Monkeys?
The password is incorrect.

Give name: John
Give password: ABC123
Both inputs are correct!
"""

def  ex2():
    while True:
        name = input("Give name: ")
        if name == "John":
            passw = input("Give password: ")
            
            if passw == "ABC123":
                print("Both inputs are correct!")
                break
            else:
                print("The password is incorrect.")
                
        else:
            print("The given name is wrong.")

# 11.3
"""
The third exercise is to create a conditional structure which prints a line depending on the given selection. 
The program asks a number between 1 and 3, and based on the number prints the following: 1 prints "You selected one.", 
2 prints "You selected two." and 3 prints "You selected three.", like this:

Select a number (1-3): 1
You selected one.

Example output:
Select a number (1-3): 2
You selected two.
"""

"# -*- coding: cp1252 -*-"

def ex3():
    selection = input("Select a number (1-3): ")
    if selection == "1":
        selection = "one"
    if selection == "2":
        selection = "two"
    if selection == "3":
        selection = "three"
    print ("You selected", selection + ".")

# 11.4
"""
In the fourth exercise the idea is to define an if-structure which decides the action based on several inputs. 
The program asks for two numbers. If both of the numbers are even, the program prints "Both numbers are even." 
If only one of the numbers is even, the program prints "One of the numbers is even.".
Finally, if neither of the numbers is even, the program prints "Both numbers are odd".
"""
def ex4():
    num1 = int(input("Give a number: "))
    num2 = int(input("Give another number: "))

    if num1 % 2 == 0 and num2 % 2 == 0:
        print("Both numbers are even.")
    elif num1 % 2 != 0 and num2 % 2 != 0:
        print("Both numbers are odd.")
    elif num1 % 2 == 0 or num2 % 2 == 0:
        print("One of the numbers is even.")


# 11.5
""" 
In this exercise, expand the calculator so that the user can select what kind of calculation is done. 
If the user chooses 1, the calculator does addition as earlier. 
If 2, the calculator does substraction, if 3, it does multiplication, if 4, division.

Also add the instructions for the user to know what to do as shown in the example below. 
Also, if the user selects anything else besides 1-4, the program prints "Selection was not correct.".
"""
def ex5():
    print("Calculator")
    num1 = int(input("Give the first number: "))
    num2 = int(input("Give the second number: "))
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    operation = int(input("Please select something (1-4): "))
    if operation > 4 or operation < 1:
        print("Selection was not correct.")
    else:
        if operation == 1:
            print("The result is: ", num1 + num2)
        if operation == 2:
            print("The result is: ", num1 - num2)
        if operation == 3:
            print("The result is: ", num1 * num2)
        if operation == 4:
            print("The result is: ", num1 / num2)
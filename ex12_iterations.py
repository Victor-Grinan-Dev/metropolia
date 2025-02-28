

# ex1
"""
The first exercise in the fourth chapter is a basic while-iteration. 
The assignment is simple: create a program which on each turn prints the round number. 
Start by the round number 0 and make the iteration continue for four loops
"""

def ex1():
    counter = 0
    while counter < 5:
        print("This is lap", counter)
        counter += 1


#ex 2

"""
Create a program which, for every loop, prompts the user for input, and then prints it on the screen. 
If the user inputs the string "quit", the program prints "Bye bye!" and shuts down.
"""

def ex2():
    while True:
        phrase = input("Write something: ")
        if phrase == "quit":
            print("Bye bye!")
            break
        else:
            print(phrase)

# ex3
"""
The third progam tests a for-iteration. 
In this program, build a calculator, which asks the user for a number, 
and calculates the sum of all positive numbers from 0 to the usergiven input. 
If the user gives the number 4, the program calculates the sum 0+1+2+3, if 7, the calculation is 0+1+2+3+4+5+6. 
Finally, the program produces an answer with the printout "The sum was:" and an answer.
"""
def ex3():
    num = int(input("Give a number: "))
    res = 0
    for i in range(num):
        res += i
    print("The sum was:", res) 

# ex 4
""" 
In this exercise, expand the existing code by implementing the following new features: 
(A) Calculator does not automatically quit when the result is given, allowing user to do new calculations. 
The user has to select "6" in the menu to exit the program. 
(B) The calculator shows the selected numbers in the main menu by printing "Current numbers:" and the user-given input. 
By selecting "5" in the calculator menu, the user can change the given numbers.
"""
# def ex4():
def ex4():
    print("Calculator")
    num1 = "false"
    num2 = "false"
    while True:
        if num1 != "false" and num2 != "false":
            print("(1) +")
            print("(2) -")
            print("(3) *")
            print("(4) /")
            print("(5) Change numbers")
            print("(6) Quit")
            print("Current numbers: ", num1, num2)
            selection = input("Please select something (1-6): ")
            if selection == "1":
                print("The result is:", num1 + num2 )
            if selection == "2":
                print("The result is:", num1 - num2)
            if selection == "3":
                print("The result is:", num1 * num2)
            if selection == "4":
                print("The result is:", num1 / num2)
            if selection == "5":
                num1 = "false"
                num2 = "false"
            if selection == "6":
                print("Thank you!")
                break
        else:
            num1 = int(input("Give the first number: "))
            num2 = int(input("Give the second number: "))






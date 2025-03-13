from random import randint, choice
import math
import time
import ownmodule
 
# ex 1
def flip_a_coin():
    print("5 coin flips:")
    coin_sides = ["Tails!", "Heads!"]
    for _ in range(5):
        print(coin_sides[randint(0,2)])

# ex 2
def Foot_Nuke_Cockroach():
    choices = [ "Nuke", "Foot", "Cockroach"]
    wins = 0
    tie = 0
    rounds = 0  

    while True:
        player_choice = input("Foot, Nuke or Cockroach? (Quit ends): ")
        if player_choice == "Quit":
            print("You played", rounds ,"rounds, and won", wins ,"rounds, playing tie in", tie ,"rounds.")
            break
        elif player_choice not in choices:
            print("Incorrect selection.")
            continue
        else:
            print("You chose:", player_choice)
            pc_choice = choices[randint(1, 3)]
            print("Computer chose:", pc_choice)
            if pc_choice == player_choice:
                if pc_choice == "nuke":
                    print("Both LOSE!")
                else:
                    print("It is a tie!")
                tie += 1
            elif pc_choice == "Foot" and  player_choice == "Nuke":
                print("You WIN!")
                wins += 1
            elif pc_choice == "Nuke" and  player_choice == "Foot":
                print("You LOSE!")
            elif pc_choice == "Cockroach" and  player_choice == "Nuke":
                print("You LOSE!")
            elif pc_choice == "Nuke" and  player_choice == "Cockroach":
                print("You WIN!")
                wins += 1
            elif pc_choice == "Foot" and  player_choice == "Cockroach":
                print("You LOSE!")
            elif pc_choice == "Cockroach" and  player_choice == "Foot":
                print("You WIN!")
                wins += 1
        rounds += 1

# ex 3
def tryme(text):
    if len(text) >= 6 and not (text.isalpha() or text.isnumeric()):
        return True
    return False

# ex 5 Calculator:
def calculator():
    print("Calculator")
    num1 = "false"
    num2 = "false"
    while True:
        if num1 != "false" and num2 != "false":
            print("(1) +")
            print("(2) -")
            print("(3) *")
            print("(4) /")
            print("(5) sin(number1/number2)")
            print("(6) cos(number1/number2)")
            print("(7) Change numbers")
            print("(8) Quit")
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
                print("The result is:", math.sin(num1 / num2))
            if selection == "6":
                print("The result is:", math.cos(num1 / num2))
            if selection == "7":
                num1 = "false"
                num2 = "false"
            if selection == "8":
                print("Thank you!")
                break
        else:
            num1 = int(input("Give the first number: "))
            num2 = int(input("Give the second number: "))


# ex 6 Notebook
def read_file():
    file = open("notebook.txt", "r")
    file_content = file.read()
    print(file_content)
    file.close()

def add_to_file():
    text = input("Write a new note: ")
    file = open("notebook.txt", "a+")
    file_content = file.read()
    file.write(file_content + "\n" + text + ":::" + time.strftime("%X %x"))
    file.close()

def empty_file():
    file = open("notebook.txt", "w")
    file.write("")
    file.close()

def notebook():
    while True:
        print("(1) Read the notebook")
        print("(2) Add note")
        print("(3) Empty the notebook")
        print("(4) Quit")
        selection = input("Please select one: ")

        if selection == "1":
            read_file()
        if selection == "2":
            add_to_file()
        if selection == "3":
            print("Notes deleted.")
            empty_file()
        if selection == "4":
            print("Notebook shutting down, thank you.")
            break


if ownmodule.printstuff("Hey!") == True:
    print("Success!")
else:
    print("It's gone!")
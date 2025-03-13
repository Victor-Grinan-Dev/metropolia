import math
import time


# ex 1
def open_file(filename):
    try:
        filename = open(filename, "r")
        content = filename.read()
        filename.close()
        return content
    except:
        print("There seems to be no file with that name.")

def convert_to_int(value):
    try:
        int_content = int(value)
        return 1000 / int_content
    except:
        print("The file contents are unsuitable.")

def open_file_divide_by_1000():
    try:
        file = input("Give the file name: ")
        file_content = open_file(file)
        if file_content:
            result = convert_to_int(file_content)
            if result:
                print("The result was", result)
    except:
        print("There was a problem with the program.")

#ex 3
def calculator():
    checked_num1 = False
    checked_num2 = False
    num1 = "false"
    num2 = "false"

    print("Calculator")
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
                print("The result is:", num1 + num2)
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
            while not checked_num1:
                try:
                    num1 = int(input("Give a number: "))
                    checked_num1 = True
                except:
                    print("This input is invalid.")
            while not checked_num2:
                try:
                    num2 = int(input("Give a number: "))
                    checked_num2 = True
                except:
                    print("This input is invalid.")
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
                print("The result is:", num1 + num2)
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
            while not checked_num1:
                try:
                    num1 = int(input("Give a number: "))
                    checked_num1 = True
                except:
                    print("This input is invalid.")
            while not checked_num2:
                try:
                    num2 = int(input("Give a number: "))
                    checked_num2 = True
                except:
                    print("This input is invalid.")


def open_default_notebook(note_file):
    try:
        file = open(note_file, "r")
        file.close()
    except:
        file = open(note_file, "w")
        file.close()
        print("No default notebook was found, created one.")


def read_file(note_file):
    file = open(note_file, "r")
    file_content = file.read()
    print(file_content)
    file.close()


def add_to_file(note_file):
    text = input("Write a new note: ")
    file = open(note_file, "a+")
    file_content = file.read()
    file.write(file_content + "\n" + text + ":::" + time.strftime("%X %x"))
    file.close()


def empty_file(note_file):
    file = open(note_file, "w")
    file.write("")
    file.close()


def main():
    current_file = "notebook.txt"
    open_default_notebook(current_file)
    while True:
        print("Now using file", current_file)
        print("(1) Read the notebook")
        print("(2) Add note")
        print("(3) Empty the notebook")
        print("(4) Change the notebook")
        print("(5) Quit")
        selection = input("Please select one: ")

        if selection == "1":
            read_file(current_file)
        if selection == "2":
            add_to_file(current_file)
        if selection == "3":
            print("Notes deleted.")
            empty_file(current_file)
        if selection == "4":
            new_file = input("Give the name of the new file: ")
            try:
                file = open(new_file, "r")
                file.close()
            except:
                file = open(new_file, "w")
                file.close()
                print("No notebook with that name detected, created one.")

            current_file = new_file

        if selection == "5":
            print("Notebook shutting down, thank you.")
            break


main()

#ex 3
def ex3():
    file = open("strings.txt", "r") 
    lines = file.readlines()

    for line in lines:
        
        if line.strip().isalnum():
            print(line.strip() + " was ok.")
        else:
            print(line.strip() + " was invalid.")

    file.close()


# ex 4

def read_file():
    file = open("notebook.txt", "r")
    file_content = file.read()
    print(file_content)
    file.close()

def add_to_file(text):
    file = open("notebook.txt", "a+")
    file_content = file.read()
    file.write(file_content + "\n" + text)
    file.close()

def empty_file():
    file = open("notebook.txt", "w")
    file.write("")
    file.close()

def main():
    while True:
        print("(1) Read the notebook")
        print("(2) Add note")
        print("(3) Empty the notebook")
        print("(4) Quit")
        selection = input("Please select one: ")

        # if selection


empty_file()
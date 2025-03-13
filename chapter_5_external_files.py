#samples
def sample0():
    with open("ex13_sample.txt", "r") as file:
        content = file.read()  # Read the entire file content
        print(content)  # Print the file content

def sample1():
    readfile = open("ex13_sample.txt","r")
    content = readfile.readlines()
    print(content)
    for i in content:
        print(i)
    readfile.close()

def sample2():
    readfile = open("ex13_sample.txt","r")
    content = readfile.readlines()
    # print(variable, end = '')
    print(content)
    for i in content:
        print(i, end = '')
    readfile.close()

def sample3():
    readfile = open("ex13_sample.txt","r")
    content = readfile.readlines()
    # readline = readline[:-1]
    print(content)
    for i in content:
        print(i[:-1])
    readfile.close()

def delist(mylist):
    stringdata = ""
    for i in range(0,len(mylist)):
        stringdata = stringdata + "€$€" + str(mylist[i])
    return stringdata


def write_sample():
    myfile = open("writings.txt", "a")

    addedtext = "Added line!\n This goes to writings.txt! \
  which was created earlier.\n"

    print(addedtext)

    myfile.write(addedtext)
    myfile.close()

#ex 1
def ex3():
    file = open("strings.txt", "r") 
    lines = file.readlines()

    for line in lines:
        
        if line.strip().isalnum():
            print(line.strip() + " was ok.")
        else:
            print(line.strip() + " was invalid.")

    file.close()

# ex 2
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

if __name__ == "__main__":
    # mylist = [0,1,2,3,4,5,6,7,8,9]
    # print(delist(mylist))
    # sample0()
    pass
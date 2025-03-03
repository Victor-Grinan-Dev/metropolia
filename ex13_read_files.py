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
  myfile = open("writings.txt","a")

  addedtext = "Added line!\n This goes to writings.txt! \
  which was created earlier.\n"
  
  print(addedtext)
  
  myfile.write(addedtext)
  myfile.close()

if __name__ == "__main__":
    # mylist = [0,1,2,3,4,5,6,7,8,9]
    # print(delist(mylist))
    sample0()
    pass
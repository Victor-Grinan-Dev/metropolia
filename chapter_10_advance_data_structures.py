import pickle
import time

# 1 lists
def print_my_list():
    my_list = ["Blue", "Red", "Yellow", "Green"]
    print(f"The first item in the list is: {my_list[0]}")
    print("The entire list printed one item a time:")
    for i in range(len(my_list)):
        print(my_list[i])

# 2
def tryout():
    selection = input("""
Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: """)

def cart_items():
    cart = ["beer", "apple", "milk"]

    while True:
        selection = input("""
    Would you like to
    (1)Add or
    (2)Remove items or
    (3)Quit?: """)
        if int(selection) > 3 or int(selection) < 0:
            print("Incorrect selection.")
            continue
        else:
            if selection == "1":
                item = input("What will be added?: ")
                cart.append(item)
            elif selection == "2":
                to_delete = input(f"""
    There are {len(cart)} items in the list.
    Which item is deleted?: """)
                try:
                    cart.pop(int(to_delete))
                except:
                    print("Incorrect selection.")
                    continue
            elif selection == "3":
                print("The following items remain in the list:")
                for i in range(len(cart)):
                    print(cart[i])
                break

def words():
    with open("words.txt", "r") as file:
        content = file.readlines()
        content.sort()
        for word in content:
            print(word.strip())


def clean_file():
    write_file("")
# ex 4
def read_file(printing=False):
    try:
        file = open("notebook.dat", 'rb')
        content = pickle.load(file)
        if printing:
            for item in content:
                    print(item)
        else:
            return content
    except:
        return False

def add_date_item(item):
    return f"{item}:::{time.strftime("%X %x")}"

def write_file(content):
    file = open("notebook.dat", "wb")
    pickle.dump(content, file)
    file.close()

def add_a_note():
    new_note = input("Write a new note: ")
    if read_file():
        content = read_file()
        content.append(add_date_item(new_note))
        write_file(content)
    else:
        write_file([add_date_item(new_note)])

def edit_a_note():
    content = read_file()
    print(f"The list has {len(content)} notes.")
    index = int(input("Which of them will be changed?: "))
    print(content[index])
    new_note = input("Give the new note: ")
    content[index] = add_date_item(new_note)
    write_file(content)

def delete_a_note():
    content = read_file(False)
    print(f"The list has {len(content)} notes.")
    note_index = int(input("Which of them will be deleted?: "))
    try:
        deleted_note = content.pop(note_index)
    except:
        deleted_note = content.pop(note_index + 1)

    write_file(content)
    print("Deleted note", deleted_note)

def main():
    try:
        file = open("notebook.dat", "rb")
        file.close()
    except:
        file = open("notebook.dat", "wb")
        file.close()
        print("No default notebook was found, created one.")
    while True:
        print("(1) Read the notebook")
        print("(2) Add note")
        print("(3) Edit a note")
        print("(4) Delete a note")
        print("(5) Save and quit\n")
        selection = input("Please select one: ")

        if selection == "1":
            read_file(True)
        if selection == "2":
            add_a_note()
        if selection == "3":
            edit_a_note()
        if selection == "4":
            delete_a_note()
        if selection == "5":
            print("Notebook shutting down, thank you.")
            break

main()
#clean_file()
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


# Put your code here
employees = []


def main():
    index = 0
    while True:
        resp = input("Please enter employee name (0 to quit):")
        if resp == "0":
            break
        else:
            index += 1
            new_employee = Employee(index, resp)
            employees.append(new_employee)
    return 0


main()

for employee in employees:
    print("Id:", employee.id, "Name:", employee.name)
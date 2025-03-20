class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PayrollSystem:
    """ takes a list of SalaryEmployee objects and prints payroll """
    def __init__(self, employees_list):
        self.employees_list = employees_list

    def calculate_payroll(self):
        for employee in self.employees_list:
            print("Employee Payroll")
            print("================")
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f"- Check amount: {employee.calculate_salary()}")
            print()


class SalaryEmployee(Employee):

    def __init__(self,  id, name, monthly_salary):
        super().__init__(id, name)
        self._monthly_salary = monthly_salary

    def calculate_salary(self):
        return self._monthly_salary


employees = []
def main():
    index = 0
    while True:
        resp = input("Please enter employee name (0 to quit):")
        if resp == "0":
            new_payroll = PayrollSystem(employees)
            new_payroll.calculate_payroll()
            break
        else:
            salary = int(input("Please enter salary:"))
            index += 1
            new_employee = SalaryEmployee(index, resp, salary)
            employees.append(new_employee)
    return 0

if __name__ == "__main__":
    main()
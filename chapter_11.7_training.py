# Exercise

class PayrollSystem:
    def calculate_payroll(self, employees):
        for employee in employees:
            print('Employee Payroll')
            print('================')
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_salary()}')
            print('')


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def ask_name(self):
        try:
            self.name = str(input("Please enter employee name:"))
        except:
            self.name = ''


class SalaryEmployee(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.salary = 'M'
        self.monthly_salary = int(monthly_salary)

    def ask_salary(self):
        try:
            self.monthly_salary = int(input("Please enter monthly salary:"))
        except:
            self.monthly_salary = 0

    def calculate_salary(self):
        return self.monthly_salary

#___________________________________________________________________________
#___________________________________________________________________________
# Put your code here
class HourlyEmployee(Employee):

    def __init__(self, id, name, hours_worked=0, hour_rate=0):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def ask_salary(self):
        self.hours_worked = int(input("Please enter hours worked:"))
        self.hour_rate = int(input("Please enter hour rate:"))

    def calculate_salary(self):
        return self.hour_rate * self.hours_worked

class CommissionEmployee(SalaryEmployee):

    def __init__(self, id, name, monthly_salary, commission):
        super().__init__(id, name, monthly_salary)
        self.commission = commission

    def ask_salary(self):
        try:
            self.monthly_salary = int(input("Please enter monthly salary:"))
        except:
            self.monthly_salary = 0
        try:
            self.commission = int(input("Please enter commission:"))
        except:
            self.commission = 0

    def calculate_salary(self):
        return self.monthly_salary + self.commission

#___________________________________________________________________________
#___________________________________________________________________________

employees = []
id = 1
while True:
    salarytype = int(input("Please enter salary type:\n(1) monthly\n(2) hourly\n(3) commission\n(0) Quit\n"))
    if salarytype == 1:
        employee = SalaryEmployee(id, '', 0)
        SalaryEmployee.ask_name(employee)
        SalaryEmployee.ask_salary(employee)
        employees.append(employee)
        id += 1
    elif salarytype == 2:
        employee = HourlyEmployee(id, '', 0, 0)
        HourlyEmployee.ask_name(employee)
        HourlyEmployee.ask_salary(employee)
        employees.append(employee)
        id += 1
    elif salarytype == 3:
        employee = CommissionEmployee(id, '', 0, 0)
        CommissionEmployee.ask_name(employee)
        CommissionEmployee.ask_salary(employee)
        employees.append(employee)
        id += 1
    elif salarytype == 0:
        break
    else:
        print("Incorrect selection.")
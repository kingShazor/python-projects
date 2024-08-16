import json

class Employee:
    def __init__(self,name,jobDesc,salaryGroup,performanceGroup):
        self.name = name
        self.jobDesc = jobDesc
        self.salaryGroup = salaryGroup
        self.performanceGroup = performanceGroup



class EmployeeList:
    def __init__(self):
        self.list = []

    def add_employee(self, employee):
        self.list.append(employee)

    def get_employees(self):
        return self.list

    def save_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.get_employees(), file)

    def load_file(self, filename):
        with open(filename, 'r') as file:
            employees = json.load(file)
            for name, jobDesc, salaryGroup, performanceGroup in employees:
                employee = Employee(name, jobDesc, salaryGroup, performanceGroup)
                self.add_employee(employee)




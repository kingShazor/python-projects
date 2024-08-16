import json

class Employee:
    def __init__(self,name,jobDesc,salaryGroup,performanceGroup):
        self.name = name
        self.jobDesc = jobDesc
        self.salaryGroup = salaryGroup
        self.performanceGroup = performanceGroup

    def copy_values(self,oth):
        self.name = oth.name
        self.jobDesc = oth.jobDesc
        self.salaryGroup = oth.salaryGroup
        self.performanceGroup = oth.performanceGroup

class EmployeeList:
    def __init__(self):
        self.list = []

    def find_employee(self, name):
        index = [i for i, listEmployee in enumerate(self.list) if listEmployee.name == name]
        if len(index) > 0:
            return self.list[index.pop()]
        return None

    def add_employee(self, employee):
        listEmployee = self.find_employee(employee.name)
        if listEmployee:
            listEmployee.copy_values(employee)
        else:
            self.list.append(employee)

    def get_employees(self):
        return self.list

    def clear(self):
        self.list.clear()

    def save_file(self, filename):
    
        out = []
        for employee in self.get_employees():
            out.append( (employee.name, employee.jobDesc, employee.salaryGroup, employee.performanceGroup))
        with open(filename, 'w') as file:
            json.dump(out, file)
    
    def load_file(self, filename):
        with open(filename, 'r') as file:
            employees = json.load(file)
            self.clear()
            for name, jobDesc, salaryGroup, performanceGroup in employees:
                employee = Employee(name, jobDesc, salaryGroup, performanceGroup)
                self.add_employee(employee)




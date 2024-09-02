import json
import matplotlib.pyplot as plt
import math

class Employee:
    def __init__(self,name,jobDesc,salaryGroup,performanceGroup,avatar_path):
        self.name = name
        self.jobDesc = jobDesc
        self.salaryGroup = salaryGroup
        self.performanceGroup = performanceGroup
        self.avatar_path = avatar_path

    def copy_values(self,oth):
        self.name = oth.name
        self.jobDesc = oth.jobDesc
        self.salaryGroup = oth.salaryGroup
        self.performanceGroup = oth.performanceGroup
        self.avatar_path = oth.avatar_path

class EmployeeList:
    def __init__(self):
        self.list = []
        self.performance_desc = ["d","c","b3","b2","b1","a"] # todo eine Deklaration

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
    
    def remove(self, employee):
        try:
            self.list.remove(employee)
            return True
        except ValueError:
            return False

    def save_file(self, filename):
        out = []
        for employee in self.get_employees():
            out.append( (employee.name, employee.jobDesc, employee.salaryGroup, employee.performanceGroup, employee.avatar_path))
        with open(filename, 'w') as file:
            json.dump(out, file)
   
    def load_from_file(self,filename):
        with open(filename, 'r') as file:
            employees = json.load(file)
        return employees

    def file_size(self, filename):
        return len(self.load_from_file(filename))

    def load_file(self, filename):
            self.clear()
            employees = self.load_from_file(filename)
            for employee_data in employees:
                if len(employee_data) == 4:
                    name, jobDesc, salaryGroup, performanceGroup = employee_data
                    avatar_path = "pics/fallback.png" #todo vereinheitlichen - nur eine angabe vom fallback.png im programm
                else:
                    name, jobDesc, salaryGroup, performanceGroup, avatar_path = employee_data

                employee = Employee(name, jobDesc, salaryGroup, performanceGroup, avatar_path)
                self.add_employee(employee)
    def get_values(self):
        y = [0,0,0,0,0,0]
        for employee in self.get_employees():
            y[self.performance_desc.index(employee.performanceGroup)] += 1
        return y

    def normalization(self, x):
        mu = 3
        sigma = math.sqrt(2)
        return (1 / (sigma * math.sqrt(2 * math.pi)))* math.exp(-((x - mu) ** 2) / (2 *sigma **2 ))

    def calc_balancing_factor(self):
        count = 0
        for i in range(len(self.performance_desc)):
            count += self.normalization(i)

        return 1/count

    def calc_normation(self):
        i = 0
        allcount = 0
        balancing_factor = self.calc_balancing_factor()
        print(f"balancing factor: {balancing_factor}")
        res = []
        for desc in self.performance_desc:
            count = self.normalization(i) * len(self.list) * balancing_factor
            allcount += count
            res.append(round(count))
            print( f"value expected for {desc}: {res[-1]}")
            i += 1
        print( f"allcount: {allcount}")
        return res

    def plot_performance(self):
        plt.style.use('dark_background')
        plt.plot(self.performance_desc, self.get_values(), label='Leistungsbewertung', marker='o')
        plt.xlabel("Leistungsbewertung")
        plt.ylabel("Anzahl")
        plt.title("Leistungsbewertung von L-Tec")
        plt.legend()
        plt.show()
        target_values = self.calc_normation()
        values = self.get_values()
        for i in range(len(target_values)):
            delta = target_values[i] - values[i]
            print(f"{self.performance_desc[i]} has a delta value {delta}")

        


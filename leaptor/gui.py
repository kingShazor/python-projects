import tkinter as tk
from tkinter import messagebox
from data import *

class LeaptorGUI:
    def __init__(self):
        self.employees = EmployeeList()
        self.root = tk.Tk()
        self.root.title("Leaptor")

        self.label_name = tk.Label(self.root, text = "Vorname & Nachname:")
        self.label_name.grid(row=0, column=0)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1)

        self.label_jobDesc = tk.Label(self.root, text="Jobprofil:")
        self.label_jobDesc.grid(row=1, column=0)
        self.entry_jobDesc = tk.Entry(self.root)
        self.entry_jobDesc.grid(row=1, column=1)

        self.label_salary = tk.Label(self.root, text="Gehaltsgruppe:")
        self.label_salary.grid(row=2, column=0)
        self.entry_salary = tk.Entry(self.root)
        self.entry_salary.grid(row=2, column=1)

        self.label_performance = tk.Label(self.root, text="Leistungsbewertung")
        self.label_performance.grid(row=3, column=0)
        self.entry_performance = tk.Entry(self.root)
        self.entry_performance.grid(row=3, column=1)

        self.button_save_employee = tk.Button(self.root, text="Mitarbeiter speichern", command=self.save_employee)
        self.button_save_employee.grid(row=4, column=1)

        self.employee_list_box = tk.Listbox(self.root, width=50, height=25)
        self.employee_list_box.grid(row=5, columnspan=2, column=0)

        self.button_load_file = tk.Button(self.root, text="Gehälter von Datei laden", command=self.load_file)
        self.button_load_file.grid(row=6, column=0)
        self.button_save_file = tk.Button(self.root, text="Gehälter in Datei speichern", command=self.save_file)
        self.button_save_file.grid(row=6, column=1)

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_jobDesc.delete(0, tk.END)
        self.entry_salary.delete(0, tk.END)
        self.entry_performace.delete(0, tk.END)

    def refresh_employee_list_box(self):
        self.employee_list_box.delete(0, tk.END)
        for employee in self.employees.get_employees():
           self.employee_list_box.insert(tk.END, f"{employee.name}-{employee.jobDesc}:{employee.salaryGroup}{employee.performanceGroup}");


    def save_employee(self):
        name = self.entry_name.get()
        jobDesc = self.entry_jobDesc.get()
        salaryGroup = self.entry_salary.get()
        performance = self.entry_performance.get()

        employee = Employee(name, jobDesc, salaryGroup, performance)
        self.employees.add_employee(employee);
        self.refresh_employee_list_box()
        self.clear_entries()


    def save_file(self):
        self.employees.save_file("employee.json")

    def load_file(self):
        clear_entries()
        self.employee_list_box.delete(0, tk.END) # todo später abmischen

        self.employees.load_file("employee.json")

    def run(self):
        self.root.mainloop()









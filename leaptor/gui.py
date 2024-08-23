import tkinter as tk
from tkinter import messagebox, ttk
from data import *
from PIL import Image, ImageTk

class LeaptorGUI:
    def __init__(self):
        self.employees = EmployeeList()
        self.root = tk.Tk()
        self.root.title("Leaptor")
        
        self.root.tk.call("source", "theme/azure.tcl")
        self.root.tk.call("set_theme", "dark")

        windowWidth = 500
        windowHeight = 700

        self.canvas = tk.Canvas(self.root, width=windowWidth, height=windowHeight)
        self.canvas.grid(row=0, column=0, columnspan=3, rowspan=7)

        texture = Image.open("pics/dino-texture.png")
        texture = texture.resize((windowWidth, windowHeight), Image.Resampling.LANCZOS)
        self.texture = ImageTk.PhotoImage(texture)
        
        self.canvas.create_image(0,0, anchor=tk.NW, image=self.texture)

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

        self.salary_value = tk.StringVar(self.root)
        self.salary_values = ["1", "2", "3", "4", "5", "6", "7", "8"]
        self.salary_default = 3
        self.salary_value.set(self.salary_values[self.salary_default])
        self.entry_salary = tk.OptionMenu(self.root, self.salary_value, *self.salary_values)
        self.entry_salary.grid(row=2, column=1)

        self.label_performance = tk.Label(self.root, text="Leistungsbewertung")
        self.label_performance.grid(row=3, column=0)
        
        self.performance_value = tk.StringVar(self.root)
        self.performance_values = ["d","c","b3","b2","b1","a"]
        self.performance_default = 3
        self.performance_value.set(self.performance_values[self.performance_default])
        self.entry_performance = tk.OptionMenu(self.root, self.performance_value, *self.performance_values)
        self.entry_performance.grid(row=3, column=1)

        self.button_save_employee = tk.Button(self.root, text="Mitarbeiter speichern", command=self.save_employee)
        self.button_save_employee.grid(row=4, column=1)

        self.employee_list_box = tk.Listbox(self.root, width=50, height=25)
        self.employee_list_box.grid(row=5, columnspan=2, column=0)
        self.employee_list_box.bind("<Double-1>", self.on_double_click)

        self.button_load_file = tk.Button(self.root, text="Mitarbeiter aus Datei lesen", command=self.load_file)
        self.button_load_file.grid(row=6, column=0)
        self.button_save_file = tk.Button(self.root, text="Mitarbeiter in Datei speichern", command=self.save_file)
        self.button_save_file.grid(row=6, column=1)

#        image = Image.open("pics/Profilbild.png")
#        print(image.size)
#        image = image.resize((50,50), Image.Resampling.LANCZOS)
#        self.avatar = ImageTk.PhotoImage(image)
#
#        self.label_avatar = tk.Label(self.root, image=self.avatar)
#        self.label_avatar.grid(row=7, column=0, pady=10)


    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_jobDesc.delete(0, tk.END)
        self.salary_value.set(self.salary_values[self.salary_default])
        self.performance_value.set(self.performance_values[self.performance_default])

    def get_current_selection(self):
        selected = self.employee_list_box.curselection()
        if selected:
            text = self.employee_list_box.get(selected[0])
            name = text.split("-")[0]
            return self.employees.find_employee(name)


    def on_double_click(self, event):
        employee = self.get_current_selection()
        if employee:
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, employee.name)
            self.entry_jobDesc.delete(0, tk.END)
            self.entry_jobDesc.insert(0, employee.jobDesc)
            self.performance_value.set(employee.performanceGroup)
            self.salary_value.set(employee.salaryGroup)
        else:
            messagebox.showerror("Fehler", "Das Hervorheben eines Mitarbeiters ist unerwartet fehlgeschlaten")

    def refresh_employee_list_box(self):
        self.employee_list_box.delete(0, tk.END)
        for employee in self.employees.get_employees():
           self.employee_list_box.insert(tk.END, f"{employee.name}-'{employee.jobDesc}':{employee.salaryGroup}{employee.performanceGroup}");

    def save_employee(self):
        name = self.entry_name.get()
        jobDesc = self.entry_jobDesc.get()
        salaryGroup = self.salary_value.get()
        performance = self.performance_value.get()

        employee = Employee(name, jobDesc, salaryGroup, performance)
        self.employees.add_employee(employee);
        self.refresh_employee_list_box()
        self.clear_entries()

    def save_file(self):
        try:
            file_name = "employee.json"
            self.employees.save_file(file_name)
            messagebox.showinfo( "Mitarbeiter gespeichert", f"Mitarbeiter erfolgreich in der Datei {file_name} gespeichert!")
        except Exception as e:
            messagebox.showerror( "Schreibefehler", f"Es ist ein unerwarteter Fehler aufgetreten: {e}")

    def load_file(self):
        try:
            file_name = "employee.json"
            self.employee_list_box.delete(0, tk.END) # todo später abmischen

            self.employees.load_file(file_name)
            self.refresh_employee_list_box()
            messagebox.showinfo( "Mitarbeiter geladen", f"Mitarbeiter erfolgreich aus der Datei {file_name} geladen!")
        except FileNotFoundError:
            messagebox.showerror( "Ladefehler", f"Das Laden der Datei {file_name} ist fehlgeschlagen. Die Datei ist nicht vorhanden!")
        except Exception as e:
            messagebox.showerror( "Ladefehler", f"Es ist ein unerwarteter Fehler aufgetreten: {e}")


    def run(self):
        self.root.mainloop()


import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from data import *
from PIL import Image, ImageTk

class LeaptorGUI:
    def __init__(self):
        self.employees = EmployeeList()
        self.root = tk.Tk()
        self.root.title("Leaptor")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.bind("<Configure>", self.resize)

        self.mainFrame = tk.Frame(self.root)
        self.mainFrame.grid(row=0, column=0)
        self.currentFrame = self.mainFrame

        self.root.tk.call("source", "theme/azure.tcl")
        self.root.tk.call("set_theme", "dark")

        self.rootFileDialog = tk.Tk()
        self.rootFileDialog.tk.call("source", "theme/azure.tcl")
        self.rootFileDialog.tk.call("set_theme", "light")
        self.rootFileDialog.withdraw()

        self.min_window_width = 725
        self.min_window_height = 725

        self.canvas = tk.Canvas(self.mainFrame, width=self.min_window_width, height=self.min_window_height)
        self.canvas.grid(row=0, column=0, columnspan=3, rowspan=9)

        self.orig_texture = Image.open("pics/dino-texture.png")
        texture = self.orig_texture.resize((self.min_window_width, self.min_window_height), Image.Resampling.LANCZOS)
        self.texture = ImageTk.PhotoImage(texture)
        
        self.background_image = self.canvas.create_image(0,0, anchor=tk.NW, image=self.texture)
        self.currentCanvas = self.canvas

        self.teamLeadFrame = tk.Frame(self.root)
        self.teamLeadFrame.grid(row=0, column=0)
        self.canvas_team_lead = tk.Canvas(self.teamLeadFrame, width=self.min_window_width, height=self.min_window_height)
        self.canvas_team_lead.grid(row=0, column=0)
        self.background_team_lead = self.canvas_team_lead.create_image(0,0, anchor=tk.NW, image=self.texture)


        self.fallback_avatar = "pics/fallback.png"

#       image_company = Image.open("pics/L-Tec.png")
#       image_company = image_company.resize((140,140), Image.Resampling.LANCZOS)
#       self.photo_company = ImageTk.PhotoImage(image_company)


        self.label_avatar = tk.Label(self.mainFrame) 
        self.label_avatar.grid(row=0, column=0, pady=10, rowspan=4)
        self.load_avatar(None)
        self.label_name = tk.Label(self.mainFrame, text = "Vorname & Nachname:")
        self.label_name.grid(row=0, column=1)
        self.entry_name = tk.Entry(self.mainFrame)
        self.entry_name.grid(row=0, column=2)

        self.label_jobDesc = tk.Label(self.mainFrame, text="Jobprofil:")
        self.label_jobDesc.grid(row=1, column=1)
        self.entry_jobDesc = tk.Entry(self.mainFrame)
        self.entry_jobDesc.grid(row=1, column=2)

        self.label_salary = tk.Label(self.mainFrame, text="Gehaltsgruppe:")
        self.label_salary.grid(row=2, column=1)

        self.salary_value = tk.StringVar(self.mainFrame)
        self.salary_values = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        self.salary_default = 3
        self.salary_value.set(self.salary_values[self.salary_default])
        self.entry_salary = tk.OptionMenu(self.mainFrame, self.salary_value, *self.salary_values)
        self.entry_salary.grid(row=2, column=2)

        self.label_performance = tk.Label(self.mainFrame, text="Leistungsbewertung")
        self.label_performance.grid(row=3, column=1)
        
        self.performance_value = tk.StringVar(self.mainFrame)
        self.performance_values = ["d","c","b3","b2","b1","a"]
        self.performance_default = 3
        self.performance_value.set(self.performance_values[self.performance_default])
        self.entry_performance = tk.OptionMenu(self.mainFrame, self.performance_value, *self.performance_values)
        self.entry_performance.grid(row=3, column=2)

        self.button_change_avatar = tk.Button(self.mainFrame, text="Profilbild ändern", command=self.get_avatar_path) # todo function
        self.button_change_avatar.grid(row=4, column=0)
        self.button_save_employee = tk.Button(self.mainFrame, text="Mitarbeiter speichern", command=self.save_employee)
        self.button_save_employee.grid(row=4, column=1)
        self.button_remove_employee = tk.Button(self.mainFrame, text="Mitarbeiter löschen", command=self.remove_employee)
        self.button_remove_employee.grid(row=4, column=2)

        self.employee_list_box = tk.Listbox(self.mainFrame, width=40, height=25)
        self.employee_list_box.grid(row=5, columnspan=2, column=0, rowspan=4, pady=10)
        self.employee_list_box.bind("<Double-1>", self.on_double_click)

#       self.button_frame = tk.Frame(self.mainFrame)
#       self.button_frame.grid(row=5, column=2)
        
        self.button_load_file = tk.Button(self.mainFrame, text="Mitarbeiter aus Datei lesen", command=self.load_file)
        self.button_load_file.grid(row=5, column=2)
        self.button_save_file = tk.Button(self.mainFrame, text="Mitarbeiter in Datei speichern", command=self.save_file)
        self.button_save_file.grid(row=6, column=2)
        self.button_plot_performance = tk.Button(self.mainFrame, text="Teamleistungsbewertung anzeigen", command=self.plot_performance)
        self.button_plot_performance.grid(row=7, column=2)
        self.button_show_team_lead = tk.Button(self.mainFrame, text="Teamleitung ansehen", command=self.show_team_lead)
        self.button_show_team_lead.grid(row=8, column=2)

        self.mainFrame.tkraise()

        self.window_height = self.root.winfo_height()
        self.window_width = self.root.winfo_width()

        self.tl_name_label = tk.Label(self.teamLeadFrame, text="team lead test")
        self.tl_name_label.grid(row=0, column=0)


    def on_closing(self):
        if self.rootFileDialog:
            self.rootFileDialog.destroy()
        self.root.destroy()

    def resize(self, event):
        new_width = self.root.winfo_width()
        new_height = self.root.winfo_height()
        #only consider the window resize
        if event.width == new_width and event.height == new_height:
            self.resize_background(new_width, new_height)

    def redraw_background(self):
            texture = self.orig_texture.resize((self.window_width, self.window_height), Image.Resampling.LANCZOS)
            self.texture = ImageTk.PhotoImage(texture)
            self.currentCanvas.config(width=self.window_width, height=self.window_height)
            self.currentCanvas.itemconfig(self.background_image, image=self.texture) 

    def resize_background(self, new_width, new_height):
        if (new_height > self.min_window_height and new_width > self.min_window_width) and (abs(new_height - self.window_height) >4 or abs(new_width - self.window_width) >4):
            self.window_width = new_width
            self.window_height = new_height
            self.redraw_background()
            print(f"resize: {new_width}, {new_height}")


            #self.canvas.itemconfig(self.

    def show_team_lead(self):
        print("Show team lead")
        last_width = self.currentFrame.winfo_width()
        last_height = self.currentFrame.winfo_height()
        self.currentFrame.grid_forget()
        self.currentFrame = self.teamLeadFrame
        #self.canvas_team_lead.config(width=last_width, height=last_height)
        #self.background_team_lead = self.canvas_team_lead.create_image(0,0, anchor=tk.NW, image=self.texture)
        self.currentCanvas = self.canvas_team_lead
        self.redraw_background()

        #self.currentFrame.grid(row=0, column=0)

        self.currentFrame.tkraise()

    def load_avatar(self, avatar_path):
        self.avatar_path = avatar_path
        if avatar_path:
            image = Image.open(avatar_path)
        else:
            image = Image.open(self.fallback_avatar)

        print(image.size) # debug can be removede
        image = image.resize((140,140), Image.Resampling.LANCZOS)
        self.avatar = ImageTk.PhotoImage(image)
        self.label_avatar.config(image=self.avatar)

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_jobDesc.delete(0, tk.END)
        self.salary_value.set(self.salary_values[self.salary_default])
        self.performance_value.set(self.performance_values[self.performance_default])
        self.load_avatar(None)

    def remove_employee(self):
        name = self.entry_name.get()
        if name:
            success = False
            employee = self.employees.find_employee(name)
            if employee:
                res = self.employees.remove(employee)
                if res:
                    self.refresh_employee_list_box()
                    self.clear_entries()
                    success = True
            if not success:
                messagebox.showerror("Löschfehlschlag", f"Das Löschen des Mitarbeiter ist fehlgeschlagen. Mitarbeiter '{name}' konnte nicht gefunden werden.")
        else:
            messagebox.showerror("Löschfehlschlag", "Das Löschen des Mitarbeiter ist fehlgeschlagen. Keinen ausgewählt, oder?")

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
            self.load_avatar(employee.avatar_path)
        else:
            messagebox.showerror("Fehler", "Das Hervorheben eines Mitarbeiters ist unerwartet fehlgeschlaten")

    def refresh_employee_list_box(self):
        self.employee_list_box.delete(0, tk.END)
        for employee in self.employees.get_employees():
            self.employee_list_box.insert(tk.END, f"{employee.name}-'{employee.jobDesc}':{employee.salaryGroup}{employee.performanceGroup}");
    
    def get_avatar_path(self):
        #self.root.tk.call("set_theme", "light")
        file_path = filedialog.askopenfilename( title="Bild auswählen",
                                                master=self.rootFileDialog,
                                                initialdir=".",
                                                filetypes=[("Image Files", "*.png")]) #;*.jpg;*.jpeg;*.bmp;*.gif")] )
        if file_path:
            print(f"file ausgewählt: {file_path}")
        else:
            print("Keine File wurde ausgewält")
        #self.root.tk.call("set_theme", "dark") mysterios error!
        self.load_avatar(file_path)

    def save_employee(self):
        name = self.entry_name.get()
        jobDesc = self.entry_jobDesc.get()
        salaryGroup = self.salary_value.get()
        performance = self.performance_value.get()
        name_min_length = 5

        if len(name) >= name_min_length:
            employee = Employee(name, jobDesc, salaryGroup, performance, self.avatar_path)
            self.employees.add_employee(employee);
            self.refresh_employee_list_box()
            self.clear_entries()
        else:
            messagebox.showerror("Mitarbeitername ist ungültig", f"Der Name des Mitarbeiters ist nicht lang genug. Es muss mindestens {name_min_length}-Zeichen lang sein!")

    def save_file(self):
        file_name = "employee.json" # todo nur einmal deklarieren
        try:
            list_length = len(self.employees.list)
            if list_length > 0:
                save = True
                if list_length < self.employees.file_size(file_name):
                    save = messagebox.askokcancel( "Mitarbeiterdatei überschreiben?", "Die vorhande Mitarbeiterdatei ist größer als die aktuelle Liste. Wollen sie die Datei mit den aktuellen Werten überschreiben" )

                if save:
                    self.employees.save_file(file_name)
                    messagebox.showinfo( "Mitarbeiter gespeichert", f"Mitarbeiter erfolgreich in der Datei {file_name} gespeichert!")
            else:
                messagebox.showerror( "Schreibfehler", "Es ist kein Mitarbeiter zum schreiben vorhanden!")
        except Exception as e:
            messagebox.showerror( "Schreibefehler", f"Es ist ein unerwarteter Fehler aufgetreten: {e}")

    def load_file(self):
        try:
            file_name = "employee.json"
            self.employee_list_box.delete(0, tk.END)

            self.employees.load_file(file_name)
            self.refresh_employee_list_box()
            messagebox.showinfo( "Mitarbeiter geladen", f"Mitarbeiter erfolgreich aus der Datei {file_name} geladen!")
        except FileNotFoundError:
            messagebox.showerror( "Ladefehler", f"Das Laden der Datei {file_name} ist fehlgeschlagen. Die Datei ist nicht vorhanden!")
        except Exception as e:
            messagebox.showerror( "Ladefehler", f"Es ist ein unerwarteter Fehler aufgetreten: {e}")

    def plot_performance(self):
        self.employees.plot_performance()

    def run(self):
        self.root.mainloop()


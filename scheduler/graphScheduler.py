import heapq
import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, name, priority, desc=""):
        self.name = name
        self.priority = priority
        self.desc = desc;

    def __lt__(self,other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(name={self.name}, priority={self.priority}, description={self.desc})"

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, task):
        heapq.heappush(self.queue, (-task.priority, self.index, task))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
 
    def peek(self):
        return self.queue[0][-1] if not self.is_empty() else None

import json

class TaskScheduler:
    def __init__(self):
        self.tasks = PriorityQueue()
    
    def add_task(self, task):
        self.tasks.push(task)

    def show_tasks(self):
        items = sorted(self.tasks.queue, key=lambda x: x[0])
        return [item[-1] for item in items]

    def process_task(self):
        if not self.tasks.is_empty():
            return self.tasks.pop()

    def remove_task(self, name):
        self.tasks.queue = [(p,i,t) for p, i, t in self.tasks.queue if t.name != name]
        heapq.heapify(self.tasks.queue)

    def save_tasks(self, filename):
        tasks = [(t.name, -p, t.desc) for p, i, t in self.tasks.queue]
        with open(filename, 'w') as f:
            json.dump(tasks, f)

    def load_tasks(self, filename):
        with open(filename, 'r') as f:
            tasks = json.load(f)
            for name, priority, desc in tasks:
                task = Task(name, priority, desc)
                self.add_task(task)


class TaskSchedulerGUI:
    def __init__(self, root):
        self.scheduler = TaskScheduler()

        self.root = root
        self.root.title("Task Scheduler")

        self.name_label = tk.Label(root, text="Aufgabenname:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.priority_label = tk.Label(root, text="Priorität:")
        self.priority_label.grid(row=1, column=0)
        self.priority_entry = tk.Entry(root)
        self.priority_entry.grid(row=1, column=1)

        self.description_label = tk.Label(root, text="Beschreibung")
        self.description_label.grid(row=2, column=0)
        self.description_entry = tk.Entry(root)
        self.description_entry.grid( row=2, column=1)

        self.add_button = tk.Button(root, text="Aufgabe hinzufügen", command=self.add_task)
        self.add_button.grid(row=3, column=0, columnspan=2)

        self.task_listbox = tk.Listbox(root, height=10, width=50)
        self.task_listbox.grid(row=4, column=0, columnspan=2)

        self.process_button = tk.Button(root, text="Aufgabe verarbeiten", command=self.process_task)
        self.process_button.grid(row=5, column=0)

        self.remove_button = tk.Button(root, text="Aufgabe entfernen", command=self.remove_task)
        self.remove_button.grid(row=5, column=1)

        self.save_button = tk.Button(root, text="Aufgaben Speichern", command=self.save_tasks)
        self.save_button.grid(row=6, column=0)

        self.load_button = tk.Button(root, text="Aufgabe Laden", command=self.load_tasks)
        self.load_button.grid(row=6, column=1)

        self.update_task_list()

    def add_task(self):
        name = self.name_entry.get()
        priority = self.priority_entry.get() # todo check range 0-100
        description = self.description_entry.get()
        if name and priority:
            try:
                priority = int(priority)
                task = Task(name, priority, description)
                self.scheduler.add_task(task)
                self.update_task_list()
                self.name_entry.delete(0, tk.END)
                self.priority_entry.delete(0, tk.END)
                self.description_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("ungültige Priorität", "Priorität muss eine Zahl sein.")
        else:
            messagebox.showerror("Fehlende Information", "Name und Priorität sind erforderlich")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        tasks = self.scheduler.show_tasks()
        for task in tasks:
            self.task_listbox.insert(tk.END, f"{task.priority} - '{task.name}' ({task.desc})")

    def process_task(self):
        task = self.scheduler.process_task()
        if task:
            messagebox.showinfo("Aufgabe verarbeitet", f"Aufabge '{task.name}' wurde verarbeitet")
            self.update_task_list()
        else:
            messagebox.showinfo("Keine Aufgaben", "Keine Aufgaben zu verarbeiten.")

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            task_info = self.task_listbox.get(selected[0])
            task_name = task_info.split("'")[1]
            self.scheduler.remove_task(task_name)
            self.update_task_list()
        else:
            messagebox.showerror("Keine Auswahl", "Keine Aufgabe ausgewählt.")

    def save_tasks(self):
        filename = "tasks.json"
        self.scheduler.save_tasks(filename)
        messagebox.showinfo("Aufaben gespeichert", f"Aufgaben wurden in {filename} gespeichert.")

    def load_tasks(self):
        filename = "tasks.json"
        self.scheduler.load_tasks(filename)
        self.update_task_list()
        messagebox.showinfo("Aufgaben geladen", f"Aufgaben wurden aus {filename} geladen.")

def main():
    root = tk.Tk()
    gui = TaskSchedulerGUI(root)
    root.mainloop()
    

if __name__ == "__main__":
    main()

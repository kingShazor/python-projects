import heapq

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
        for item in items:
            print(item[-1])

    def process_task(self):
        if not self.tasks.is_empty():
            task = self.tasks.pop()
            print(f"Verarbeite Aufgabe: {task}")
        else:
            print("Keine Aufgabe zu verarbeiten!")

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

def main():
    scheduler = TaskScheduler()

    while True:
        print("\n1. Aufgabe hinzufügen")
        print("2. Aufgabe anzeigen")
        print("3. Aufgabe verarbeiten")
        print("4. Aufgabe entfernen")
        print("5. Aufgaben speichern")
        print("6. Aufgaben laden")
        print("7. Scheduler beenden")

        choice = input("wähle eine Option: ")
        
        if choice == "1":
            name = input("Name der Aufgabe: ")
            priority = int(input("Priorität der Aufgabe: "))
            desc = input("Beschreibung der Aufgabe (optional): ")
            task = Task(name, priority, desc)
            scheduler.add_task(task)
        elif choice == "2":
            scheduler.show_tasks()
        elif choice == "3":
            scheduler.process_task()
        elif choice == "4":
            name = input("Name der zu entfernenden Aufgabe: " )
            scheduler.remove_task(name)
        elif choice == "5":
            filename = input("Dateiname zum Speichern: ")
            scheduler.save_tasks(filename)
        elif choice == "6":
            filename = input("Name der zu ladenen Datei: ")
            scheduler.load_tasks(filename)
        elif choice == "7":
            break
        else:
            print("ungültige Auswahl, bitte erneut versuchen.")


if __name__ == "__main__":
    main()

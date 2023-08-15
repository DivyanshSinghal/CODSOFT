import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.heading_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 24))
        self.heading_label.pack(pady=10)

        self.task_entry = tk.Entry(root, font=("Helvetica", 14), width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", font=("Helvetica", 12), command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, font=("Helvetica", 14), width=40, height=10)
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", font=("Helvetica", 12), command=self.delete_task)
        self.delete_button.pack(pady=10)

        self.update_button = tk.Button(root, text="Update Task", font=("Helvetica", 12), command=self.update_task)
        self.update_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_listbox()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[index] = new_task
                self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

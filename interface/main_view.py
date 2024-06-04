# main_view.py

import tkinter as tk
from tkinter import messagebox


class MainView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("To-Do List")
        self._setup_ui()

    def _setup_ui(self):
        frame = tk.Frame(self)
        frame.pack(pady=10)

        self.title_entry = tk.Entry(frame, width=20)
        self.title_entry.pack(side=tk.LEFT, padx=5)

        self.description_entry = tk.Entry(frame, width=30)
        self.description_entry.pack(side=tk.LEFT, padx=5)

        self.date_entry = tk.Entry(frame, width=11)
        self.date_entry.pack(side=tk.LEFT, padx=5)

        add_button = tk.Button(frame, text="Add Task", command=self.controller.add_task)
        add_button.pack(side=tk.LEFT)

        self.task_list = tk.Listbox(self, width=100, height=10)
        self.task_list.pack(pady=10)

        delete_button = tk.Button(self, text="Delete Task", command=self.controller.delete_task)
        delete_button.pack()

    def get_task_details(self):
        return self.title_entry.get(), self.description_entry.get(), self.date_entry.get()

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def get_selected_task_id(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            task_id = self.task_list.get(selected_task).split()[0]
            return task_id
        return None

    def show_warning(self, title, message):
        messagebox.showwarning(title, message)

    def update_task_list(self, tasks):
        self.task_list.delete(0, tk.END)
        for task in tasks:
            task_str = f"{task[0]} - {task[1]} (Due: {task[4]})"
            if task[3]:  # task[3] is the "done" boolean
                task_str += " [DONE]"
            if task[2]:  # task[2] is the "description"
                task_str += f" - {task[2]}"
            self.task_list.insert(tk.END, task_str)


# main_controller.py
from data.db.todo_nexus import ToDoNexus
from interface.main_view import MainView


class MainController:
    def __init__(self):
        self.view = MainView(self)
        self.data = ToDoNexus()
        self.refresh_tasks()

    def run(self):
        self.view.mainloop()

    def add_task(self):
        title, description, due_date = self.view.get_task_details()
        if title and due_date:
            self.data.add(title, description, due_date)
            self.view.clear_entries()
            self.refresh_tasks()
        else:
            self.view.show_warning("Input Error", "Please enter a title and a due date.")

    def delete_task(self):
        task_id = self.view.get_selected_task_id()
        if task_id:
            self.data.delete(task_id)
            self.refresh_tasks()
        else:
            self.view.show_warning("Selection Error", "Please select a task to delete.")

    def refresh_tasks(self):
        tasks = self.data.get_all()
        self.view.update_task_list(tasks)

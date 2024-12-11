class Project:
    def __init__(self, name, description, tasks:list):
        self.name = name
        self.description = description
        self.tasks = tasks

    def add_task(self, title, description, status):
        if status.lower().title() not in ["Planned", "In Progress", "Completed"]:
            print("Incorrect status, try again.")
        else:
            task = {"title": title,
                    "description": description,
                    "status": status}
            self.tasks.append(task)

    def remove_task(self, title):
        for task in self.tasks:
            if task["title"] == title:
                self.tasks.remove(task)

    def get_task_status(self, title):
        for task in self.tasks:
            if task["title"] == title:
                print(f"{task["status"]}")

    def update_task_status(self, title, new_status):
        if new_status not in ["Planned", "In Progress", "Completed"]:
            print("Invalid status, try again.")
        else:
            for task in self.tasks:
                if task["title"] == title:
                    task["status"] = new_status

    def get_tasks_by_status(self, status):
        if status not in ["Planned", "In Progress", "Completed"]:
            print("Invalid status, please try again.")
        else:
            for task in self.tasks:
                if task["status"] == status:
                    print(task)

    def print_tasks(self):
        for task in self.tasks:
            print(f"Task: {task['title']}, Status: {task['status']}")

project = Project("Website Redesign", "A project for redesigning the company website", [])
project.add_task("Design Layout", "Create a layout for the new website", "Planned")
project.add_task("Develop Homepage", "Develop the homepage of the website", "In Progress")

project.update_task_status("Design Layout", "Completed")

project.print_tasks()
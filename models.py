import json
import os

class Task:
    def __init__(self, task_id, name, days, start_time):
        self.task_id = task_id
        self.name = name
        self.days = [day.lower() for day in days]  # Keep day names lowercase
        self.start_time = start_time  # Stored as HH:MM

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "name": self.name,
            "days": self.days,
            "start_time": self.start_time
        }


class ScheduleManager:
    def __init__(self, filepath="data.json"):
        self.filepath = filepath
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filepath):
            return []

        with open(self.filepath, 'r') as f:
            data = json.load(f)

        return [Task(**task_data) for task_data in data]

    def save_tasks(self):
        with open(self.filepath, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self, name, days, start_time):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, name, days, start_time)
        self.tasks.append(new_task)
        self.save_tasks()
        return new_task

    def delete_task(self, task_id):
        if not any(task.task_id == task_id for task in self.tasks):
            return False

        self.tasks = [t for t in self.tasks if t.task_id != task_id]

        # Give the remaining tasks new IDs
        for new_task_id, task in enumerate(self.tasks, start=1):
            task.task_id = new_task_id

        self.save_tasks()
        return True

    def edit_task(self, task_id, new_name, new_days, new_time):
        for task in self.tasks:
            if task.task_id == task_id:
                task.name = new_name
                task.days = [day.lower() for day in new_days]
                task.start_time = new_time
                self.save_tasks()
                return True

        return False


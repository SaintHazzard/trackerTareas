from models.task_model import Task, create_task, get_all_tasks, update_task, delete_task
from models.database import SessionLocal

class TaskController:
    """Controlador de tareas. Provee la lógica entre vista y modelo."""
    def __init__(self):
        self.db = SessionLocal()

    def add_task(self, title, description,completed = False):
        if title.strip():
            create_task(title=title.strip(), description=description.strip(), completed=completed)
            return True
        return False

    def get_tasks(self):
        return get_all_tasks()

    def set_task_completed(self, task_id, completed):
        update_task(task_id, completed=completed)

    def remove_task(self, task_id):
        delete_task(task_id)

    def get_task_completed(self, task_id):
        task = self.get_task_by_id(task_id)
        return task.completed if task else None

    def get_task_by_id(self, task_id):
        return self.db.query(Task).filter(Task.id == task_id).first()





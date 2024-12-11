from models.task_model import Task, create_task, get_all_tasks, update_task, delete_task
from models.database import SessionLocal

class TaskController:
    """Controlador de tareas. Provee la lógica entre vista y modelo."""
    def __init__(self):
        self.db = SessionLocal()

    def add_task(self, text):
        if text.strip():
            create_task(text.strip(), completed=False)
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
        print(task_id)
        return self.get_or_none(Task.id == task_id)

    def get_or_none(self, model, **kwargs):
        try:
            query = self.db.query(model).filter(*[getattr(model, key) == value for key, value in kwargs.items()])
            compiled_query = query.statement.compile(dialect=self.db.bind.dialect)
            print("Consulta generada:", compiled_query)
            print("Parámetros:", compiled_query.params)
            return query.one_or_none()
        except Exception as e:
            print("Error al ejecutar la consulta:", e)
            raise




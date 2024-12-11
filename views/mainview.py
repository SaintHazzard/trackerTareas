from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from controllers.task_controller import TaskController
from views.tasklistitem import TaskListItem
import json


class MainView(BoxLayout):
    input_task = ObjectProperty(None)
    input_description = ObjectProperty(None)
    rv = ObjectProperty(None)

    def __init__(self, **kwargs):
        self.controller = TaskController()
        super().__init__(**kwargs)
        print(self.ids)


    def on_kv_post(self, base_widget):
        self.populate_tasks(None)

    def populate_tasks(self, dt):
        tasks = self.controller.get_tasks()
        self.rv.data = [
            {
                'task_id': t.id,
                'title': t.title,
                'description': t.description,
                'completed': t.completed
            } for t in tasks
        ]
        # self.rv.refresh_from_data()

    def add_task(self):
        title = self.input_task.text
        description = self.input_description.text
        if self.controller.add_task(title, description):
            self.input_task.text = ''
            self.input_description.text = ''
            self.populate_tasks(0)

    def add_task_imported(self, title, description, completed):
        if self.controller.add_task(title, description,completed):
            self.populate_tasks(0)

    def on_task_completed(self, task_id, completed):
        
        print(f'{task_id} {completed} funcion on task completed')
        current_state = self.controller.get_task_completed(task_id)
        if current_state != completed:
            self.controller.set_task_completed(task_id, completed)
            self.populate_tasks(0)
            self.rv.refresh_from_data()

    def on_task_deleted(self, task_id):
        self.controller.remove_task(task_id)
        self.populate_tasks(0)

    def import_data(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                self.rv.data = data
                for task in data:
                    self.add_task_imported(task['title'], task['description'], task['completed'])
                print("Datos importados correctamente.")
        except Exception as e:
            print(f"Error al importar datos: {e}")

    def export_data(self):
        try:
            with open('data.json', 'w') as f:
                json.dump(self.rv.data, f)
                print("Datos exportados correctamente.")
        except Exception as e:
            print(f"Error al exportar datos: {e}")

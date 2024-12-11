from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from controllers.task_controller import TaskController
from views.tasklistitem import TaskListItem


class MainView(BoxLayout):
    input_task = ObjectProperty(None)
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
                'text': t.text,
                'completed': t.completed
            } for t in tasks
        ]

    def add_task(self):
        text = self.input_task.text
        if self.controller.add_task(text):
            self.input_task.text = ""
            self.populate_tasks(0)

    def on_task_completed(self, task_id, completed):
        
        print(f'{task_id} {completed}')
        current_state = self.controller.get_task_completed(task_id)
        if current_state != completed:
            self.controller.set_task_completed(task_id, completed)
            self.populate_tasks(0)

    def on_task_deleted(self, task_id):
        self.controller.remove_task(task_id)
        self.populate_tasks(0)

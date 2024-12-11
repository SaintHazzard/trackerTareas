from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivy.app import App
from views.customwidgets import HoverButton

class TaskListItem(BoxLayout):
    task_id = NumericProperty(0)
    title = StringProperty('')
    description = StringProperty('')
    completed = BooleanProperty(False)

    def handle_checkbox(self, is_active):
        print(f'{self.task_id} {is_active} funcion handle checkbox')
        if self.completed != is_active:
            self.completed = is_active
            app = App.get_running_app()
            app.root.on_task_completed(self.task_id, is_active)

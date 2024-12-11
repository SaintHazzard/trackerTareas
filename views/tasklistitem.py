from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty, NumericProperty

class TaskListItem(BoxLayout):
    task_id = NumericProperty(0)
    title = StringProperty('')
    description = StringProperty('')
    completed = BooleanProperty(False)

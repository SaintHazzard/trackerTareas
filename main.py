from kivy.lang import Builder
# Primero carga tasklistitem.kv
Builder.load_file('views/tasklistitem.kv')
# Luego mainview.kv
Builder.load_file('views/mainview.kv')

from kivy.app import App
from views.mainview import MainView

class TaskManagerApp(App):
    def build(self):
        return MainView()

if __name__ == '__main__':
    TaskManagerApp().run()

from kivy.core.window import Window
from kivy.modules import inspector
from kivy.base import EventLoop
from kivy.utils import platform


if platform != 'android':
    EventLoop.ensure_window()
    inspector.create_inspector(Window, EventLoop)

from kivy.lang import Builder


Builder.load_file('views/tasklistitem.kv')
Builder.load_file('views/mainview.kv')

from kivy.app import App
from views.mainview import MainView



class TaskManagerApp(App):
    def build(self):
        return MainView()

if __name__ == '__main__':
    TaskManagerApp().run()

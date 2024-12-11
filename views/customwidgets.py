from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import BooleanProperty

class HoverBehavior(object):
    hovering = BooleanProperty(False)
    normal_text_color = ListProperty([0, 0, 0, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        self.color = self.normal_text_color

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovering != inside:
            self.hovering = inside
            if inside:
                self.dispatch('on_enter')
            else:
                self.dispatch('on_leave')

class HoverButton(Button, HoverBehavior):
    hover_color = ListProperty([1, 0, 0, 1])  # Rojo
    normal_color = ListProperty([0.3, 0.6, 0.3, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = self.normal_color

    def on_enter(self):
        """Evento al pasar el mouse sobre el botón."""
        self.background_color = self.hover_color

    def on_leave(self):
        """Evento al salir el mouse del botón."""
        self.background_color = self.normal_color

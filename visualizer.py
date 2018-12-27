from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.vector import Vector
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.graphics.texture import Texture


class VisLayout(BoxLayout):

    def __init__(self):
        super().__init__()
        width = 1
        height = 512

        texture = Texture.create(size=(width, height))

        # create 64x64 rgb tab, and fill with values from 0 to 255
        # we'll have a gradient from black to white
        size = width * height * 3
        # buf = [int(x * 255 / size) for x in range(size)]
        buf = []
        for i in range(height):
            buf.extend([int(i * 255 / height)] * 3 * width)
        print(buf)
        buf = ''.join(map(chr, buf))
        print(buf)
        texture.blit_buffer(buf.encode(), colorfmt='rgb', bufferfmt='ubyte')
        with self.canvas.before:
            print('in canvas')
            self.background = Rectangle(texture=texture, pos=self.pos, size=(self.width, self.height))
        self.bind(pos=self.update_background,
                  size=self.update_background)

    def update_background(self, *args):
        print('args: ', args)
        # gives widget and size?
        self.background.pos = self.pos
        self.background.size = self.size

    def on_touch_down(self, touch):
        print(touch.x, touch.y)
        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))


class VisualizerApp(App):
    def build(self):
        main_layout = VisLayout()
        # print(main_layout.width, main_layout.height)
        # main_layout.size_hint = (0, 0)
        return main_layout


if __name__ == '__main__':
    VisualizerApp().run()

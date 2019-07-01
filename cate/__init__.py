from collections import defaultdict
from time import time as get_time
import os.path
import pathlib

from pynegin.components import text, component, line
from pynegin.constants.colors import COLORS
from pynegin.gameLogic import GameLogic
import pygame

from .keys import Keys

import pynegin


class Canvas(component.Component):
    def __init__(self, container, size, color):
        self.color = color
        surface = pygame.Surface(size)
        surface.fill(color)
        super().__init__(container, surface=surface)

        self.components = {}
        self.components['text'] = text.Text(self, color=COLORS.BLACK, textSize=40)

    def show(self, surf):
        self.surface.fill(self.color)
        for comp in self.components.values():
            comp.show(self.surface)
        if self.isVisible:
            surf.blit(self.surface, self.rect)

    def set_text(self, text):
        self.components['text'].setText(text)

    def add_component(self, component, alias):
        self.components[alias] = component



class Cate(GameLogic):
    """Wrapper class for pynegin"""
    def __init__(self, window_size=(800,600), window_title="Cate", window_color=(255, 255, 255), showing_axis=True):
        icon_path = str(pathlib.Path(os.path.dirname(__file__)).joinpath("assets/icon.png"))

        self.window = pynegin.Window(window_size, window_title, backgroundColor=window_color, customIconPath=icon_path)
        self.engine = pynegin.Engine(self, self.window)
        self.context = Canvas(self.window, window_size, window_color)
        self.context.center()
        self._startupFunctions = []
        self._on_keys = defaultdict(list)
        self._on_keys_down = defaultdict(list)
        self._draw_axis(showing_axis)


    # Override
    def input(self):
        for key, val in self._on_keys.items():
            if self.window.isKeyPressed(key):
                for f in val:
                    f()

        for key, val in self._on_keys_down.items():
            if self.window.isKeyDown(key):
                for f in val:
                    f()


    def on_start(self, f):
        self._startupFunctions.append(f)


    def start(self):
        for f in self._startupFunctions:
            f()

        self.engine.run()


    def pause(self, to_wait):
        # Make sure latest updates are visible before the sleep
        self.render()

        previous = get_time()

        while to_wait > 0:
            self.window.update() # Pump events so it does not hang
            now = get_time()
            delta = now - previous
            to_wait -= delta
            previous = now


    def exit(self):
        self.window.quit()


    def on_key(self, key):
        def f(func):
            self._on_keys[key].append(func)
        return f


    def on_key_down(self, key):
        def f(func):
            self._on_keys_down[key].append(func)
        return f


    def say(self, msg):
        self.context.set_text(str(msg))


    def show_axis(self, e):
        self.context.components['y_axis'].setVisible(e)
        self.context.components['x_axis'].setVisible(e)


    def toggle_axis(self):
        e = not self.context.components['y_axis'].isVisible
        self.context.components['y_axis'].setVisible(e)
        self.context.components['x_axis'].setVisible(e)


    def wait_for(self, *keys):
        self.render() # Make sure latest changes are visible
        pressed_keys = self.window.getPressedKeys()

        while True:
            self.window.update() # Listen for new keys/prevent hanging
            for key in keys:
                if self.window.isKeyPressed(key):
                    return key


    def _draw_axis(self, visible):
        if self.show_axis:
            v_line = line.Line(self.context, (0,0), (0,self.context.getHeight()), 3, COLORS.BLACK, isVisible=visible)
            h_line = line.Line(self.context, (0,0), (self.context.getWidth(),0), 3, COLORS.BLACK, isVisible=visible)
            v_line.centerHorizontal()
            h_line.centerVertical()
            self.context.add_component(v_line, "y_axis")
            self.context.add_component(h_line, "x_axis")



cate = Cate(window_size=(600,600))

def on_start(f):
    cate.on_start(f)

def on_key(key):
    return cate.on_key(key)

def on_key_down(key):
    return cate.on_key_down(key)

def say(msg):
    cate.say(msg)

def start():
    cate.start()

def pause(time):
    cate.pause(time)

def exit():
    cate.exit()

def wait_for(*keys):
    return cate.wait_for(*keys)

def show_axis(e):
    cate.show_axis(e)

def toggle_axis():
    cate.toggle_axis()

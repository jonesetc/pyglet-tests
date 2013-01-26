import pyglet
from pyglet.window import key, mouse

window = pyglet.window.Window()

@window.event
def on_key_press(symbol, modifiers):
    print '%s %r' % (symbol, modifiers)

@window.event
def on_draw():
    window.clear()

pyglet.app.run()

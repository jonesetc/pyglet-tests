import pyglet
from pyglet.window import key, mouse

window = pyglet.window.Window()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        pyglet.graphics.draw(4, pyglet.gl.GL_POLYGON,
                ('v2i',(x, y, x, y+50, x+50, y+50, x+50, y)))
    else:
        window.clear()

pyglet.app.run()

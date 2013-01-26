from random import random

import pyglet
from pyglet.window import key, mouse

class square(object):
    def __init__(self, size, initial, xVel, yVel):
        self.size = size
        self.pos = initial
        self.xVel = xVel
        self.yVel = yVel

    def update(self):
        self.pos = (self.pos[0]+self.xVel, self.pos[1]+self.yVel)

    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_POLYGON,
                ('v2f',(self.pos[0]-self.size, self.pos[1]+self.size, self.pos[0]+self.size, self.pos[1]+self.size,
                    self.pos[0]+self.size, self.pos[1]-self.size, self.pos[0]-self.size, self.pos[1]-self.size)))
        self.update()
        
shapes = []
for _ in xrange(25):
    shapes.append(square(25, (random()*500, random()*500), 0, random()*-10))
window = pyglet.window.Window()

@window.event
def on_draw():
    window.clear()
    for s in shapes:
        s.draw()

pyglet.app.run()

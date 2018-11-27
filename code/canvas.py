import pyglet
from pyglet.gl import *

class Triangle:
    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list(3, ('v3f', [-0.5,-0.5,0.0, 0.5,-0.5, 0.0, 0.0, 0.5, 0.0]),
                                                    ('c3B', [100,200,220, 200, 110, 100, 100,250,100]))
class Quad:
    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list_indexed(4, [0,1,2, 3], 
                                                            ('v3f', [-0.5,-0.5,0.0, 0.5,-0.5, 0.0, 0.5, 0.5, 0.0, -0.5,0.5,0.0]))

class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(400,300)
        glClearColor(0.2, 0.3, 0.2, 1.0)
        self.triangle = Triangle()
        self.quad = Quad()
        
    def on_draw(self):
        self.clear()
        self.quad.vertices.draw(GL_QUADS)
    
    def on_resize(self, width, height):
        pyglet.gl.glViewport(0, 0, width, height)
        
if __name__ == "__main__":
    window = MyWindow(1280,720, "My window", resizable = True)
    pyglet.app.run()
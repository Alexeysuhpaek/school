from ctypes import sizeof
import turtle
screen= turtle.getscreen()
t = turtle.Turtle(shape="turtle")
class DrawShape:
    def draw(self,color='red'):
        if self.fill:
            t.color(color)
            t.begin_fill()
        for _ in range(self.sides):
            t.forward(self.size)
            t.left(self.angle)
        if self.fill:
            t.end_fill()
class Rect(DrawShape):
    def __init__(self,size, fill) -> None:
        self.size = size
        self.sides = 4
        self.angle = 90
        self.fill = fill
    def __str__(self) -> str:
        return 'kmujngtrfefrvr'
a =  Rect(50,True)
print(a)
a.draw('purple')
screen.mainloop()

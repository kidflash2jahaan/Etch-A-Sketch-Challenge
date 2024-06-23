from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def w():
    turtle.forward(5)


def s():
    turtle.back(5)


def a():
    turtle.left(10)


def d():
    turtle.right(10)


screen.listen()

screen.onkeypress(w, "w")
screen.onkeypress(s, "s")
screen.onkeypress(a, "a")
screen.onkeypress(d, "d")

screen.mainloop()

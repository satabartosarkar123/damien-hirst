from turtle import Turtle,Screen
import turtle
from random import choice as c
import color_extractor as ce


colors=["red", "orange", "yellow", "green", "blue", "indigo", "violet","cyan","magenta"]
def all_gons():
    t=Turtle(shape="turtle")
    global colors
    t.colormode(cmode=None)
    for i in range(3,11):
        t.color(colors[i-3])
        t.setheading(0)
        for j in range(i):
            t.right(360/i)
            t.forward(100)


def random_wals():
    t=Turtle(shape="turtle")
    turtle.colormode(cmode=255)
    global colors
    t.pensize(10)
    t.speed(0)
    for i in range(5000):
        t.color(c(range(0,256)),c(range(0,256)),c(range(0,256)))
        t.forward(50)
        t.right(c([0,90,180,270]))


def spirograph():
    t=Turtle(shape="turtle")
    turtle.colormode(cmode=255)
    t.speed(0)
    for i in range(100):
        t.color(c(range(0,256)),c(range(0,256)),c(range(0,256)))
        t.circle(100)
        t.setheading(t.heading()+360/100)


def damien_hirtz(image:str, n:int):
    t=Turtle(shape="turtle")
    turtle.colormode(cmode=255)
    t.speed(0)
    t.teleport(-200,-200)
    colors=ce.extract_colors(image, n)
    colors.sort()  # Sort colors by red value
    for i in range(10):
        for j in range(10):
            t.color(tuple(c(colors)))
            t.dot(20)
            t.teleport(t.xcor()+50,t.ycor())
        t.teleport(-200, t.ycor()+50)




damien_hirtz(input("Enter the image file name (e.g., 'img.jpg'): "), int(input("Enter the number of colors to extract: ")))
s=Screen()
s.exitonclick()
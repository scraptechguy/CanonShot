import turtle

vx0 = int(input("Enter velocity 1: "))
vy0 = int(input("Enter velocity 2: "))



sc = turtle.Screen()
sc.bgcolor("black")
sc.setup(width= 1280, height= 720)
sc.tracer(0)

txt = turtle.Turtle()
txt.speed(0)
txt.color("red")
txt.penup()
txt.hideturtle()

sq = turtle.Turtle()
sq.speed(0)
sq.shape("square")
sq.color("white")


pen1 = turtle.Turtle()
pen1.color("white")
pen1.hideturtle()

pen2 = turtle.Turtle()
pen2.color("white")
pen2.hideturtle()


for i in range(15):
    pen1.forward(700)
    pen1.right(180)
    pen1.forward(700)
    pen1.right(90)
    pen1.forward(25)
    pen1.right(90)


pen2.left(90)

for i in range(29):
    pen2.forward(350)
    pen2.left(180)
    pen2.forward(350)
    pen2.left(90)
    pen2.forward(25)
    pen2.left(90)

t = " "
x0 = 0
y0 = 0
g = 9.8
n = 1000

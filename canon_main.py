import turtle

# Input of two vector velocities 
vx0 = int(input("Enter vx0: "))
vy0 = int(input("Enter vy0: "))


# Screen parameters
sc = turtle.Screen()
sc.bgcolor("black")
sc.setup(width= 1280, height= 720)
sc.tracer(0)

# Text-writing pens

# y coordinates 
txty = turtle.Turtle()
txty.speed(0)
txty.color("white")
txty.penup()
txty.hideturtle()

# x coordinates
txtx = turtle.Turtle()
txtx.speed(0)
txtx.color("white")
txtx.penup()
txtx.hideturtle()

# x and y coordinates on the left 
txt = turtle.Turtle()
txt.speed(0)
txt.color("white")
txt.penup()
txt.hideturtle()

# Square representing cannon ball
sq = turtle.Turtle()
sq.speed(0)
sq.shape("square")
sq.color("white")

# Squeare representing hight
sqy = turtle.Turtle()
sqy.speed(0)
sqy.shape("square")
sqy.color("red")
sqy.shapesize(0.3, 0.3)
sqy.penup()

# Square representing length
sqx = turtle.Turtle()
sqx.speed(0)
sqx.shape("square")
sqx.color("red")
sqx.shapesize(0.3, 0.3)
sqx.penup()



# Grid-writing pens

# Horizontal
peny = turtle.Turtle()
peny.color("white")
peny.hideturtle()

# Vertical
penx = turtle.Turtle()
penx.color("white")
penx.hideturtle()


# Horizontal grid
for i in range(15):
    peny.forward(700)
    peny.right(180)
    peny.forward(700)
    peny.right(90)
    peny.forward(25)
    peny.right(90)

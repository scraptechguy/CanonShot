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

    

# Vertical grid
penx.left(90)

for i in range(29):
    penx.forward(350)
    penx.left(180)
    penx.forward(350)
    penx.left(90)
    penx.forward(25)
    penx.left(90)

grid_y = 25

txty.right(180)
txty.forward(30)
txty.right(90)

# Horizontal grid
for i in range(14):
    txty.forward(25)
    txty.write(
        grid_y,
        font=("Courier", 10)
    )
    grid_y += 25

grid_x = 25

txtx.right(90)
txtx.forward(20)
txtx.left(90)

for i in range(28):
    txtx.forward(25)
    txtx.write(
        grid_x,
        font=("Courier", 7)
    )
    grid_x += 25

    # Placing coordinates on screen
txt.goto(-600, 250)

# Defining varuables used in the equations below
t = " "
# Distance from position 0, 0
x0 = 0
# Height above the ground 
y0 = 0
# Gravitional acceleration 
g = 9.8
# In range of ... variable
n = 100000

# For loop for displaying flight
for i in range(n):
    # updating time in each cycle 
    t = float(i)/n * 1000
    # Equations of motion of a body in a gravitational field
    iks = x0 + vx0 * t 
    ypsilon = y0 + vy0 * t - 0.5 * g * t * t

    # Movement of the cannon ball
    sq.goto(iks, ypsilon)

    sqy.goto(0, sq.ycor())
    sqx.goto(sq.xcor(), 0)

    # Displaying x and y coordinates 
    txt.clear()
    txt.write(
        "Distance: {}     \nHeight: {}      ".format(sq.xcor(), sq.ycor()),
        font=("Courier", 20, "normal")
    )

    # Stopping the cycle when the ball hit the ground 
    if sq.ycor() < 0:
        break

    # Refreshing the screen
    sc.update()

# Keeping the screen going 
while True:
    sc.update()

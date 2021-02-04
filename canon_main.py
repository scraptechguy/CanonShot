import turtle

# Input of two vector velocities 
vx0 = int(input("Enter vx0: "))
vy0 = int(input("Enter vy0: "))


# Screen parameters
sc = turtle.Screen()
sc.bgcolor("black")
sc.setup(width= 1280, height= 720)
sc.tracer(0)

# Text-writing pen
txt = turtle.Turtle()
txt.speed(0)
txt.color("red")
txt.penup()
txt.hideturtle()

# Square representing cannon ball
sq = turtle.Turtle()
sq.speed(0)
sq.shape("square")
sq.color("white")


# Grid-writing pens

# Horizontal
pen1 = turtle.Turtle()
pen1.color("white")
pen1.hideturtle()

# Vertical
pen2 = turtle.Turtle()
pen2.color("white")
pen2.hideturtle()


# Horizontal grid
for i in range(15):
    pen1.forward(700)
    pen1.right(180)
    pen1.forward(700)
    pen1.right(90)
    pen1.forward(25)
    pen1.right(90)


# Vertical grid
pen2.left(90)

for i in range(29):
    pen2.forward(350)
    pen2.left(180)
    pen2.forward(350)
    pen2.left(90)
    pen2.forward(25)
    pen2.left(90)

# Defining varuables used in the equations below
t = " "
# Distance from position 0, 0
x0 = 0
# Height above the ground 
y0 = 0
# Gravitional acceleration 
g = 9.8
# In range of ... variable
n = 10000

# For loop for displaying flight
for i in range(n):
    # updating time in each cycle 
    t = float(i)/n * 100
    # Equations of motion of a body in a gravitational field
    iks = x0 + vx0 * t 
    ypsilon = y0 + vy0 * t - 0.5 * g * t * t

    # Movement of the cannon ball
    sq.goto(iks, ypsilon)
    # Refreshing the screen
    sc.update()

    # Displaying x and y coordinates 
    print(iks)
    print(ypsilon)

    # Stopping the cycle when the ball hit the ground 
    if sq.ycor() < 0:
        break

# Keeping the screen going 
while True:
    sc.update()

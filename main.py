# library turtle is used for graphics 

import turtle


# while loop to secure right inputs. Inputs have to be integers, if they're not, user is asked to input different value

while True:

    
    # two verctor velocities get declared and are assigned values by the user
    
    vx0 = input("Enter vx0: ")
    vy0 = input("Enter vy0: ")

    try:
        vx0 = int(vx0)
        break
        
    except ValueError:
        pass

    try:
        vy0 = int(vy0)
        break
        
    except ValueError:
        pass

vx0 = int(vx0)
vy0 = int(vy0)
    

# parameters of the main screen

sc = turtle.Screen()
sc.bgcolor("black")
sc.setup(width= 1280, height= 720)
sc.tracer(0)


# text-writing pens that write x and y coordinates 

txty = turtle.Turtle()
txty.speed(0)
txty.color("white")
txty.penup()
txty.hideturtle()

txtx = turtle.Turtle()
txtx.speed(0)
txtx.color("white")
txtx.penup()
txtx.hideturtle()


# text-writing pen that notes coordinates on the left 

txt = turtle.Turtle()
txt.speed(0)
txt.color("white")
txt.penup()
txt.hideturtle()


# objects representing the cannon ball

sq = turtle.Turtle()
sq.speed(0)
sq.shape("square")
sq.color("white")


# red squeare that represents hight on y axes

sqy = turtle.Turtle()
sqy.speed(0)
sqy.shape("square")
sqy.color("red")
sqy.shapesize(0.3, 0.3)
sqy.penup()


# red square that represents length on x axes

sqx = turtle.Turtle()
sqx.speed(0)
sqx.shape("square")
sqx.color("red")
sqx.shapesize(0.3, 0.3)
sqx.penup()


# pens that draw horizontal and verticals parts of the grid

peny = turtle.Turtle()
peny.color("white")
peny.hideturtle()

penx = turtle.Turtle()
penx.color("white")
penx.hideturtle()


# for loop used to draw horizontal (y axes) of the grid

for i in range(15):
    peny.forward(700)
    peny.right(180)
    peny.forward(700)
    peny.right(90)
    peny.forward(25)
    peny.right(90)


# for loop used to draw vertical (x axes) of the grid 
# (penx.left(90) because turtle's forward is up ^ by default)

penx.left(90)

for i in range(29):
    penx.forward(350)
    penx.left(180)
    penx.forward(350)
    penx.left(90)
    penx.forward(25)
    penx.left(90)


# for loop that writes y values next to the grid. One square is equal to 25 meters (pixels)
# texty is moved to start at the right spot
    
grid_y = 25

txty.right(180)
txty.forward(30)
txty.right(90)

for i in range(14):
    txty.forward(25)
    txty.write(
        grid_y,
        font=("Courier", 10)
    )
    grid_y += 25

    
# for loop that writes x values next to the grid. One square is also equal to 25 meters (pixels)  
  
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

# Placing coordinates
txt.goto(-600, 250)

# Defining variables used in the equations below
t = " "
# Distance from position 0, 0
x0 = 0
# Height above the ground 
y0 = 0
# Gravitional acceleration 
g = 9.8
# In range of ... variable
n = 100000

# Definition of list that stores every achieved height (can't be in the loop, would overwrite itself)
list_of_heights = []

# For loop for displaying flight
for i in range(n):
    # updating time in each cycle 
    t = float(i)/n * 1000
    # Equations of motion of a body in a gravitational field
    iks = x0 + vx0 * t 
    ypsilon = y0 + vy0 * t - 0.5 * g * t * t

    # Movement of the cannon ball
    sq.goto(iks, ypsilon)


    #movement of red indicator squares
    sqy.goto(0, sq.ycor())
    sqx.goto(sq.xcor(), 0)


    # appending every achieved height to one list and then searching for the highest number (highest altitude)
    height = sq.ycor()
    list_of_heights.append(height)
    top_height = int(max(list_of_heights))


    # Displaying x and y coordinates 
    txt.clear()
    txt.write(
        "Distance: {} meters\nHeight: {} meters\n\nTop height: {} meters".format(int(sq.xcor()), int(sq.ycor()), top_height),
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

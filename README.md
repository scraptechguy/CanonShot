# This program simulates flight of a cannonball shot

+ To run this yourself, review <a href="https://github.com/scraptechguy/CanonShot/blob/main/requirements.md" target="_blank">requirements.md</a> file and do the following in terminal: 

```sh
cd <path of the project on your computer>
```

And then:

```sh
pip install -r requirements.txt
python main.py
```

### Table of contents

+ <a href="https://github.com/scraptechguy/CanonShot#how-does-it-work">How does it work?</a>
+ <a href="https://github.com/scraptechguy/CanonShot#understand-whats-on-the-screen">Understand what's on the screen</a>
+ <a href="https://github.com/scraptechguy/CanonShot#understand-the-code">Understand the code</a>

## How does it work?

User inputs two vector velocities (in m/s), vertical (y) and horizontal (x). These two vectors get added together following the laws of <a href="https://www.physicsclassroom.com/Class/vectors/U3L1b.cfm" target="_blank">vector addition</a>. 



<img src="https://user-images.githubusercontent.com/75474651/139541508-45e718ff-3df5-4c71-a7cb-4b730dd8ec7d.jpg" width="500">



The cannon ball moves accordingly to the resulting vector velocity. Simulation is NOT in real time though distances traveled (upward and forward) are accurate. One pixel on screen represents one meter in real life -> instant coordinates of the cannon ball are coordinates the ball would have in the real world ([100; 150] -> the cannon ball is 100 meters above the ground and 150 meters far from the point from which it was shot)

+ Note: Air resistance is NOT added (yet, still on it!) thus distances are accurate to the point when air is added 


## Understand what's on the screen

We're shooting from point with coordinates [0: 0]. White square (the cannon ball) flies from that point to the right. One square on the grid has dimensions 25 x 25 pixels (meters). In the left top corner is information about the position of the cannon ball (distance, height, and top height). Small red squares represent the movement of the cannon ball on the according axes. 


## Understand the code

Program is written in Python 3.10 using <a href="https://pypi.org/project/PythonTurtle/" target="_blank">Python Turtle</a> library. 

### Code structure with snippets of code

+ User input of two vector velocities; vx0 and vy0

```py
    vx0 = input("Enter vx0: ")
    vy0 = input("Enter vy0: ")
```

+ Definition of all the objects on the screen (screen included)

```py
    sc = turtle.Screen()
    sc.bgcolor("black")
    sc.setup(width= 1280, height= 720)
    sc.tracer(0)
```

+ Drawing the grid with axis numbers 

```py
    for i in range(15):
        peny.forward(700)
        peny.right(180)
        peny.forward(700)
        peny.right(90)
        peny.forward(25)
        peny.right(90)
```

+ For loop where the cannon ball coordinates and everything else gets updated. This while loop has break when y coordinate of the cannon ball is smaller than 0

```py
    for i in range(n):
```

+ Using equations for flight in a gravitational field to make the cannon ball move accordingly

```py
        iks = x0 + vx0 * t 
        ypsilon = y0 + vy0 * t - 0.5 * g * t * t

        sq.goto(iks, ypsilon)

        sc.update()
```

+ While loop to keeep the screen going after the first while loop finishes (cannon ball hits the ground) 

```py
    while True:

        sc.update()
```

And that's it! 

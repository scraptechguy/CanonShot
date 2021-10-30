## This program simulates the flight of a cannonball shot.

## How does it work?

User inputs two vector velocities, vertical (y) and horizontal (x). These two vectors get added together following the laws of vector addition. The cannon ball moves accordingly to the resulting vector velocity. Simulation is NOT in real time though distances traveled (upward and forward) are accurate. One pixel on screen represents one meter in real life -> instant coordinates of the cannon ball are coordinates the ball would have in the real world ([100; 150] -> the cannon ball is 100 meters above the ground and 150 meters far from the point from which it was shot)

## Understand what's on the screen

of which are pointing straight vertical and horizontal x, y; vx0 vector is pointing straight along the x-axis and vy0 vector straight along the y-axis. The combination of two and time updating overtime is resulting in a pretty accurate trajectory estimate.

Small red squares represent the movement of the cannonball on a certain axis. 
Air resistance is not included (yet, still on it!), one pixel is equal to one meter in real life, velocities are in meters per second.

Program should run after pasting to any code editor (i.e. VS Code, Sublime text, etc.) with Python 3 installed on your computer. Formating issues may appear when pasting directly to a terminal.

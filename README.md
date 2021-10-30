# This program simulates the flight of a cannonball shot

+ To run this yourself, review <a href="https://github.com/scraptechguy/CanonShot/blob/main/requirements.md" target="_blank">requirements.md</a> file

## How does it work?

User inputs two vector velocities (in m/s), vertical (y) and horizontal (x). These two vectors get added together following the laws of vector addition. The cannon ball moves accordingly to the resulting vector velocity. Simulation is NOT in real time though distances traveled (upward and forward) are accurate. One pixel on screen represents one meter in real life -> instant coordinates of the cannon ball are coordinates the ball would have in the real world ([100; 150] -> the cannon ball is 100 meters above the ground and 150 meters far from the point from which it was shot)

+ Note: Air resistance is NOT added (yet, still on it!) thus distances are accurate to the point when air is added 

## Understand what's on the screen

We're shooting from point with coordinates [0: 0]. White square (the cannon ball) flies from that point to the right. One square on the grid has dimensions 25 x 25 pixels (meters). In the left top corner is information about the position of the cannon ball (distance, height, and top height). Small red squares represent the movement of the cannon ball on each axes. 



# ROAD RAGE

Simulates traffic along a road to determine the optimal speed for that road to avoid jams and collisions.

To view graphs, install from requirements.txt and run jupyter notebook.

This is done through 3 classes:

## ROAD

-Holds the length of the road and a method to loop cars back to the beginning of the simulated road.

## CAR

-Holds everything that car needs to know: position, speed, max speed, it's size, and an ID number (for later use)
-Cars handle moving themselves, changing their speed, checking for collisions, and checking if they need to be sent to the beginning of the simulation

## SIM

-Creates a list of cars
-Updates each car's position through the list
-Gathers data


## MAIN

-Tells the sim how many times to run and with what input for the max speeds.
-Collects the data from each run to create graphs and calculate the best speed limit.

# =================================================================================
# MODULE IMPORTS (Packages)
# These lines import necessary external libraries, often called 'modules' or 'packages'.
# They provide extra functionality that we can use in our program.
# =================================================================================
import random # This module is used to generate random numbers and choices. 
              # It is essential for making our points 'walk' randomly.
import time   # This module provides functions for dealing with time, 
              # most notably 'sleep', which pauses the execution of the program 
              # for a specified number of seconds to control the animation speed.
import os     # This module provides a way to interact with the operating system. 
              # We use 'os.system('cls')' or 'os.system('clear')' to clear the 
              # console screen between frames, creating the illusion of movement.

# Define the possible steps a Point can take in one direction (x or y).
# -1: move left/up
# 0: stay put
# 1: move right/down
possibilities = [-1, 0, 1]

# =================================================================================
# CLASS: Point (The Object)
# A Class is a blueprint for creating objects. The Point class defines the data 
# (attributes) and behavior (methods/functions) of a single moving entity.
# =================================================================================
class Point:
    # --- Constructor Method: __init__ ---
    # This method is called automatically when a new Point object is created (instantiated).
    # It sets up the initial state of the object.
    def __init__(self, x, y, marker="*"):
        # Private Attributes (Data Encapsulation)
        # We use '__' (double underscore) before the attribute name (e.g., __x) 
        # to signal that these attributes are intended to be 'private'. 
        # This is a convention in Python, meaning they should only be modified 
        # using the defined methods (getters/setters), not directly.
        self.__x = x
        self.__y = y
        # Public attribute for the character used to represent the Point on the grid.
        self.marker = marker

    # --- Getter Methods (Access Modifiers) ---
    # Getters allow controlled reading of private attributes.
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    # --- Setter Methods (Access Modifiers) ---
    # Setters allow controlled writing (modification) of private attributes.
    def set_x(self, value):
        self.__x = value

    def set_y(self, value):
        self.__y = value

    # --- Method: move ---
    # Defines the behavior for changing the Point's position.
    # dx and dy are the change in x and y coordinates, respectively.
    # width and height represent the boundaries of the grid.
    def move(self, dx=0, dy=0, width=-1, height=-1): 
        # Calculate the potential new coordinates.
        new_x = self.get_x() + dx
        new_y = self.get_y() + dy
        
        # Check if boundary limits (width and height) were NOT provided (i.e., -1).
        if width == -1 and height == -1:
            # If no grid boundaries are given, the point moves freely (no constraints).
            self.set_x(new_x)
            self.set_y(new_y)
            return
        
        # --- Boundary Checking (Collision/Wall Logic) ---
        # If boundaries ARE provided, check if the new position is within the grid.
        # This logic ensures the point wraps or stops at the edges.
        
        # Check X-axis boundaries:
        if new_x >= width:
            new_x = width - 1 # Stop at the right edge
        if new_x < 0:
            new_x = 0         # Stop at the left edge
            
        # Check Y-axis boundaries:
        if new_y >= height:
            new_y = height - 1 # Stop at the bottom edge
        if new_y < 0:
            new_y = 0          # Stop at the top edge
            
        # Update the private attributes using the setter methods.
        self.set_x(new_x)
        self.set_y(new_y)

    # --- Method: move_random_step ---
    # Moves the point randomly within the boundaries of the grid.
    # NOTE ON DESIGN: We pass 'width' and 'height' from the Grid here.
    # This design AVOIDS CIRCULAR REFERENCES. The Point object does not need 
    # to know the Grid object itself; it only needs the dimensions (width, height)
    # to perform its boundary checks. This keeps the two classes cleanly separated.
    def move_random_step(self, width, height):
        # Randomly choose a movement step for x and y from the 'possibilities' list.
        dx = random.choice(possibilities)
        dy = random.choice(possibilities)
        # Call the main move method with the random steps and grid boundaries.
        self.move(dx, dy, width, height)

    # --- Method: display (Not used in the final simulation loop, but good for debugging) ---
    def display(self):
        print(f"The coordinates of the Point are ({self.get_x()}, {self.get_y()})")


# =================================================================================
# CLASS: Grid (The Container/Environment)
# The Grid class represents the environment where the Points exist and move.
# It is responsible for drawing the border and positioning the Points.
# =================================================================================
class Grid:
    # --- Constructor Method: __init__ ---
    def __init__(self, width, height, points=[]):
        self.width = width      # The horizontal size of the grid area.
        self.height = height    # The vertical size of the grid area.
        self.points = points    # A list to store all the Point objects on the grid.

    # --- Method: add_point ---
    # Simple method to add a new Point object to the Grid's list of points.
    def add_point(self, point):
        self.points.append(point)

    # --- Method: display ---
    # Renders the current state of the grid and all the Points onto the console.
    def display(self):
        # Draw the top border
        print(" " + "_" * self.width)
        
        # Iterate through each row (Y-coordinate)
        for y in range(self.height):
            print("|", end="") # Draw the left wall of the grid
            
            # Iterate through each column (X-coordinate)
            for x in range(self.width):
                marker = " " # Start assuming the space is empty
                
                # Check every Point in the 'self.points' list
                for p in self.points:
                    # If a Point's coordinates match the current (x, y) grid cell:
                    if (p.get_x() == x) and (p.get_y() == y):
                        marker = p.marker # Use that Point's marker character
                        break # Stop checking other points for this cell (assuming no overlap)
                        
                print(marker, end="") # Print the space or the Point's marker
                
            print("|") # Draw the right wall of the grid and move to the next line
            
        # Draw the bottom border
        print(" " + "‾" * self.width)

# =================================================================================
# MAIN PROGRAM EXECUTION
# This section sets up the simulation and runs the main loop.
# =================================================================================

# 1. Instantiate (create) two Point objects
p1 = Point(1, 1, "A") # Point A starts at (1, 1)
p2 = Point(5, 5, "B") # Point B starts at (5, 5)

# 2. Instantiate the Grid object
grid = Grid(10, 10) # Create a 10x10 grid

# 3. Add the Point objects to the Grid
grid.add_point(p1)
grid.add_point(p2)

# --- The Main Simulation Loop ---
# This loop runs forever, updating the position of the points and redrawing the grid.
while True:
    # 1. Move the Points randomly, passing the grid boundaries (10, 10)
    p1.move_random_step(grid.width, grid.height)
    p2.move_random_step(grid.width, grid.height)
    
    # 2. Display the updated grid
    grid.display()
    
    # 3. Pause the program for 0.5 seconds for animation effect (using the 'time' module)
    time.sleep(0.5)
    
    # 4. Clear the console screen (using the 'os' module) to show the next frame
    # Note: 'cls' works on Windows, 'clear' works on Linux/macOS. This code uses 'cls'.
    os.system('cls') 
import random
import time
import os


possibilities = [-1, 0, 1]


class Point:
    def __init__(self, x, y, marker="*"):
        self.__x = x
        self.__y = y
        self.marker = marker

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, value):
        self.__x = value

    def set_y(self, value):
        self.__y = value

    def move(self, dx=0, dy=0, width=-1, height=-1):
        new_x = self.get_x() + dx
        new_y = self.get_y() + dy

        
        if width == -1 and height == -1:
            self.set_x(new_x)
            self.set_y(new_y)
            return

        
        if new_x >= width:
            new_x = width - 1
        if new_x < 0:
            new_x = 0

        if new_y >= height:
            new_y = height - 1
        if new_y < 0:
            new_y = 0

        self.set_x(new_x)
        self.set_y(new_y)

    def move_random_step(self, width, height):
        dx = random.choice(possibilities)
        dy = random.choice(possibilities)
        self.move(dx, dy, width, height)


class Grid:
    def __init__(self, width, height, points=None):
        self.width = width
        self.height = height
        self.points = points if points is not None else []

    def add_point(self, point):
        self.points.append(point)

    def display(self):
        print(" " + "_" * self.width)

        for y in range(self.height):
            print("|", end="")
            for x in range(self.width):
                marker = " "
                for p in self.points:
                    if p.get_x() == x and p.get_y() == y:
                        marker = p.marker
                        break
                print(marker, end="")
            print("|")

        print(" " + "‾" * self.width)



p1 = Point(1, 1, "A")
p2 = Point(5, 5, "B")


grid = Grid(10, 10)

grid.add_point(p1)
grid.add_point(p2)


while True:
    p1.move_random_step(grid.width, grid.height)
    p2.move_random_step(grid.width, grid.height)

    grid.display()

    time.sleep(0.5)

    os.system('cls' if os.name == 'nt' else 'clear')    
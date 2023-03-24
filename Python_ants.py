# import required libraries
import random
import numpy as np
import matplotlib.pyplot as plt

# define Ant class
class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.uniform(0,2*np.pi)
        self.speed = 0.1
        
    def move(self):
        # update position based on current direction and speed
        self.x += self.speed * np.cos(self.direction)
        self.y += self.speed * np.sin(self.direction)
        
    def turn(self, angle):
        # update direction by given angle (in radians)
        self.direction += angle

# define Ant Colony class
class AntColony:
    def __init__(self, width, height, num_ants):
        self.width = width
        self.height = height
        self.num_ants = num_ants
        self.ants = [Ant(random.uniform(0,width), random.uniform(0,height)) for i in range(num_ants)]
        self.scent = np.zeros((width,height))
        
    def add_ant(self):
        # add new ant at random position within colony boundaries
        self.ants.append(Ant(random.uniform(0,self.width), random.uniform(0,self.height)))
        self.num_ants += 1
        
    def remove_ant(self):
        # remove random ant from list
        if self.num_ants > 0:
            self.ants.pop(random.randint(0,self.num_ants-1))
            self.num_ants -= 1
        
    def update_scent(self):
        # decay scent and add scent at current ant positions
        self.scent *= 0.9
        for ant in self.ants:
            x, y = int(ant.x), int(ant.y)
            if x >= 0 and y >= 0 and x < self.width and y < self.height:
                self.scent[x,y] += 0.1
        
    def simulate(self, num_steps, food_pos):
        # run simulation for specified number of steps
        for step in range(num_steps):
            # move ants and update scent trail
            for ant in self.ants:
                ant.move()
                ant.turn(random.uniform(-np.pi/6,np.pi/6))
            self.update_scent()
            
            
            # plot current positions of ants and scent trail
            fig, ax = plt.subplots()
            ax.imshow(self.scent.T, cmap='Greys')
            ax.scatter([ant.x for ant in self.ants], [ant.y for ant in self.ants], s=5)
            ax.set_xlim(0, self.width)
            ax.set_ylim(0, self.height)
            plt.pause(0.01)
            plt.cla()
            
# initialize colony and run simulation
colony = AntColony(100, 100, 100)
colony.simulate(1000, (50,50))
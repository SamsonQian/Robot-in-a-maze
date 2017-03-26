# -----------------------------------------------------------------------------
# Name:       robot
# Purpose:    class definition for robots 
#
# Author:     Samson Qian
# Date:       3/26/17
# -----------------------------------------------------------------------------

"""
Module to describe and control a robot in a maze.
"""
import tkinter

class Robot(object):

    unit_size = 60

    # Class variable describing the maze
    # False represents an obstacle, True represents open space
    maze = [[True, True, False, True, True, True, False, True, True, True],
           [True, True, False, True, True, True, False, True, True, True],
           [True, False, True, True, True, True, False, True, True, True],
           [True, True, True, True, True, True, True, True, False, True],
           [True, True, True, True, True, True, True, True, False, True],
           [True, True, True, True, True, True, True, True, True, True],
           [True, False, False, False, False, True, True, True, True, True],
           [True, True, False, True, True, True, True, True, False, True],
           [True, False, True, True, True, True, True, True, False, True],
           [True, True, True, True, True, True, True, True, False, True]]

    maze_size = len(maze)
    # class variable to represent a full charge
    # A robot with a fully charged battery can take up to 20 steps
    full = 20

    def __init__(self,  name, color, row=0, column=0):
        self.name = name
        self.color = color
        self.row = row
        self.column = column
        self.battery = self.full

    def __str__(self):
        return self.name + ' is a ' + self.color + ' robot lost in the maze'


    def __gt__(self, other):
        return self.battery > other.battery


    def recharge(self):
        self.battery = self.full
        return self
   
    
    
    def helper(self):
        row = self.row
        column = self.column
        
        if (0 <= row < self.maze_size) and (0 <= column < self.maze_size) and self.maze[row][column]:
             return True
        else:
             return False 
   

    def one_step_forward(self):
        self.row += 1
        
        if self.helper() and (self.battery != 0):    
              self.battery -= 1
              return self
        else:
              self.row -= 1
              return self

    def one_step_back(self):
        self.row -= 1
        
        if self.helper() and (self.battery != 0):    
              self.battery -= 1
              return self
        else:
              self.row += 1
              return self

    def one_step_right(self):
        self.column += 1
        
        if self.helper() and (self.battery != 0):    
              self.battery -= 1
              return self
        else:
              self.column -= 1
              return self

    def one_step_left(self):
        self.column -= 1
        
        if self.helper() and (self.battery != 0):    
              self.battery -= 1
              return self
        else:
              self.column += 1
              return self

    def forward(self, steps):
        i = 1
        while i <= steps:
              self.one_step_forward()
              i += 1


    def backward(self, steps):
        i = 1
        while i <= steps:
              self.one_step_back()
              i += 1


    def right(self, steps):
        i = 1
        while i <= steps:
              self.one_step_right()
              i += 1


    def left(self, steps):
        i = 1
        while i <= steps:
              self.one_step_left()
              i += 1


    def show(self):
        """
        Draw a graphical representation of the robot in the maze.
        Imported from Tkinter
        """
        root = tkinter.Tk()
        root.title (self.name + ' in the Maze')
        canvas= tkinter.Canvas(root, background = 'light green',
                               width = self.unit_size * self.maze_size,
                               height = self.unit_size * self.maze_size)
        canvas.grid()  #draw the grid

        # draw a representation of the robot in the maze
        if self.battery:
            upper_x = self.column * self.unit_size + self.unit_size / 4
            upper_y = self.row * self.unit_size
            lower_x = upper_x + self.unit_size / 2
            lower_y = upper_y + self.unit_size
            eye_x = lower_x - 3 * self.unit_size /  20
            eye_y = upper_y + self.unit_size / 10

        else: # the robot ran out of battery
            upper_x = self.column * self.unit_size
            upper_y = self.row * self.unit_size + self.unit_size / 2
            lower_x = upper_x + self.unit_size
            lower_y = upper_y + self.unit_size / 2
            eye_x = lower_x - 9 * self.unit_size / 10
            eye_y = lower_y -  3 * self.unit_size / 20

        rectangle = canvas.create_rectangle(upper_x,
                                            upper_y,
                                            lower_x,
                                            lower_y,
                                            fill = self.color)
        # draw the robot's eyes
        canvas.create_oval(upper_x + self.unit_size / 10,
                           upper_y + self.unit_size / 10,
                           upper_x + 3 * self.unit_size / 20,
                           upper_y + 3 * self.unit_size / 20,
                           fill = 'black')
        canvas.create_oval(eye_x,
                           eye_y,
                           eye_x + self.unit_size / 20,
                           eye_y + self.unit_size / 20,
                           fill = 'black')
        # draw the obstacles in the maze
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                if not self.maze[row][col]:
                    canvas.create_rectangle(col * self.unit_size,
                                            row * self.unit_size,
                                            (col + 1) * self.unit_size,
                                            (row + 1) * self.unit_size,
                                            fill='red')
        # draw lines for the grid
        for row in range(self.maze_size):
            canvas.create_line(0,
                               row * self.unit_size,
                               self.maze_size * self.unit_size,
                               row * self.unit_size)
        for col in range(self.maze_size):
            canvas.create_line(col * self.unit_size,
                               0,
                               col * self.unit_size,
                               self.maze_size * self.unit_size )
        root.mainloop()


#2nd class for Underwater robot for depth

class UnderwaterRobot(Robot):

    depth = 1

    def __init__(self,  name, color, depth, row=0, column=0):
        self.depth = depth
        super().__init__(name, color, row=0, column=0)
        
 
   def __str__(self):
        return self.name + 'is a' + self.color + 'robot diving under water.'

    def dive(self, distance):
        """
        Allows the robot to dive deeper
        """
        self.depth += distance
        return self






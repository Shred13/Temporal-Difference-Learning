"""
Date: October 4th 2020
Author: Shreyansh Anand
Program to showcase the use of Markov Decision Processes in the context of Gridworld
Student Number: 20053370
"""

from copy import deepcopy


class Grid:
    """
    Grid class which will make the grid based on the dimensions and then can be used to find the final values.
    """
    def __init__(self, size, discount_rate):
        """
        Initialize the grid and add a & b (and a' and b') depending on the dimensions
        :param size: dimensions of the grid (5 or 7)
        :param discount_rate: discount rate which impacts learning (0.75 or 0.85)
        """
        self.discount_rate = discount_rate
        self.size = size
        self.grid = []
        for i in range(size):
            self.grid.append([])
            for j in range(size):
                self.grid[i].append(0)  # initialize each cell in the grid to 0.
        if size == 5:
            self.a = (0, 1)
            self.a_prime = (4, 1)
            self.b = (0, 3)
            self.b_prime = (2, 3)
        elif size == 7:
            self.a = (2, 1)
            self.a_prime = (6, 1)
            self.b = (0, 5)
            self.b_prime = (3, 5)
        self.θ = 0.01

    def grid_iterations(self):
        """
        Takes the grid and loops through each cells with the equation to find the optimal values for each part
        :return: Nothing returned, but the grid is printed
        """
        done_with_loop = False
        grid_copy = deepcopy(self.grid)  # grid copied and saved for reference when updating the values
        while not done_with_loop:
            𝚫 = 0
            for row in range(self.size):
                # the while loop is for each iteration, these for loops are for each cell in the grid. The values are
                # updated based on the equation for value iteration
                for col in range(self.size):
                    difference = 0
                    if row == self.a[0] and col == self.a[1]:  # special cases a
                        difference += 10 + self.discount_rate * grid_copy[self.a_prime[0]][self.a_prime[1]]
                    elif row == self.b[0] and col == self.b[1]:  # special cases b
                        difference += 5 + self.discount_rate * grid_copy[self.b_prime[0]][self.b_prime[1]]

                    elif row == 0 and col == 0:  # top row
                        difference += (1 / 2 * (-1 + self.discount_rate * grid_copy[row][col])) + (
                                    1 / 4 * (self.discount_rate * grid_copy[row + 1][col])) + (
                                                  1 / 4 * (self.discount_rate * grid_copy[row][col + 1]))
                    elif row == 0 and col == self.size - 1:
                        difference += (1 / 2 * (-1 + self.discount_rate * grid_copy[row][col])) + (
                                1 / 4 * (self.discount_rate * grid_copy[row + 1][col])) + (
                                              1 / 4 * (self.discount_rate * grid_copy[row][col - 1]))
                    elif row == 0 and col != self.size - 1 and col != 0:
                        difference += (1 / 4 * (-1 + self.discount_rate * grid_copy[row][col])) + (
                                1 / 4 * (self.discount_rate * grid_copy[row + 1][col])) + (
                                              1 / 4 * (self.discount_rate * grid_copy[row][col - 1])) + (
                                              1 / 4 * (self.discount_rate * grid_copy[row][col + 1]))

                    elif row == self.size - 1 and col == 0:  # bottom row
                        difference += (1 / 2 * (-1 + self.discount_rate * grid_copy[row][col])) + (
                                    1 / 4 * (self.discount_rate * grid_copy[row - 1][col])) + (
                                                  1 / 4 * (self.discount_rate * grid_copy[row][col + 1]))
                    elif row == self.size - 1 and col == self.size - 1:
                        difference += (1 / 2 * (-1 + self.discount_rate * grid_copy[row][col])) + (
                                1 / 4 * (self.discount_rate * grid_copy[row - 1][col])) + (
                                              1 / 4 * (self.discount_rate * grid_copy[row][col - 1]))
                    elif row == self.size - 1 and col != self.size - 1 and col != 0:
                        difference += (1 / 4 * (-1 + self.discount_rate * grid_copy[row][col])) + (
                                1 / 4 * (self.discount_rate * grid_copy[row - 1][col])) + (
                                              1 / 4 * (self.discount_rate * grid_copy[row][col - 1])) + (
                                              1 / 4 * (self.discount_rate * grid_copy[row][col + 1]))
                    else:  # middle rows
                        if col == 0:
                            difference += (1 / 4 * (-1 + self.discount_rate * grid_copy[row][col])) + (
                                        1 / 4 * (self.discount_rate * grid_copy[row - 1][col])) + (
                                                      1 / 4 * (self.discount_rate * grid_copy[row][col + 1])) + (
                                                      1 / 4 * (self.discount_rate * grid_copy[row + 1][col]))
                        elif col == self.size - 1:
                            difference += (1 / 4 * (-1 + self.discount_rate * grid_copy[row][col])) + (
                                    1 / 4 * (self.discount_rate * grid_copy[row - 1][col])) + (
                                                  1 / 4 * (self.discount_rate * grid_copy[row][col - 1])) + (
                                                  1 / 4 * (self.discount_rate * grid_copy[row + 1][col]))
                        else:
                            difference += (1 / 4 * (self.discount_rate * grid_copy[row][col + 1])) + (
                                    1 / 4 * (self.discount_rate * grid_copy[row - 1][col])) + (
                                                  1 / 4 * (self.discount_rate * grid_copy[row][col - 1])) + (
                                                  1 / 4 * (self.discount_rate * grid_copy[row + 1][col]))

                    compare_to_delta = abs(self.grid[row][col] - difference)
                    𝚫 = max(𝚫, compare_to_delta)  # see what delta to save, will be the largest change in the
                    # entire iteration
                    self.grid[row][col] = difference
            grid_copy = deepcopy(self.grid)

            if self.θ > 𝚫:  # checks to see if the theta is larger than delta which signifies the error change is
                # not significant anymore and the grids have stabilized.
                done_with_loop = True

    def grid_largest(self, i, j):
        if i == self.a[0] and j == self.a[1]:
            return str(self.a_prime[0]+1) + ", " + str(self.a_prime[1]+1)
        elif i == self.b[0] and j == self.b[1]:
            return str(self.b_prime[0]+1) + ", " + str(self.b_prime[1]+1)

        elif i == 0 and j == 0:
            if self.grid[i + 1][j] > self.grid[i][j + 1]:
                return "⌄"
            else:
                return ">"
        elif i == len(self.grid) - 1 and j == len(self.grid) - 1:
            if self.grid[i - 1][j] > self.grid[i][j - 1]:
                return "^"
            else:
                return "<"
        elif i == len(self.grid) - 1 and j == 0:
            if self.grid[i - 1][j] > self.grid[i][j + 1]:
                return "^"
            else:
                return ">"
        elif i == 0 and j == len(self.grid) - 1:
            if self.grid[i + 1][j] > self.grid[i][j - 1]:
                return "⌄"
            else:
                return "<"

        elif i == 0 and j != 0:
            largest = "⌄" if self.grid[i+1][j] > self.grid[i][j-1] else "<"
            if largest == "⌄" and self.grid[i+1][j] > self.grid[i][j+1]:
                return largest
            elif largest == "⌄" and self.grid[i+1][j] <= self.grid[i][j+1]:
                return ">"
            elif largest == "<" and self.grid[i][j-1] > self.grid[i][j+1]:
                return "<"
            elif largest == "<" and self.grid[i][j-1] <= self.grid[i][j+1]:
                return ">"

        elif i != 0 and j == 0:
            largest = "⌄" if self.grid[i+1][j] > self.grid[i-1][j] else "^"
            if largest == "⌄" and self.grid[i+1][j] > self.grid[i][j+1]:
                return largest
            elif largest == "⌄" and self.grid[i+1][j] <= self.grid[i][j+1]:
                return ">"
            elif largest == "^" and self.grid[i-1][j] > self.grid[i][j+1]:
                return "^️"
            elif largest == "^" and self.grid[i-1][j] <= self.grid[i][j+1]:
                return ">"

        elif i == len(self.grid) - 1:
            largest = "^" if self.grid[i - 1][j] > self.grid[i][j + 1] else ">"
            if largest == "^" and self.grid[i - 1][j] > self.grid[i][j - 1]:
                return largest
            elif largest == "^" and self.grid[i - 1][j] <= self.grid[i][j - 1]:
                return ">"
            elif largest == ">" and self.grid[i][j + 1] > self.grid[i][j - 1]:
                return ">"
            elif largest == ">" and self.grid[i][j + 1] <= self.grid[i][j - 1]:
                return ">"

        elif j == len(self.grid) - 1:
            largest = "^" if self.grid[i - 1][j] > self.grid[i][j - 1] else "<"
            if largest == "^" and self.grid[i - 1][j] > self.grid[i+1][j]:
                return largest
            elif largest == "^" and self.grid[i - 1][j] <= self.grid[i + 1][j]:
                return "⌄"
            elif largest == "<" and self.grid[i][j - 1] > self.grid[i+1][j]:
                return largest
            elif largest == "<" and self.grid[i][j - 1] <= self.grid[i+1][j]:
                return "⌄"

        else:
            largest_between_up_and_down = ("^",  self.grid[i - 1][j])  if self.grid[i - 1][j] > self.grid[i+1][j] else ("⌄",self.grid[i+1][j])
            largest_between_left_and_right = (">", self.grid[i][j+1]) if self.grid[i][j+1] > self.grid[i][j-1] else (">️", self.grid[i][j-1])
            largest = largest_between_left_and_right[0] if largest_between_left_and_right[1] > largest_between_up_and_down[1] else largest_between_up_and_down[0]
            return largest

    def draw_policy(self):
        policy = [[0 for j in range(len(self.grid))] for i in range(len(self.grid))]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j] = round(self.grid[i][j], 1)
                term = self.grid_largest(i, j)
                policy[i][j] = term
            print(([''.join(['{:8}'.format(item) for item in self.grid[i]])]))
        print("\n")

        for i in range(len(policy)):
            print(([''.join(['{:8}'.format(item) for item in policy[i]])]))
        print("\n")


grid_with_5_75 = Grid(5, 0.75)
print("Grid 5x5 with 0.75 Discount")
grid_with_5_75.grid_iterations()
grid_with_5_75.draw_policy()

grid_with_7_75 = Grid(7, 0.75)
print("Grid 7x7 with 0.75 Discount")
grid_with_7_75.grid_iterations()
grid_with_7_75.draw_policy()

grid_with_5_85 = Grid(5, 0.85)
print("Grid 5x5 with 0.85 Discount")
grid_with_5_85.grid_iterations()
grid_with_5_85.draw_policy()

grid_with_7_85 = Grid(7, 0.85)
print("Grid 7x7 with 0.85 Discount")
grid_with_7_85.grid_iterations()
grid_with_7_85.draw_policy()

"""
Date: October 25th 2020
Authors: Shreyansh Anand, Anne Liu
CISC 453/474
Assignment 2
"""
from part_1_of_assignment import Grid
from part_2_of_assignment import algorithm_with_anchor, algorithm_without_anchor, rock_paper_scissors_unanchored, rock_paper_scissors_with_anchor


def main():
    # testing of the Grid and Policy Design
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

    print("PRISONERS")
    algorithm_without_anchor([0.5, 0.5], [0.5, 0.5], [[5, 0], [10, 1]], [[5, 10], [0, 1]], 300000, "Prisoners Dilemma")
    print("\n\n\nPennies without anchor")
    algorithm_without_anchor([0.2, 0.8],[0.2, 0.8], [[1, -1], [-1, 1]], [[-1, 1], [1, -1]], 200000, "Pennies without "
                                                                                                    "anchor")
    print("\n\n\nPennies with anchor")
    algorithm_with_anchor([0.2, 0.8], [[1, -1], [-1, 1]], [[-1, 1], [1, -1]], 5000000, "Pennies with anchor")
    print("\n\n\nRock paper scissors with anchor")
    rock_paper_scissors_with_anchor()
    print("\n\n\nRock paper scissors without anchor")
    rock_paper_scissors_unanchored()


if __name__ == '__main__':
    main()

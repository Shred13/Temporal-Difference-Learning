"""
Date: October 25th 2020
Authors: Shreyansh Anand, Anne Liu
"""

import random
import matplotlib.pyplot as plt


def prisoners_algo_1():
    person1_action1 = []
    person1_action2 = []
    person2_action1 = []
    person2_action2 = []
    person_1_prob = [0.5, 0.5]
    person_2_prob = [0.5, 0.5]
    p1_rewards = [[5, 0], [10, 1]]
    alpha = 0.001
    for i in range(50000):
        person1_action1.append(person_1_prob[0])
        person1_action2.append(person_1_prob[1])
        person2_action1.append(person_2_prob[0])
        person2_action2.append(person_2_prob[1])
        person_1_action = random.random()
        person_2_action = random.random()

        if (person_1_action > person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][1] * (1 - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] + alpha * p1_rewards[1][1] * (1 - person_2_prob[1])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][1] * person_1_prob[0]
            person_2_prob[0] = person_2_prob[0] - alpha * p1_rewards[1][1] * person_2_prob[0]

        elif (person_1_action <= person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][1] * (1 - person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] + alpha * p1_rewards[1][0] * (1 - person_2_prob[1])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][1] * person_1_prob[1]
            person_2_prob[0] = person_2_prob[0] - alpha * p1_rewards[1][0] * person_2_prob[0]

        elif (person_1_action <= person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][0] * (1 - person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] + alpha * p1_rewards[0][0] * (1 - person_2_prob[0])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][0] * person_1_prob[1]
            person_2_prob[1] = person_2_prob[1] - alpha * p1_rewards[0][0] * person_2_prob[1]

        elif (person_1_action > person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][0] * (1 - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] + alpha * p1_rewards[0][1] * (1 - person_2_prob[0])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][0] * person_1_prob[0]
            person_2_prob[1] = person_2_prob[1] - alpha * p1_rewards[0][1] * person_2_prob[1]

        if i % 1000 == 0:
            to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
            to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
            print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))

    plottr([person1_action1, person1_action2], [person2_action1, person2_action2], "Prisoners with Anchor")


def pennies_algo_1():

    person1_action1 = []
    person1_action2 = []
    person2_action1 = []
    person2_action2 = []
    person_1_prob = [0.2, 0.8]
    person_2_prob = [0.2, 0.8]

    p1_rewards = [[1, -1], [-1, 1]]
    p2_rewards = [[-1, 1], [1, -1]]
    alpha = 0.001
    for i in range(50000):
        person1_action1.append(person_1_prob[0])
        person1_action2.append(person_1_prob[1])
        person2_action1.append(person_2_prob[0])
        person2_action2.append(person_2_prob[1])
        person_1_action = random.random()
        person_2_action = random.random()

        if (person_1_action > person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][1] * (1 - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] + alpha * p2_rewards[1][1] * (1 - person_2_prob[1])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][1] * person_1_prob[0]
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[1][1] * person_2_prob[0]

        elif (person_1_action <= person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][1] * (1 - person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] + alpha * p2_rewards[0][1] * (1 - person_2_prob[1])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][1] * person_1_prob[1]
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[0][1] * person_2_prob[0]

        elif (person_1_action <= person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][0] * (1 - person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[0][0] * (1 - person_2_prob[0])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][0] * person_1_prob[1]
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[0][0] * person_2_prob[1]

        elif (person_1_action > person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][0] * (1 - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[1][0] * (1 - person_2_prob[0])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][0] * person_1_prob[0]
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[1][0] * person_2_prob[1]

        if i % 1000 == 0:
            to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
            to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
            print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))

        plottr([person1_action1, person1_action2], [person2_action1, person2_action2], "Pennies without Anchor")

def pennies_algo_2():
    person_1_prob = [0.2, 0.8]
    person_2_prob = [0.2, 0.8]
    p1_rewards = [[1, -1], [-1, 1]]
    p2_rewards = [[-1, 1], [1, -1]]
    alpha = 0.001
    person1_action1 = []
    person1_action2 = []

    person2_action1 = []
    person2_action2 = []
    for i in range(50000):
        person1_action1.append(person_1_prob[0])
        person1_action2.append(person_1_prob[1])

        person2_action1.append(person_2_prob[0])
        person2_action2.append(person_2_prob[1])

        person_1_action = random.random()
        person_2_action = random.random()

        # tails and tails
        if (person_1_action > person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][1] * (1 - person_1_prob[1]) + alpha * (
                        sum(person1_action2) / len(person1_action2) - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] + alpha * p2_rewards[1][1] * (1 - person_2_prob[1]) + alpha * (
                        sum(person2_action2) / len(person2_action2) - person_2_prob[1])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][1] * person_1_prob[0] + alpha * (
                        sum(person1_action1) / len(person1_action1) - person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[1][1] * person_2_prob[0] + alpha * (
                        sum(person2_action1) / len(person2_action1) - person_2_prob[0])

        # heads and tails
        elif (person_1_action <= person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][1] * (1 - person_1_prob[0]) + alpha * (
                        sum(person1_action1) / len(person1_action1) - person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] + alpha * p2_rewards[0][1] * (1 - person_2_prob[1]) + alpha * (
                        sum(person2_action2) / len(person1_action1) - person_2_prob[1])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][1] * person_1_prob[1] + alpha * (
                        sum(person1_action2) / len(person1_action1) - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[0][1] * person_2_prob[0] + alpha * (
                        sum(person2_action1) / len(person1_action1) - person_2_prob[0])

        # heads and heads
        elif (person_1_action <= person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][0] * (1 - person_1_prob[0]) + alpha * (
                        sum(person1_action1) / len(person1_action1) - person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[0][0] * (1 - person_2_prob[0]) + alpha * (
                        sum(person2_action1) / len(person1_action1) - person_2_prob[0])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][0] * person_1_prob[1] + alpha * (
                        sum(person1_action2) / len(person1_action2) - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[0][0] * person_2_prob[1] + alpha * (
                        sum(person2_action2) / len(person2_action2) - person_2_prob[1])

        # tail and heads
        elif (person_1_action > person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][0] * (1 - person_1_prob[1]) + alpha * (
                        sum(person1_action2) / len(person1_action1) - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[1][0] * (1 - person_2_prob[0]) + alpha * (
                        sum(person2_action1) / len(person1_action1) - person_2_prob[0])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][0] * person_1_prob[0] + alpha * (
                        sum(person1_action1) / len(person1_action1) - person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[1][0] * person_2_prob[1] + alpha * (
                        sum(person2_action2) / len(person1_action1) - person_2_prob[1])

        if i % 1000 == 0:
            to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
            to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
            print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))

    plottr([person1_action1, person1_action2], [person2_action1, person2_action2], "Pennies with Anchor")

# todo do the rock paper scissors one, part 1, make graphs for each one and add the value for each game
def rock_paper_scissors():
    # rock, paper, scissors
    person_1_prob = [0.6, 0.2, 0.2]
    person_2_prob = [0.6, 0.2, 0.2]
    # rewards for scenarios (abbreviated) [[rr, rp, rs], [pr, pp, ps], [sr, sp, ss]]
    p1_rewards = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
    p2_rewards = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
    alpha = 0.001
    person1_action1 = []
    person1_action2 = []
    person1_action3 = []

    person2_action1 = []
    person2_action2 = []
    person2_action3 = []

    for i in range(500000):
        person1_action1.append(person_1_prob[0])
        person1_action2.append(person_1_prob[1])
        person1_action3.append(person_1_prob[2])

        person2_action1.append(person_2_prob[0])
        person2_action2.append(person_2_prob[1])
        person2_action3.append(person_2_prob[2])

        person_1_action = random.random()
        person_2_action = random.random()

        # rewards for scenarios (abbreviated) [[rr, rp, rs], [pr, pp, ps], [sr, sp, ss]]
        # rock and rock
        if (0 <= person_1_action <= person_1_prob[0]) and (0 <= person_2_action <= person_2_prob[0]):

            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][0] * (1 - person_1_prob[0]) + alpha * (
                        sum(person1_action1) / len(person1_action1) - person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[0][0] * (1 - person_2_prob[0]) + alpha * (
                        sum(person2_action1) / len(person2_action1) - person_2_prob[0])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][0] * person_1_prob[1] + alpha * (
                        sum(person1_action2) / len(person1_action2) - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[0][0] * person_2_prob[1] + alpha * (
                        sum(person2_action2) / len(person2_action2) - person_2_prob[1])

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[0][0] * person_1_prob[2] + alpha * (
                        sum(person1_action3) / len(person1_action3) - person_1_prob[2])
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[0][0] * person_2_prob[2] + alpha * (
                        sum(person2_action3) / len(person2_action3) - person_2_prob[2])

        # p1 rock and paper
        # p2 paper and  rock
        elif (0 <= person_1_action <= person_1_prob[0]) and (
                person_2_prob[0] <= person_2_action <= person_2_prob[0] + person_2_prob[1]):

            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][1] * (1 - person_1_prob[0]) + alpha * (
                        sum(person1_action1) / len(person1_action1) - person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] + alpha * p2_rewards[0][1] * (1 - person_2_prob[1]) + alpha * (
                        sum(person2_action2) / len(person1_action2) - person_2_prob[1])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][1] * person_1_prob[1] + alpha * (
                        sum(person1_action2) / len(person1_action2) - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[0][1] * person_2_prob[0] + alpha * (
                        sum(person2_action1) / len(person2_action1) - person_2_prob[0])

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[0][1] * person_1_prob[2] + alpha * (
                        sum(person1_action3) / len(person1_action3) - person_1_prob[2])
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[0][1] * person_2_prob[2] + alpha * (
                        sum(person2_action3) / len(person2_action3) - person_2_prob[2])

        # p1 rock and scissors
        # p2 scissors and rock
        elif (0 <= person_1_action <= person_1_prob[0]) and (
                person_2_prob[0] + person_2_prob[1] <= person_2_action <= 1):

            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][2] * (1 - person_1_prob[0]) + alpha * (
                        sum(person1_action1) / len(person1_action1) - person_1_prob[0])
            person_2_prob[2] = person_2_prob[2] + alpha * p2_rewards[0][2] * (1 - person_2_prob[2]) + alpha * (
                        sum(person2_action3) / len(person1_action2) - person_2_prob[2])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][2] * person_1_prob[1] + alpha * (
                        sum(person1_action2) / len(person1_action2) - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[0][2] * person_2_prob[1] + alpha * (
                        sum(person2_action2) / len(person2_action2) - person_2_prob[1])

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[0][2] * person_1_prob[2] + alpha * (
                        sum(person1_action3) / len(person1_action3) - person_1_prob[2])
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[0][2] * person_2_prob[0] + alpha * (
                        sum(person2_action1) / len(person2_action1) - person_2_prob[0])



        # [pr, pp, ps]
        # p1 paper and rock
        elif (person_1_prob[0] <= person_1_action <= person_1_prob[0] + person_1_prob[1]) and (
                0 <= person_2_action <= person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][0] * (1 - person_1_prob[1]) + alpha * (
                        sum(person1_action2) / len(person1_action2) - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[1][0] * (1 - person_2_prob[0]) + alpha * (
                        sum(person2_action1) / len(person2_action1) - person_2_prob[0])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][0] * person_1_prob[0] + alpha * (
                        sum(person1_action1) / len(person1_action1) - person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[1][0] * person_2_prob[1] + alpha * (
                        sum(person2_action2) / len(person2_action2) - person_2_prob[1])

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[1][0] * person_1_prob[2] + alpha * (
                        sum(person1_action3) / len(person1_action3) - person_1_prob[2])
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[1][0] * person_2_prob[2] + alpha * (
                        sum(person2_action3) / len(person2_action3) - person_2_prob[2])

        # p1 paper and paper
        elif (person_1_prob[0] <= person_1_action <= person_1_prob[0] + person_1_prob[1]) and (
                person_2_prob[0] <= person_2_action <= person_2_prob[0] + person_2_prob[1]):

            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][1] * (1 - person_1_prob[0]) + alpha * (
                        sum(person1_action2) / len(person1_action2) - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] + alpha * p2_rewards[1][1] * (1 - person_2_prob[0]) + alpha * (
                        sum(person2_action2) / len(person2_action2) - person_2_prob[1])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][1] * person_1_prob[0] + alpha * (
                        sum(person1_action1) / len(person1_action1) - person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[1][1] * person_2_prob[0] + alpha * (
                        sum(person2_action1) / len(person2_action1) - person_2_prob[0])

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[1][1] * person_1_prob[0] + alpha * (
                        sum(person1_action3) / len(person1_action3) - person_1_prob[2])
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[1][1] * person_2_prob[0] + alpha * (
                        sum(person2_action3) / len(person2_action3) - person_2_prob[2])

        # p1 paper and scissor
        elif (person_1_prob[0] <= person_1_action <= person_1_prob[0] + person_1_prob[1]) and (
                person_2_prob[0] + person_2_prob[1] <= person_2_action <= 1):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][2] * (1 - person_1_prob[1]) + alpha * (
                        sum(person1_action2) / len(person1_action2) - person_1_prob[1])
            person_2_prob[2] = person_2_prob[2] + alpha * p2_rewards[1][2] * (1 - person_2_prob[2]) + alpha * (
                        sum(person2_action3) / len(person2_action3) - person_2_prob[2])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][2] * person_1_prob[0] + alpha * (
                        sum(person1_action1) / len(person1_action1) - person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[1][2] * person_2_prob[1] + alpha * (
                        sum(person2_action2) / len(person2_action2) - person_2_prob[1])

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[1][2] * person_1_prob[2] + alpha * (
                        sum(person1_action3) / len(person1_action3) - person_1_prob[2])
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[1][2] * person_2_prob[0] + alpha * (
                        sum(person2_action1) / len(person2_action1) - person_2_prob[0])

        # [sr, sp, ss]
        # p1 scissor and rock
        elif (person_1_prob[0] + person_1_prob[1] <= person_1_action <= 1) and (
                0 <= person_2_action <= person_2_prob[0]):
            person_1_prob[2] = person_1_prob[2] + alpha * p1_rewards[2][0] * (1 - person_1_prob[2]) + alpha * (
                        sum(person1_action3) / len(person1_action3) - person_1_prob[2])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[2][0] * (1 - person_2_prob[0]) + alpha * (
                        sum(person2_action1) / len(person2_action1) - person_2_prob[0])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[2][0] * person_1_prob[1] + alpha * (
                        sum(person1_action2) / len(person1_action2) - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[2][0] * person_2_prob[1] + alpha * (
                        sum(person2_action2) / len(person2_action2) - person_2_prob[1])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[2][0] * person_1_prob[0] + alpha * (
                        sum(person1_action1) / len(person1_action1) - person_1_prob[0])
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[2][0] * person_2_prob[2] + alpha * (
                        sum(person2_action3) / len(person2_action3) - person_2_prob[2])


        # p1 scissor and paper
        elif (person_1_prob[0] + person_1_prob[1] <= person_1_action <= 1) and (
                person_2_prob[0] <= person_2_action <= person_2_prob[0] + person_2_prob[1]):
            person_1_prob[2] = person_1_prob[2] + alpha * p1_rewards[2][1] * (1 - person_1_prob[2]) + alpha * (
                        sum(person1_action3) / len(person1_action3) - person_1_prob[2])
            person_2_prob[1] = person_2_prob[1] + alpha * p2_rewards[2][1] * (1 - person_2_prob[1]) + alpha * (
                        sum(person2_action2) / len(person2_action2) - person_2_prob[1])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[2][1] * person_1_prob[1] + alpha * (
                        sum(person1_action2) / len(person1_action2) - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[2][1] * person_2_prob[0] + alpha * (
                        sum(person2_action1) / len(person2_action1) - person_2_prob[0])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[2][1] * person_1_prob[0] + alpha * (
                        sum(person1_action1) / len(person1_action1) - person_1_prob[0])
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[2][1] * person_2_prob[2] + alpha * (
                        sum(person2_action3) / len(person2_action3) - person_2_prob[2])

        # p1 scissor and scissor
        elif (person_1_prob[0] + person_1_prob[1] <= person_1_action <= 1) and (
                person_2_prob[0] + person_2_prob[1] <= person_2_action <= 1):
            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[2][2] * person_1_prob[2] + alpha * (
                        sum(person1_action3) / len(person1_action3) - person_1_prob[2])
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[2][2] * person_2_prob[2] + alpha * (
                        sum(person2_action3) / len(person2_action3) - person_2_prob[2])

            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[2][2] * (1 - person_1_prob[0]) + alpha * (
                        sum(person1_action1) / len(person1_action1) - person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[2][2] * (1 - person_2_prob[0]) + alpha * (
                        sum(person2_action1) / len(person2_action1) - person_2_prob[0])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[2][2] * person_1_prob[1] + alpha * (
                        sum(person1_action2) / len(person1_action2) - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[2][2] * person_2_prob[1] + alpha * (
                        sum(person2_action2) / len(person2_action2) - person_2_prob[1])

        if i % 10000 == 0:
            to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
            to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
            print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))

    plottr([person1_action1, person1_action2, person1_action3], [person2_action1, person2_action2, person1_action3], "Rock Paper Scissors with Anchor")

def rock_paper_scissors_unanchored():
    # rock, paper, scissors
    person_1_prob = [0.6, 0.2, 0.2]
    person_2_prob = [0.6, 0.2, 0.2]
    # rewards for scenarios (abbreviated) [[rr, rp, rs], [pr, pp, ps], [sr, sp, ss]]
    p1_rewards = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
    p2_rewards = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
    alpha = 0.001
    person1_action1 = []
    person1_action2 = []
    person1_action3 = []

    person2_action1 = []
    person2_action2 = []
    person2_action3 = []

    for i in range(500000):
        person1_action1.append(person_1_prob[0])
        person1_action2.append(person_1_prob[1])
        person1_action3.append(person_1_prob[2])

        person2_action1.append(person_2_prob[0])
        person2_action2.append(person_2_prob[1])
        person2_action3.append(person_2_prob[2])

        person_1_action = random.random()
        person_2_action = random.random()

        # rewards for scenarios (abbreviated) [[rr, rp, rs], [pr, pp, ps], [sr, sp, ss]]
        # rock and rock
        if (0 <= person_1_action <= person_1_prob[0]) and (0 <= person_2_action <= person_2_prob[0]):

            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][0] * (1 - person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[0][0] * (1 - person_2_prob[0])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][0] * person_1_prob[1]
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[0][0] * person_2_prob[1]

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[0][0] * person_1_prob[2]
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[0][0] * person_2_prob[2]

        # p1 rock and paper
        # p2 paper and  rock
        elif (0 <= person_1_action <= person_1_prob[0]) and (
                person_2_prob[0] <= person_2_action <= person_2_prob[0] + person_2_prob[1]):

            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][1] * (1 - person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] + alpha * p2_rewards[0][1] * (1 - person_2_prob[1])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][1] * person_1_prob[1]
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[0][1] * person_2_prob[0]

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[0][1] * person_1_prob[2]
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[0][1] * person_2_prob[2]

        # p1 rock and scissors
        # p2 scissors and rock
        elif (0 <= person_1_action <= person_1_prob[0]) and (
                person_2_prob[0] + person_2_prob[1] <= person_2_action <= 1):

            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][2] * (1 - person_1_prob[0])
            person_2_prob[2] = person_2_prob[2] + alpha * p2_rewards[0][2] * (1 - person_2_prob[2])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][2] * person_1_prob[1]
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[0][2] * person_2_prob[1]

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[0][2] * person_1_prob[2]
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[0][2] * person_2_prob[0]



        # [pr, pp, ps]
        # p1 paper and rock
        elif (person_1_prob[0] <= person_1_action <= person_1_prob[0] + person_1_prob[1]) and (
                0 <= person_2_action <= person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][0] * (1 - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[1][0] * (1 - person_2_prob[0])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][0] * person_1_prob[0]
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[1][0] * person_2_prob[1]

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[1][0] * person_1_prob[2]
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[1][0] * person_2_prob[2]

        # p1 paper and paper
        elif (person_1_prob[0] <= person_1_action <= person_1_prob[0] + person_1_prob[1]) and (
                person_2_prob[0] <= person_2_action <= person_2_prob[0] + person_2_prob[1]):

            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][1] * (1 - person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] + alpha * p2_rewards[1][1] * (1 - person_2_prob[0])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][1] * person_1_prob[0]
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[1][1] * person_2_prob[0]

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[1][1] * person_1_prob[0]
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[1][1] * person_2_prob[0]

        # p1 paper and scissor
        elif (person_1_prob[0] <= person_1_action <= person_1_prob[0] + person_1_prob[1]) and (
                person_2_prob[0] + person_2_prob[1] <= person_2_action <= 1):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][2] * (1 - person_1_prob[1])
            person_2_prob[2] = person_2_prob[2] + alpha * p2_rewards[1][2] * (1 - person_2_prob[2])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][2] * person_1_prob[0]
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[1][2] * person_2_prob[1]

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[1][2] * person_1_prob[2]
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[1][2] * person_2_prob[0]
        # [sr, sp, ss]

        # p1 scissor and rock
        elif (person_1_prob[0] + person_1_prob[1] <= person_1_action <= 1) and (
                0 <= person_2_action <= person_2_prob[0]):
            person_1_prob[2] = person_1_prob[2] + alpha * p1_rewards[2][0] * (1 - person_1_prob[2])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[2][0] * (1 - person_2_prob[0])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[2][0] * person_1_prob[1]
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[2][0] * person_2_prob[1]

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[2][0] * person_1_prob[0]
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[2][0] * person_2_prob[2]


        # p1 scissor and paper
        elif (person_1_prob[0] + person_1_prob[1] <= person_1_action <= 1) and (
                person_2_prob[0] <= person_2_action <= person_2_prob[0] + person_2_prob[1]):
            person_1_prob[2] = person_1_prob[2] + alpha * p1_rewards[2][1] * (1 - person_1_prob[2])
            person_2_prob[1] = person_2_prob[1] + alpha * p2_rewards[2][1] * (1 - person_2_prob[1])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[2][1] * person_1_prob[1]
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[2][1] * person_2_prob[0]

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[2][1] * person_1_prob[0]
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[2][1] * person_2_prob[2]

        # p1 scissor and scissor
        elif (person_1_prob[0] + person_1_prob[1] <= person_1_action <= 1) and (
                person_2_prob[0] + person_2_prob[1] <= person_2_action <= 1):
            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[2][2] * person_1_prob[2]
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[2][2] * person_2_prob[2]

            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[2][2] * (1 - person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[2][2] * (1 - person_2_prob[0])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[2][2] * person_1_prob[1]
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[2][2] * person_2_prob[1]

        if i % 10000 == 0:
            to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
            to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
            print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))

    plottr([person1_action1, person1_action2, person1_action3], [person2_action1, person2_action2, person1_action3], "Rock Paper Scissors with Anchor")

def plottr(p1, p2, title):
    x = [i for i in range(len(p1[0]))]
    for y in range(len(p1)):
        plt.plot(x, p1[y], label="prob"+str(y+1))
    plt.title(title + " : Person 1")
    plt.legend()
    plt.show()

    for y in range(len(p2)):
        plt.plot(x, p2[y], label="prob2"+str(y+1))
    plt.legend()
    plt.title(title + " : Person 2")
    plt.show()

    # print("PRISONERS")
# prisoners_algo_1()
# print("\n\n\nPennies without anchor")
# pennies_algo_1()
# print("\n\n\nPennies with anchor")
pennies_algo_2()
# print("\n\n\nPennies with anchor")
# rock_paper_scissors()
print("\n\n\nRock paper scissors with anchor")

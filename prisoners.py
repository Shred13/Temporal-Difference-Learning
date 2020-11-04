"""
Date: October 25th 2020
Authors: Shreyansh Anand, Anne Liu
"""

import random
import matplotlib.pyplot as plt
import numpy as np

#prisoner's dilemma optimal policy
def prisoners_algo_1():
    #instantiate variables
    person1_action1 = []
    person1_action2 = []
    person2_action1 = []
    person2_action2 = []
    person_1_prob = [0.5, 0.5]
    person_2_prob = [0.5, 0.5]
    p1_rewards = [[5, 0], [10, 1]]
    p2_rewards = [[5,10], [0, 1]]
    alpha = 0.001
    for i in range(50000):
        person1_action1.append(person_1_prob[0])
        person1_action2.append(person_1_prob[1])
        person2_action1.append(person_2_prob[0])
        person2_action2.append(person_2_prob[1])
        # generate a random action
        person_1_action = random.random()
        person_2_action = random.random()

        # update probability based on action
        # the action taken is dependent on the probability, for instance, person_1_action > person_1_prob[0] is equivalent of person one defecting)
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

        # if i % 1000 == 0:
        #     to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
        #     to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
        #     print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))

    # plot probability change
    plottr([person1_action1, person1_action2], [person2_action1, person2_action2], "Prisoners")
    # results
    print("final value for person 1: " + str(matrix_multiplier(person_1_prob, person_2_prob, p1_rewards)))
    print("final value for person 2: " + str(matrix_multiplier(person_2_prob, person_1_prob, p2_rewards)))
    to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
    to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
    print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))

#Finds pennies optimal policy without anchor
def pennies_algo_1():
    #instantiation
    person1_action1 = []
    person1_action2 = []
    person2_action1 = []
    person2_action2 = []
    person_1_prob = [0.2, 0.8]
    person_2_prob = [0.2, 0.8]

    p1_rewards = [[1, -1], [-1, 1]]
    p2_rewards = [[-1, 1], [1, -1]]
    alpha = 0.001

    #episodes
    for i in range(300000):
        person1_action1.append(person_1_prob[0])
        person1_action2.append(person_1_prob[1])
        person2_action1.append(person_2_prob[0])
        person2_action2.append(person_2_prob[1])
        person_1_action = random.random()
        person_2_action = random.random()

        # update probability based on action
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

        # if i % 1000000 == 0:
        #     to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
        #     to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
        #     print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))

    # plot probability change
    plottr([person1_action1, person1_action2], [person2_action1, person2_action2], "Pennies without Anchor")
    # results
    print("final value for person 1: " + str(matrix_multiplier(person_1_prob, person_2_prob, p1_rewards)))
    print("final value for person 2: " + str(matrix_multiplier(person_2_prob, person_1_prob, p2_rewards)))
    to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
    to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
    print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))

#Finds pennies optimal policy with anchor
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
    sum1_action1 = 0
    sum2_action1 = 0
    sum1_action2 = 0
    sum2_action2 = 0

    #episodes
    for i in range(5000000):
        person1_action1.append(person_1_prob[0])
        sum1_action1 += person_1_prob[0]
        person1_action2.append(person_1_prob[1])
        sum1_action2 += person_1_prob[1]

        person2_action1.append(person_2_prob[0])
        sum2_action1 += person_2_prob[0]
        person2_action2.append(person_2_prob[1])
        sum2_action2 += person_2_prob[1]

        person_1_action = random.random()
        person_2_action = random.random()

        # update probability based on action
        # p1:tails and p2:tails
        if (person_1_action > person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][1] * (1 - person_1_prob[1]) + alpha * (
                        sum1_action2 / len(person1_action2) - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] + alpha * p2_rewards[1][1] * (1 - person_2_prob[1]) + alpha * (
                        sum2_action2 / len(person2_action2) - person_2_prob[1])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][1] * person_1_prob[0] + alpha * (
                        sum1_action1 / len(person1_action1) - person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[1][1] * person_2_prob[0] + alpha * (
                        sum2_action1 / len(person2_action1) - person_2_prob[0])

        # p1:heads and p2:tails
        elif (person_1_action <= person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][1] * (1 - person_1_prob[0]) + alpha * (
                        sum1_action1 / len(person1_action1) - person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] + alpha * p2_rewards[0][1] * (1 - person_2_prob[1]) + alpha * (
                        sum2_action2/ len(person1_action1) - person_2_prob[1])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][1] * person_1_prob[1] + alpha * (
                        sum1_action2 / len(person1_action1) - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[0][1] * person_2_prob[0] + alpha * (
                        sum2_action1 / len(person1_action1) - person_2_prob[0])

        # p1:heads and p2:heads
        elif (person_1_action <= person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][0] * (1 - person_1_prob[0]) + alpha * (
                        sum1_action1/ len(person1_action1) - person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[0][0] * (1 - person_2_prob[0]) + alpha * (
                        sum2_action1 / len(person1_action1) - person_2_prob[0])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][0] * person_1_prob[1] + alpha * (
                        sum1_action2 / len(person1_action2) - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[0][0] * person_2_prob[1] + alpha * (
                        sum2_action2 / len(person2_action2) - person_2_prob[1])

        # p1:tail and p2:heads
        elif (person_1_action > person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][0] * (1 - person_1_prob[1]) + alpha * (
                        sum1_action2 / len(person1_action1) - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[1][0] * (1 - person_2_prob[0]) + alpha * (
                        sum2_action1 / len(person1_action1) - person_2_prob[0])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][0] * person_1_prob[0] + alpha * (
                        sum1_action1 / len(person1_action1) - person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[1][0] * person_2_prob[1] + alpha * (
                        sum2_action2 / len(person1_action1) - person_2_prob[1])

        # if i % 1000000 == 0:
        #     to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
        #     to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
        #     print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))

    # plot probability change
    plottr([person1_action1, person1_action2], [person2_action1, person2_action2], "Pennies with Anchor")
    # results
    print("final value for person 1: " + str(matrix_multiplier(person_1_prob, person_2_prob,  p1_rewards)))
    print("final value for person 2: " + str(matrix_multiplier(person_2_prob, person_1_prob, p2_rewards)))
    to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
    to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
    print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))

# Rock paper scissors optimal policy with anchor
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
    
    sum1_action1 = 0
    sum2_action1 = 0
    sum1_action2 = 0
    sum2_action2 = 0
    sum1_action3 = 0
    sum2_action3 = 0

    #episodes
    for i in range(10000000):
        person1_action1.append(person_1_prob[0])
        sum1_action1 += person_1_prob[0]
        person1_action2.append(person_1_prob[1])
        sum1_action2 += person_1_prob[1]
        person1_action3.append(person_1_prob[2])
        sum1_action3 += person_1_prob[2]

        person2_action1.append(person_2_prob[0])
        sum2_action1 += person_2_prob[0]
        person2_action2.append(person_2_prob[1])
        sum2_action2 += person_2_prob[1]
        person2_action3.append(person_2_prob[2])
        sum2_action3 += person_2_prob[2]

        person_1_action = random.random()
        person_2_action = random.random()

        # update probability based on action
        # rewards for scenarios (abbreviated) [[rr, rp, rs], [pr, pp, ps], [sr, sp, ss]]

        # update for [rr, rp, rs]
        # rock and rock
        if (0 <= person_1_action <= person_1_prob[0]) and (0 <= person_2_action <= person_2_prob[0]):

            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][0] * (1 - person_1_prob[0]) + alpha * (
                        sum1_action1 / len(person1_action1) - person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[0][0] * (1 - person_2_prob[0]) + alpha * (
                        sum2_action1 / len(person2_action1) - person_2_prob[0])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][0] * person_1_prob[1] + alpha * (
                        sum1_action2 / len(person1_action2) - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[0][0] * person_2_prob[1] + alpha * (
                        sum2_action2 / len(person2_action2) - person_2_prob[1])

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[0][0] * person_1_prob[2] + alpha * (
                        sum1_action3 / len(person1_action3) - person_1_prob[2])
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[0][0] * person_2_prob[2] + alpha * (
                        sum2_action3 / len(person2_action3) - person_2_prob[2])


        # p1 rock and paper
        # p2 paper and  rock
        elif (0 <= person_1_action <= person_1_prob[0]) and (
                person_2_prob[0] <= person_2_action <= person_2_prob[0] + person_2_prob[1]):

            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][1] * (1 - person_1_prob[0]) + alpha * (
                        sum1_action1 / len(person1_action1) - person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] + alpha * p2_rewards[0][1] * (1 - person_2_prob[1]) + alpha * (
                        sum2_action2 / len(person1_action2) - person_2_prob[1])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][1] * person_1_prob[1] + alpha * (
                        sum1_action2 / len(person1_action2) - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[0][1] * person_2_prob[0] + alpha * (
                        sum2_action1 / len(person2_action1) - person_2_prob[0])

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[0][1] * person_1_prob[2] + alpha * (
                        sum1_action3 / len(person1_action3) - person_1_prob[2])
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[0][1] * person_2_prob[2] + alpha * (
                        sum2_action3 / len(person2_action3) - person_2_prob[2])

        # p1 rock and scissors
        # p2 scissors and rock
        elif (0 <= person_1_action <= person_1_prob[0]) and (
                person_2_prob[0] + person_2_prob[1] <= person_2_action <= 1):

            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][2] * (1 - person_1_prob[0]) + alpha * (
                        sum1_action1 / len(person1_action1) - person_1_prob[0])
            person_2_prob[2] = person_2_prob[2] + alpha * p2_rewards[0][2] * (1 - person_2_prob[2]) + alpha * (
                        sum2_action3 / len(person1_action2) - person_2_prob[2])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][2] * person_1_prob[1] + alpha * (
                        sum1_action2 / len(person1_action2) - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[0][2] * person_2_prob[1] + alpha * (
                        sum2_action2 / len(person2_action2) - person_2_prob[1])

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[0][2] * person_1_prob[2] + alpha * (
                        sum1_action3 / len(person1_action3) - person_1_prob[2])
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[0][2] * person_2_prob[0] + alpha * (
                        sum2_action1 / len(person2_action1) - person_2_prob[0])



        # [pr, pp, ps]
        # p1 paper and rock
        elif (person_1_prob[0] <= person_1_action <= person_1_prob[0] + person_1_prob[1]) and (
                0 <= person_2_action <= person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][0] * (1 - person_1_prob[1]) + alpha * (
                        sum1_action2 / len(person1_action2) - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[1][0] * (1 - person_2_prob[0]) + alpha * (
                        sum2_action1 / len(person2_action1) - person_2_prob[0])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][0] * person_1_prob[0] + alpha * (
                        sum1_action1 / len(person1_action1) - person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[1][0] * person_2_prob[1] + alpha * (
                        sum2_action2 / len(person2_action2) - person_2_prob[1])

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[1][0] * person_1_prob[2] + alpha * (
                        sum1_action3 / len(person1_action3) - person_1_prob[2])
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[1][0] * person_2_prob[2] + alpha * (
                        sum2_action3 / len(person2_action3) - person_2_prob[2])

        # p1 paper and paper
        elif (person_1_prob[0] <= person_1_action <= person_1_prob[0] + person_1_prob[1]) and (
                person_2_prob[0] <= person_2_action <= person_2_prob[0] + person_2_prob[1]):

            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][1] * (1 - person_1_prob[0]) + alpha * (
                        sum1_action2 / len(person1_action2) - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] + alpha * p2_rewards[1][1] * (1 - person_2_prob[0]) + alpha * (
                        sum2_action2 / len(person2_action2) - person_2_prob[1])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][1] * person_1_prob[0] + alpha * (
                        sum1_action1 / len(person1_action1) - person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[1][1] * person_2_prob[0] + alpha * (
                        sum2_action1 / len(person2_action1) - person_2_prob[0])

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[1][1] * person_1_prob[0] + alpha * (
                        sum1_action3 / len(person1_action3) - person_1_prob[2])
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[1][1] * person_2_prob[0] + alpha * (
                        sum2_action3 / len(person2_action3) - person_2_prob[2])

        # p1 paper and scissor
        elif (person_1_prob[0] <= person_1_action <= person_1_prob[0] + person_1_prob[1]) and (
                person_2_prob[0] + person_2_prob[1] <= person_2_action <= 1):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][2] * (1 - person_1_prob[1]) + alpha * (
                        sum1_action2 / len(person1_action2) - person_1_prob[1])
            person_2_prob[2] = person_2_prob[2] + alpha * p2_rewards[1][2] * (1 - person_2_prob[2]) + alpha * (
                        sum2_action3 / len(person2_action3) - person_2_prob[2])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][2] * person_1_prob[0] + alpha * (
                        sum1_action1 / len(person1_action1) - person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[1][2] * person_2_prob[1] + alpha * (
                        sum2_action2 / len(person2_action2) - person_2_prob[1])

            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[1][2] * person_1_prob[2] + alpha * (
                        sum1_action3 / len(person1_action3) - person_1_prob[2])
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[1][2] * person_2_prob[0] + alpha * (
                        sum2_action1 / len(person2_action1) - person_2_prob[0])



        # [sr, sp, ss]
        # p1 scissor and rock
        elif (person_1_prob[0] + person_1_prob[1] <= person_1_action <= 1) and (
                0 <= person_2_action <= person_2_prob[0]):
            person_1_prob[2] = person_1_prob[2] + alpha * p1_rewards[2][0] * (1 - person_1_prob[2]) + alpha * (
                        sum1_action3 / len(person1_action3) - person_1_prob[2])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[2][0] * (1 - person_2_prob[0]) + alpha * (
                        sum2_action1 / len(person2_action1) - person_2_prob[0])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[2][0] * person_1_prob[1] + alpha * (
                        sum1_action2 / len(person1_action2) - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[2][0] * person_2_prob[1] + alpha * (
                        sum2_action2 / len(person2_action2) - person_2_prob[1])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[2][0] * person_1_prob[0] + alpha * (
                        sum1_action1 / len(person1_action1) - person_1_prob[0])
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[2][0] * person_2_prob[2] + alpha * (
                        sum2_action3 / len(person2_action3) - person_2_prob[2])


        # p1 scissor and paper
        elif (person_1_prob[0] + person_1_prob[1] <= person_1_action <= 1) and (
                person_2_prob[0] <= person_2_action <= person_2_prob[0] + person_2_prob[1]):
            person_1_prob[2] = person_1_prob[2] + alpha * p1_rewards[2][1] * (1 - person_1_prob[2]) + alpha * (
                        sum1_action3 / len(person1_action3) - person_1_prob[2])
            person_2_prob[1] = person_2_prob[1] + alpha * p2_rewards[2][1] * (1 - person_2_prob[1]) + alpha * (
                        sum2_action2 / len(person2_action2) - person_2_prob[1])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[2][1] * person_1_prob[1] + alpha * (
                        sum1_action2 / len(person1_action2) - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] - alpha * p2_rewards[2][1] * person_2_prob[0] + alpha * (
                        sum2_action1 / len(person2_action1) - person_2_prob[0])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[2][1] * person_1_prob[0] + alpha * (
                        sum1_action1 / len(person1_action1) - person_1_prob[0])
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[2][1] * person_2_prob[2] + alpha * (
                        sum2_action3 / len(person2_action3) - person_2_prob[2])

        # p1 scissor and scissor
        elif (person_1_prob[0] + person_1_prob[1] <= person_1_action <= 1) and (
                person_2_prob[0] + person_2_prob[1] <= person_2_action <= 1):
            person_1_prob[2] = person_1_prob[2] - alpha * p1_rewards[2][2] * person_1_prob[2] + alpha * (
                        sum1_action3 / len(person1_action3) - person_1_prob[2])
            person_2_prob[2] = person_2_prob[2] - alpha * p2_rewards[2][2] * person_2_prob[2] + alpha * (
                        sum2_action3 / len(person2_action3) - person_2_prob[2])

            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[2][2] * (1 - person_1_prob[0]) + alpha * (
                        sum1_action1 / len(person1_action1) - person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] + alpha * p2_rewards[2][2] * (1 - person_2_prob[0]) + alpha * (
                        sum2_action1 / len(person2_action1) - person_2_prob[0])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[2][2] * person_1_prob[1] + alpha * (
                        sum1_action2 / len(person1_action2) - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] - alpha * p2_rewards[2][2] * person_2_prob[1] + alpha * (
                        sum2_action2 / len(person2_action2) - person_2_prob[1])

        # if i % 1000000 == 0:
        #     to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
        #     to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
        #     print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))

    # plot probability change
    plottr([person1_action1, person1_action2, person1_action3], [person2_action1, person2_action2, person1_action3], "Rock Paper Scissors with Anchor")
    # results
    print("final value for person 1: " + str(matrix_multiplier(person_1_prob, person_2_prob, p1_rewards)))
    print("final value for person 2: " + str(matrix_multiplier(person_2_prob, person_1_prob, p2_rewards)))
    to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
    to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
    print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))

# Rock paper scissors optimal policy without anchor
def rock_paper_scissors_unanchored():
    # initial probabilities: rock, paper, scissors
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

    #episodes
    for i in range(250000):
        person1_action1.append(person_1_prob[0])
        person1_action2.append(person_1_prob[1])
        person1_action3.append(person_1_prob[2])

        person2_action1.append(person_2_prob[0])
        person2_action2.append(person_2_prob[1])
        person2_action3.append(person_2_prob[2])

        person_1_action = random.random()
        person_2_action = random.random()

        # update probability based on action
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

        # if i % 10000 == 0:
        #     to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
        #     to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
        #     print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))

    # plot probability change
    plottr([person1_action1, person1_action2, person1_action3], [person2_action1, person2_action2, person1_action3], "Rock Paper Scissors without Anchor")
    # results
    print("final value for person 1: " + str(matrix_multiplier(person_1_prob, person_2_prob, p1_rewards)))
    print("final value for person 2: " + str(matrix_multiplier(person_2_prob, person_1_prob, p2_rewards)))
    to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
    to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
    print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))

#plots the probabilities with the x axis as the episodes and y axis as the probability of action
def plottr(p1, p2, title):
    x = [i for i in range(len(p1[0]))]
    for y in range(len(p1)):
        plt.plot(x, p1[y], label="Probability of Action "+str(y+1))
    plt.title(title + " : Person 1")
    plt.xlabel = "# of Iterations"
    plt.ylabel = "Probability"
    plt.legend()
    plt.show()

    for y in range(len(p2)):
        plt.plot(x, p2[y], label="Probability of Action "+str(y+1))
    plt.legend()
    plt.title(title + " : Person 2")
    plt.xlabel = "# of Iterations"
    plt.ylabel = "Probability"
    plt.show()

#calculates the Game values
def matrix_multiplier(prob1, prob2, reward):
    person_1 = np.transpose(np.array(prob1))
    person_2 = np.array(prob2)
    rewards = np.array(reward)
    final_scaler = np.matmul(np.matmul(person_1, rewards), person_2)
    return final_scaler


print("PRISONERS")
prisoners_algo_1()
print("\n\n\nPennies without anchor")
pennies_algo_1()
print("\n\n\nPennies with anchor")
pennies_algo_2()
print("\n\n\nRock paper scissors with anchor")
rock_paper_scissors()
print("\n\n\nRock paper scissors without anchor")
rock_paper_scissors_unanchored()

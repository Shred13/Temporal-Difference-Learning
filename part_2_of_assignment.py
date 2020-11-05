"""
Date: October 25th 2020
Authors: Shreyansh Anand, Anne Liu
"""

import random
import matplotlib.pyplot as plt
import numpy as np


def equation_without_anchor(person_1_prob, person_2_prob, p1_rewards, p2_rewards, person_1_not, person_2_not):
    """
    Function to easily call the Temporal Difference Equation without anchor.
    person_1_prob: the probability of the first action
    person_2_prob: the probability of the second action
    p1_rewards: the first person's rewards based on the actions chosen
    p2_rewards: the second person's rewards based on the actions chosen
    person_1_not: the probabilities of the actions not chosen by the first person
    person_2_not: the probabilities of the actions not chosen by the second person
    """
    alpha = 0.001
    person_1_return = person_1_prob + alpha * p1_rewards * (1 - person_1_prob)
    person_2_return = person_2_prob + alpha * p2_rewards * (1 - person_2_prob)

    return_person_1_not = person_1_not - alpha * p1_rewards * person_1_not
    return_person_2_not = person_2_not - alpha * p2_rewards * person_2_not

    return person_1_return, person_2_return, return_person_1_not, return_person_2_not


def equation_with_anchor(person_1_prob, person_2_prob, p1_rewards, p2_rewards, person_1_not, person_2_not, average1,
                         average2, average3, average4):
    """
    Function to easily call the Temporal Difference Equation with anchor.
    person_1_prob: the probability of the first action
    person_2_prob: the probability of the second action
    p1_rewards: the first person's rewards based on the actions chosen
    p2_rewards: the second person's rewards based on the actions chosen
    person_1_not: the probabilities of the actions not chosen by the first person
    person_2_not: the probabilities of the actions not chosen by the second person
    average1, average2: the average expected probability of the first and second person's chosen actions
    average3, average4: the average expected probability of the first and second person's not chosen actions
    """
    alpha = 0.001
    person_1_return = person_1_prob + alpha * p1_rewards * (1 - person_1_prob) + alpha * (average1 - person_1_prob)
    person_2_return = person_2_prob + alpha * p2_rewards * (1 - person_2_prob) + alpha * (average2 - person_2_prob)

    return_person_1_not = person_1_not - alpha * p1_rewards * person_1_not + alpha * (average3 - person_1_not)
    return_person_2_not = person_2_not - alpha * p2_rewards * person_2_not + alpha * (average4 - person_2_not)

    return person_1_return, person_2_return, return_person_1_not, return_person_2_not


def value_printer(person_1_prob, person_2_prob, p1_rewards, p2_rewards):
    """
    small helper function to print the values of all the different problems
    person_1_prob: the probability of the first action
    person_2_prob: the probability of the second action
    p1_rewards: the first person's rewards based on the actions chosen
    p2_rewards: the second person's rewards based on the actions chosen
    """
    print("final value for person 1: " + str(matrix_multiplier(person_1_prob, person_2_prob, p1_rewards)))
    print("final value for person 2: " + str(matrix_multiplier(person_2_prob, person_1_prob, p2_rewards)))
    to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
    to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
    print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))


def algorithm_without_anchor(person_1_prob, person_2_prob, p1_rewards, p2_rewards, iterations, title):
    """
    General method of the first TD equation without the anchor. This should converge for Prisoners but not pennies
    person_1_prob: the probability of the first action
    person_2_prob: the probability of the second action
    p1_rewards: the first person's rewards based on the actions chosen
    p2_rewards: the second person's rewards based on the actions chosen
    iterations: the number of max iterations the equation should run
    title: the title of the graph that will be plotted
    """
    #  initializing the lists to hold the probabilities of all the different actions
    person1_action1 = []
    person1_action2 = []
    person2_action1 = []
    person2_action2 = []
    for i in range(iterations):
        person1_action1.append(person_1_prob[0])
        person1_action2.append(person_1_prob[1])
        person2_action1.append(person_2_prob[0])
        person2_action2.append(person_2_prob[1])

        #  choosing the actions
        person_1_action = random.random()
        person_2_action = random.random()

        # for prisoners both sides defect
        if (person_1_action > person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[1], person_2_prob[1], person_1_prob[0], person_2_prob[0] = equation_without_anchor(
                person_1_prob[1], person_2_prob[1], p1_rewards[1][1], p2_rewards[1][1], person_1_prob[0],
                person_2_prob[0])
        # for prisoners player 2 defects only
        elif (person_1_action <= person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[0], person_2_prob[1], person_1_prob[1], person_2_prob[0] = equation_without_anchor(
                person_1_prob[0], person_2_prob[1], p1_rewards[0][1], p2_rewards[0][1], person_1_prob[1],
                person_2_prob[0])
        # for prisoners both players cooperate
        elif (person_1_action <= person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[0], person_2_prob[0], person_1_prob[1], person_2_prob[1] = equation_without_anchor(
                person_1_prob[0], person_2_prob[0], p1_rewards[0][0], p2_rewards[0][0], person_1_prob[1],
                person_2_prob[1])
        # for prisoners player 1 defects only
        elif (person_1_action > person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[1], person_2_prob[0], person_1_prob[0], person_2_prob[1] = equation_without_anchor(
                person_1_prob[1], person_2_prob[0], p1_rewards[1][0], p2_rewards[1][0], person_1_prob[0],
                person_2_prob[1])
    # plotting the final results
    plottr([person1_action1, person1_action2], [person2_action1, person2_action2], title)
    value_printer(person_1_prob, person_2_prob, p1_rewards, p2_rewards)


def algorithm_with_anchor(person_1_prob, p1_rewards, p2_rewards, iterations, title):
    """
    General method of the first TD equation without the anchor. This will converge for Pennies
    person_1_prob: the probability of the first action
    person_2_prob: the probability of the second action
    p1_rewards: the first person's rewards based on the actions chosen
    p2_rewards: the second person's rewards based on the actions chosen
    iterations: the number of max iterations the equation should run
    title: the title of the plot that will be used to showcase results
    """
    #  initializing the lists to hold the probabilities of all the different
    #  actions and the 2nd person's action probabilities
    person_2_prob = person_1_prob.copy()
    person1_action1 = []
    person1_action2 = []

    person2_action1 = []
    person2_action2 = []
    # initializing the sums that will be incremented during the for loop
    sum1_action1 = 0
    sum2_action1 = 0
    sum1_action2 = 0
    sum2_action2 = 0

    for i in range(iterations):
        person1_action1.append(person_1_prob[0])
        sum1_action1 += person_1_prob[0]
        person1_action2.append(person_1_prob[1])
        sum1_action2 += person_1_prob[1]

        person2_action1.append(person_2_prob[0])
        sum2_action1 += person_2_prob[0]
        person2_action2.append(person_2_prob[1])
        sum2_action2 += person_2_prob[1]
        # choosing an action
        person_1_action = random.random()
        person_2_action = random.random()

        # this section is similar to the function which does not
        # use an anchor. The only difference here is the use of the anchor.
        if (person_1_action > person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[1], person_2_prob[1], person_1_prob[0], person_2_prob[0] = equation_with_anchor(
                person_1_prob[1], person_2_prob[1], p1_rewards[1][1], p2_rewards[1][1], person_1_prob[0],
                person_2_prob[0], (sum1_action2 / len(person1_action2)), (sum2_action2 / len(person1_action2)),
                (sum1_action1 / len(person1_action2)), (sum2_action1 / len(person1_action2)))

        elif (person_1_action <= person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[0], person_2_prob[1], person_1_prob[1], person_2_prob[0] = equation_with_anchor(
                person_1_prob[0], person_2_prob[1], p1_rewards[0][1], p2_rewards[0][1], person_1_prob[1],
                person_2_prob[0], sum1_action1 / len(person1_action1), sum2_action2 / len(person1_action1),
                                  sum1_action2 / len(person1_action1), sum2_action1 / len(person1_action1))

        elif (person_1_action <= person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[0], person_2_prob[0], person_1_prob[1], person_2_prob[1] = equation_with_anchor(
                person_1_prob[0], person_2_prob[0], p1_rewards[0][0], p2_rewards[0][0], person_1_prob[1],
                person_2_prob[1], sum1_action1 / len(person1_action1), sum2_action1 / len(person1_action1),
                                  sum1_action2 / len(person1_action2), sum2_action2 / len(person2_action2))

        elif (person_1_action > person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[1], person_2_prob[0], person_1_prob[0], person_2_prob[1] = equation_with_anchor(
                person_1_prob[1], person_2_prob[0], p1_rewards[1][0], p2_rewards[1][0], person_1_prob[0],
                person_2_prob[1], sum1_action2 / len(person1_action1), sum2_action1 / len(person1_action1),
                                  sum1_action1 / len(person1_action1), sum2_action2 / len(person1_action1))

    plottr([person1_action1, person1_action2], [person2_action1, person2_action2], title)
    value_printer(person_1_prob, person_2_prob, p1_rewards, p2_rewards)


def rock_paper_scissors_with_anchor():
    """
    Function to find the optimal policy for Rock Paper and Scissors using the TD Algorithm and Anchor
    """
    # rock, paper, scissors probabilities
    person_1_prob = [0.6, 0.2, 0.2]
    person_2_prob = [0.6, 0.2, 0.2]
    # rewards for scenarios (abbreviated) [[rr, rp, rs], [pr, pp, ps], [sr, sp, ss]]
    p1_rewards = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
    p2_rewards = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
    alpha = 0.001  # the learning rate
    # initializing the actions list
    person1_action1 = []
    person1_action2 = []
    person1_action3 = []
    person2_action1 = []
    person2_action2 = []
    person2_action3 = []
    # initializing the incrementors and counters for the sum
    sum1_action1 = 0
    sum2_action1 = 0
    sum1_action2 = 0
    sum2_action2 = 0
    sum1_action3 = 0
    sum2_action3 = 0

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

        # rewards for scenarios (abbreviated) [[rr, rp, rs], [pr, pp, ps], [sr, sp, ss]]
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
    # plotting the results
    plottr([person1_action1, person1_action2, person1_action3], [person2_action1, person2_action2, person1_action3],
           "Rock Paper Scissors with Anchor")
    # printing the value
    value_printer(person_1_prob, person_2_prob, p1_rewards, p2_rewards)


def rock_paper_scissors_unanchored():
    """
    Function to find the optimal policy for Rock Paper and Scissors using the TD Algorithm without the anchor.
    This should not converge
    """
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

    for i in range(50000):
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

    plottr([person1_action1, person1_action2, person1_action3], [person2_action1, person2_action2, person1_action3],
           "Rock Paper Scissors without Anchor")
    value_printer(person_1_prob, person_2_prob, p1_rewards, p2_rewards)


def plottr(p1, p2, title):
    """
    A small helper function to help plot the results of the optimality problems from above
    p1: the probabilities over time steps for the first person
    p2: the probabilities over time steps for the second person
    title: the title used on the graph.
    """
    # the probability graph for the first person
    x = [i for i in range(len(p1[0]))]
    for y in range(len(p1)):
        plt.plot(x, p1[y], label="Probability of Action " + str(y + 1))
    plt.title(title + " : Person 1")
    plt.xlabel = "# of Iterations"
    plt.ylabel = "Probability"
    plt.legend()
    plt.show()
    # the probability graph for the second person
    for y in range(len(p2)):
        plt.plot(x, p2[y], label="Probability of Action " + str(y + 1))
    plt.legend()
    plt.title(title + " : Person 2")
    plt.xlabel = "# of Iterations"
    plt.ylabel = "Probability"
    plt.show()


def matrix_multiplier(prob1, prob2, reward):
    """
    A small helper function to find the value of the games using matrix multiplication
    prob1: the action probabilties of the first person.
    prob2: the action probabilties of the second person.
    reward: the reward matrix used.
    """
    person_1 = np.transpose(np.array(prob1))
    person_2 = np.array(prob2)
    rewards = np.array(reward)
    final_scaler = np.matmul(np.matmul(person_1, rewards), person_2)
    return final_scaler

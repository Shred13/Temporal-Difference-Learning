"""
Date: October 25th 2020
Authors: Shreyansh Anand, Anne Liu
"""

import random


def prisoners_algo_1():
    person_1_prob = [0.5, 0.5]
    person_2_prob = [0.5, 0.5]
    p1_rewards = [[5, 0], [10, 1]]
    alpha = 0.001
    for i in range(50000):
        person_1_action = random.random()
        person_2_action = random.random()

        if(person_1_action > person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][1] * (1-person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] + alpha * p1_rewards[1][1] * (1 - person_2_prob[1])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][1] * person_1_prob[0]
            person_2_prob[0] = person_2_prob[0] - alpha * p1_rewards[1][1] *  person_2_prob[0]

        elif(person_1_action <= person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][1] * (1-person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] + alpha * p1_rewards[1][0] * (1 - person_2_prob[1])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][1] * person_1_prob[1]
            person_2_prob[0] = person_2_prob[0] - alpha * p1_rewards[1][0] * person_2_prob[0]

        elif(person_1_action <= person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][0] * (1-person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] + alpha * p1_rewards[0][0] * (1 - person_2_prob[0])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][0] * person_1_prob[1]
            person_2_prob[1] = person_2_prob[1] - alpha * p1_rewards[0][0] * person_2_prob[1]

        elif(person_1_action > person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][0] * (1 - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] + alpha * p1_rewards[0][1] * (1 - person_2_prob[0])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][0] * person_1_prob[0]
            person_2_prob[1] = person_2_prob[1] - alpha * p1_rewards[0][1] * person_2_prob[1]

        if i % 1000 == 0:
            to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
            to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
            print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))


def pennies_algo_1():
    person_1_prob = [0.2, 0.8]
    person_2_prob = [0.2, 0.8]
    p1_rewards = [[1, -1], [-1, 1]]
    alpha = 0.001
    for i in range(50000):
        person_1_action = random.random()
        person_2_action = random.random()

        if(person_1_action > person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][1] * (1-person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] + alpha * p1_rewards[1][1] * (1 - person_2_prob[1])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][1] * person_1_prob[0]
            person_2_prob[0] = person_2_prob[0] - alpha * p1_rewards[1][1] *  person_2_prob[0]

        elif(person_1_action <= person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][1] * (1-person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] + alpha * p1_rewards[1][0] * (1 - person_2_prob[1])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][1] * person_1_prob[1]
            person_2_prob[0] = person_2_prob[0] - alpha * p1_rewards[1][0] * person_2_prob[0]

        elif(person_1_action <= person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][0] * (1-person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] + alpha * p1_rewards[0][0] * (1 - person_2_prob[0])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][0] * person_1_prob[1]
            person_2_prob[1] = person_2_prob[1] - alpha * p1_rewards[0][0] * person_2_prob[1]

        elif(person_1_action > person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][0] * (1 - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] + alpha * p1_rewards[0][1] * (1 - person_2_prob[0])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][0] * person_1_prob[0]
            person_2_prob[1] = person_2_prob[1] - alpha * p1_rewards[0][1] * person_2_prob[1]

        if i % 1000 == 0:
            to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
            to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
            print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))


def pennies_algo_2():
    person_1_prob = [0.2, 0.8]
    person_2_prob = [0.2, 0.8]
    p1_rewards = [[1, -1], [-1, 1]]
    alpha = 0.001
    person1_action1 = []
    person1_action2 = []

    person2_action1 = []
    person2_action2 = []
    for i in range(100000):
        person1_action1.append(person_1_prob[0])
        person1_action2.append(person_1_prob[1])

        person2_action1.append(person_2_prob[0])
        person2_action2.append(person_2_prob[1])

        person_1_action = random.random()
        person_2_action = random.random()

        if(person_1_action > person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][1] * (1-person_1_prob[1]) + alpha * (sum(person1_action2)/len(person1_action2) - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] + alpha * p1_rewards[1][1] * (1 - person_2_prob[1]) + alpha * (sum(person2_action2)/len(person2_action2) - person_2_prob[1])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][1] * person_1_prob[0] + alpha * (sum(person1_action1)/len(person1_action1) - person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] - alpha * p1_rewards[1][1] * person_2_prob[0] + alpha * (sum(person2_action1)/len(person2_action1) - person_2_prob[0])

        elif(person_1_action <= person_1_prob[0]) and (person_2_action > person_2_prob[0]):
            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][1] * (1-person_1_prob[0]) + alpha * (sum(person1_action1)/len(person1_action1) - person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] + alpha * p1_rewards[1][0] * (1 - person_2_prob[1]) + alpha * (sum(person2_action2)/len(person1_action1) - person_2_prob[1])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][1] * person_1_prob[1] + alpha * (sum(person1_action2)/len(person1_action1) - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] - alpha * p1_rewards[1][0] * person_2_prob[0] + alpha * (sum(person2_action1)/len(person1_action1) - person_2_prob[0])

        elif(person_1_action <= person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[0] = person_1_prob[0] + alpha * p1_rewards[0][0] * (1-person_1_prob[0]) + alpha * (sum(person1_action1)/len(person1_action1) - person_1_prob[0])
            person_2_prob[0] = person_2_prob[0] + alpha * p1_rewards[0][0] * (1 - person_2_prob[0]) + alpha * (sum(person2_action1)/len(person1_action1) - person_2_prob[0])

            person_1_prob[1] = person_1_prob[1] - alpha * p1_rewards[0][0] * person_1_prob[1] + alpha * (sum(person1_action2)/len(person1_action2) - person_1_prob[1])
            person_2_prob[1] = person_2_prob[1] - alpha * p1_rewards[0][0] * person_2_prob[1] + alpha * (sum(person2_action2)/len(person2_action2) - person_2_prob[1])

        elif(person_1_action > person_1_prob[0]) and (person_2_action <= person_2_prob[0]):
            person_1_prob[1] = person_1_prob[1] + alpha * p1_rewards[1][0] * (1 - person_1_prob[1]) + alpha * (sum(person1_action2)/len(person1_action1) - person_1_prob[1])
            person_2_prob[0] = person_2_prob[0] + alpha * p1_rewards[0][1] * (1 - person_2_prob[0]) + alpha * (sum(person2_action1)/len(person1_action1) - person_2_prob[0])

            person_1_prob[0] = person_1_prob[0] - alpha * p1_rewards[1][0] * person_1_prob[0] + alpha * (sum(person1_action1)/len(person1_action1) - person_1_prob[0])
            person_2_prob[1] = person_2_prob[1] - alpha * p1_rewards[0][1] * person_2_prob[1] + alpha * (sum(person2_action2)/len(person1_action1) - person_2_prob[1])

        if i % 1000 == 0:
            to_print1 = [round(person_1_prob[i], 4) for i in range(len(person_1_prob))]
            to_print2 = [round(person_2_prob[i], 4) for i in range(len(person_2_prob))]
            print("person 1 probability: " + str(to_print1) + " person 2 probability: " + str(to_print2))


print("PRISONERS")
prisoners_algo_1()
print("\n\n\nPennies without anchor")
pennies_algo_1()
print("\n\n\nPennies with anchor")
pennies_algo_2()

# todo do the rock paper scissors one, part 1, make graphs for each one and add the value for each game

import random

def swap_two_values(individual):
    choice1, choice2 = random.sample(individual, 2)

    idx1 = individual.index(choice1)
    idx2 = individual.index(choice2)

    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

    return individual

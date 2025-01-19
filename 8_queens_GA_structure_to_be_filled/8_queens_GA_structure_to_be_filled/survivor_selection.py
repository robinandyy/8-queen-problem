"""
My collection of survivor selection methods

"""

#imports
import random


def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    """replacement selection"""

    population = []
    fitness = []

    # student code starts
    for i in range(len(offspring)):
        worst_index = current_fitness.index(min(current_fitness))
        del current_fitness[worst_index]
        del current_pop[worst_index]

    population = current_pop + offspring
    fitness = current_fitness + offspring_fitness
    
    # student code ends
    
    return population, fitness


def random_uniform(current_pop, current_fitness, offspring, offspring_fitness):
    """random uniform selection"""
    population = []
    fitness = []

    # student code starts

    for i in range(len(offspring)):
        choice = random.choice(current_pop)
        current_pop.index(choice)
        del current_pop[choice]
        del current_fitness[choice]

    population = current_pop + offspring
    fitness = current_fitness + offspring_fitness

    # student code ends
    
    return population, fitness



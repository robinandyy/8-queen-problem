"""
My collection of parent selection methods

"""

# imports
import random


def tournament(fitness, mating_pool_size, tournament_size):
    """Tournament selection without replacement"""

    selected_to_mate = []

    # student code starts
    for i in range(mating_pool_size):
        contestants = random.sample(fitness, tournament_size)
        best = max(contestants)
        selected_index = fitness.index(best)
        selected_to_mate.append(selected_index)


    # student code ends
    
    return selected_to_mate


def random_uniform (population_size, mating_pool_size):
    """Random uniform selection"""

    selected_to_mate = []

    # student code starts

    selected_to_mate = random.sample(range(population_size), mating_pool_size)

    

    # student code ends
    
    return selected_to_mate


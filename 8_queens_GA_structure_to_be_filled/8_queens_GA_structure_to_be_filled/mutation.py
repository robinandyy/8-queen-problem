"""
My colleciton of mutation methods

"""

# imports
import random


def permutation_swap (individual):
    """Mutate a permutation"""

    mutant = individual.copy()
    # student code starts
    print(f"here is the individual: {individual}")
    choice, choice2 = random.sample(range(len(individual)), 2)


    mutant[choice], mutant[choice2] = mutant[choice2], mutant[choice]
    print(f"Swapping {choice} with {choice2}")
    # student code ends

    return mutant





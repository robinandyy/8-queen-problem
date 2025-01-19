


import random

def random_permutation(population_size, genome_length):
    population = []


    for i in range(population_size):
        # Create a list of integers from 0 to length-1
        numbers = list(range(1,genome_length))
        # Shuffle the list in place
        random.shuffle(numbers)
        population.append(numbers)


    
    return population




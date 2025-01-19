"""
My collection of initialization methods for different representations

"""








#imports

import random



def permutation (pop_size, genome_length):
    """initialize a population of permutation"""

    population = []
    # student code begin



    for i in range(pop_size):
    
        numbers = list(range(1, genome_length + 1))
        random.shuffle(numbers)
        
        population.append(numbers)
    
    
    return population



   





                 


"""
My collection of fitness evaluation methods

"""

#imports


def fitness_8queen (individual): 
    """Compute fitness of an invidual for the 8-queen puzzle (maximization)"""    

    fitness = 0
    # student code begin


    l = len(individual)
    for i in range(0, l):
        for j in range(i + 1, l):
            if individual[i] - individual[j] == abs(i-j):
                fitness -= 10



    # student code end
    
    return fitness





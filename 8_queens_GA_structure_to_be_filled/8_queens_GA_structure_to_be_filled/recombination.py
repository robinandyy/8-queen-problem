"""
My collection of recombination methods

"""

#imports


def permutation_cut_and_crossfill (parent1, parent2):
    """cut-and-crossfill crossover for permutation representations"""

    offspring1 = []
    offspring2 = []
    
    # student code begin

    for i in range(0,len(parent1)//2):
        offspring1.append(parent1[i])
    


    for i in range(len(parent2)//2, len(parent2)-1):
        if parent2[i] not in offspring1:
            offspring1.append(parent2[i])
    


    while len(offspring1) != len(parent1):
        for i in range(len(parent2)):
                    if parent2[i] not in offspring2:
                        offspring2.append(parent2[i])

    for i in range(0,len(parent1)//2):
        offspring2.append(parent2[i])
    


    for i in range(len(parent2)//2, len(parent2)-1):
        if parent1[i] not in offspring2:
            offspring2.append(parent1[i])
    


    while len(offspring2) != len(parent1):
        for i in range(len(parent2)):
                    if parent1[i] not in offspring2:
                        offspring2.append(parent1[i])

            
                
    # student code end
    
    return offspring1, offspring2




def cut_and_crossfill(parent1, parent2):
    mid = len(parent1)//2

    child1 = []
    child2 = []


    child1.append(parent1[:mid])
    for i in range(mid + 1, len(parent1)):
        if parent2[i] not in child1:
            child1.append(parent2[i])
    
    if len(child1) != len(parent1):
        for i in range(len(parent2)):
            if parent2[i] not in child1:
                child1.append(parent2[i])

    child2.append(parent2[:mid])
    for i in range(mid + 1, len(parent1)):
        if parent1[i] not in child2:
            child2.append(parent1[i])
    
    if len(child2) != len(parent2):
        for i in range(len(parent1)):
            if parent1[i] not in child2:
                child2.append(parent1[i])

    
    return child1, child2

    



    

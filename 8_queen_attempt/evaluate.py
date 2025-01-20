def evaluation(individual):
    score = 0


    for i in range(len(individual)):
        for j in range(len(individual)):
            if individual[i] - individual[j] == i - j:
                score -= 10
    
    return score

    
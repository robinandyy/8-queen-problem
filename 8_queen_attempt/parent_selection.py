import random


def tournament(population, mating_pool_size, fitness, tournament_size):
    parents = []

    
    while len(parents) < mating_pool_size:
        contestants = random.sample(population, tournament_size)
        max = -1000
        for i in range(len(contestants)):
            index = population.index(contestants[i])
            if fitness[index] > max:
                max = index
        parents.append(population[max])

    return parents


# def random_uniform():
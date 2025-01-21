# imports
import random
import initialize
import evaluate
import parent_selection


# set up variables
string_length = 8
pop_size = 20
mating_pool_size = int(pop_size//2)
tournament_size = 4
crossover_rate = 0.7
mutation_rate = 0.3
generation_limit = 50
parent_selection_method = "tournament"
survivor_selection_method = "replacement"



generation = 0

# create population
population = initialize.random_permutation(pop_size, string_length)


fitness = []
for i in range(len(population)):
    fitness.append(evaluate.evaluation(population[i]))



print(f"Generation: {generation} best fitness: {max(fitness)} average fitness: {sum(fitness)/len(fitness)}")

while generation < 1:

    if parent_selection_method == "MPS":
        pass
    elif parent_selection_method == "tournament":
        parents = parent_selection.tournament(population, mating_pool_size, fitness, tournament_size)
        print(parents)
    else: # random uniform
        pass


    generation += 1
    
    offspring = []
    offspring_fitness = []
    # while len(offspring) < mating_pool_size:
    #     if random.random() < crossover_rate:
    #         offspring1, offspring2 = recombination.cut_and_crossfill()
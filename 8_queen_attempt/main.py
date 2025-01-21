# imports
import random
import initialize
import evaluate
import parent_selection
import recombination
import mutation

# set up variables
string_length = 8
pop_size = 20
mating_pool_size = int(pop_size//2)
tournament_size = 4
crossover_rate = 0.7
mutation_rate = 0.3
generation_limit = 50
parent_selection_method = "random_uniform"
survivor_selection_method = "replacement"



generation = 0

# create population
population = initialize.random_permutation(pop_size, string_length)


fitness = []
for i in range(len(population)):
    fitness.append(evaluate.evaluation(population[i]))



print(f"Generation: {generation} best fitness: {max(fitness)} average fitness: {sum(fitness)/len(fitness)}")

while generation < 1:


    # choose parents
    if parent_selection_method == "MPS":
        pass

    elif parent_selection_method == "tournament":
        parents = parent_selection.tournament(population, mating_pool_size, fitness, tournament_size)
        
    else: # random uniform
        parents = parent_selection.random_uniform(population, mating_pool_size)
        print(parents)

    generation += 1
    
    offspring = []
    offspring_fitness = []

    random.shuffle(parents)
    i = 0
    while len(offspring) < mating_pool_size:
        
        # possible crossover
        if random.random() < crossover_rate:
            offspring1, offspring2 = recombination.cut_and_crossfill(parents[i], parents[i + 2])
        
        else: 
            offspring1, offspring2 = parents[i].copy(), parents[i + 1].copy()


        # possible mutation 
        if random.random() < mutation_rate:
            offspring1 = mutation.swap_two_values(offspring1)
            offspring2 = mutation.swap_two_values(offspring2)
        

        offspring.append(offspring1)
        offspring.append(offspring2)

        offspring_fitness.append(evaluate.evaluation(offspring1))
        offspring_fitness.append(evaluate.evaluation(offspring2))

        i += 2
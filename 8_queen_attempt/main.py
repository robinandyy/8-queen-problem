# imports
import initialize
import evaluate


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

print(fitness)
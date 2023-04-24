import random
import math

#Stochastic Uninversal Selection parent selection
def SUS_parent_selection(population, fitness_values, num_parents,machine_count):
    # Calculate total fitness
    total_fitness = sum(fitness_values)

    # Calculate normalized fitness values
    normalized_fitness = [fitness / total_fitness for fitness in fitness_values]
    # Calculate expected number of offspring for each parent
    # Initialize variables
    parents = []
    parent_machines = []
    pointer_distance = 1 / num_parents
    start_pointer = random.uniform(0, pointer_distance)
    cumulative_fitness = normalized_fitness[0]
    parent_index = 0
    # Perform roulette wheel selection
    for i in range(num_parents):
        pointer = start_pointer + i * pointer_distance
        while pointer > cumulative_fitness:
            parent_index += 1
            cumulative_fitness += normalized_fitness[parent_index]
        parents.append(population[parent_index])
        parent_machines.append(machine_count[parent_index])
    return parents , parent_machines

#Rank selection
def rank_selection(population, fitness, num_parents, machine_count):
    # sort the population by fitness in ascending order
    index=list(range(len(fitness)))
    sorted_index= sorted(index,key=lambda x:fitness[x])
    # assign ranks to each individual
    ranks = [i+1 for i in range(len(population))]

    # calculate selection probabilities based on ranks
    probabilities = [rank / sum(ranks) for rank in ranks]

    # select parents based on the probabilities
    parent_indices = random.choices(range(len(population)), weights=probabilities, k=num_parents)

    return [population[sorted_index[i]] for i in parent_indices], [machine_count[sorted_index[i]] for i in parent_indices]

def boltzmann_selection(population, fitness, num_parents, machine_count):

    index=list(range(len(fitness)))
    parent_indices=[]

    # calculate the Boltzmann factors for each individual
    boltzmann_factors = [math.exp(fitness[individual]) for individual in index]
    # calculate the total Boltzmann factor for the population
    total_boltzmann_factor = sum(boltzmann_factors)
    weighted_boltzmann_factor=[i/total_boltzmann_factor for i in boltzmann_factors]
    # select an individual using a weighted random choice based on Boltzmann factors
    parent_indices = random.choices(index, weights=weighted_boltzmann_factor,k=num_parents)
    
    return [population[i] for i in parent_indices], [machine_count[i] for i in parent_indices]

def combine_random(populations, machine_counts):
    population=[]
    machine_count=[]
    for i in range(len(populations[0])):
        index=random.randrange(len(populations))
        population.append(populations[index][i])
        machine_count.append(machine_counts[index][i])

    return population, machine_count
                   



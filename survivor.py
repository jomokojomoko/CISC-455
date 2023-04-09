import random


def tournament_selection(population, fitness, offspring, offspring_fitness, machine_count, offspring_machine_count):

    #Initialzie varible
    total_population = population+offspring
    total_fitness = fitness+offspring_fitness
    total_machine_count = machine_count+offspring_machine_count
    num_survivors = len(population)
    survivors = []
    survivors_fitness = []
    survivors_machine_count = []
    tournament_size = 10

    # Conduct tournaments until we have selected enough survivors
    while len(survivors) < num_survivors:
        tournament = random.sample(range(len(total_population)), tournament_size)

        # Find the fittest individual in the tournament
        winner = max(tournament, key=lambda x: total_fitness[x])

        # Add the winner to the list of survivors
        survivors.append(total_population[winner])
        survivors_fitness.append(total_fitness[winner])
        survivors_machine_count.append(total_machine_count[winner])

    return survivors, survivors_fitness, survivors_machine_count


def truncation_selection(population, fitness, offspring, offspring_fitness, machine_count, offspring_machine_count):
    # sort the population by fitness in descending order
    total_fitness=fitness+offspring_fitness
    index=list(range(len(total_fitness)))
    sorted_index= sorted(index,key=lambda x:total_fitness[x], reverse=True)

    total_population=population+offspring
    total_machine_count=machine_count+offspring_machine_count
    sorted_population=[total_population[i] for i in sorted_index]
    sorted_machine_count=[total_machine_count[i] for i in sorted_index]
    sorted_fitness=[total_fitness[i] for i in sorted_index]

    # calculate the number of individuals to keep
    num_to_keep = (population)

    # select the top individuals to survive
    survivors = sorted_population[:num_to_keep]
    survivors_fitness = sorted_fitness[:num_to_keep]
    survivors_machine_count = sorted_machine_count[:num_to_keep]

    return survivors, survivors_fitness, survivors_machine_count

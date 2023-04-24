# imports
import random
import numpy
import time
import population as generator
import evaluation
import parents as p_selection
import recombination
import mutation
import survivor

   
def main():
    #Keep track of time for data purposes
    start_time=time.time()
    random.seed()
    numpy.random.seed()

    #Size of population
    popsize = 20  
    #Amount of parents
    mating_pool_size = int(popsize*0.5) 
    #Different rates for mutations
    xover_rate = 0.9
    add_rate=0.01
    subtract_rate=0.01
    mut_rate = 0.2
    #Amount of iterations
    gen_limit = 50

    # initialize population
    gen = 0 # initialize the generation counter
    population,machine_count = generator.generate_population(popsize)
    fitness = []
    #Calculate fitness of populations
    for i in range (0, popsize):
        fitness.append(evaluation.calculate_fitness(population[i]))
    print("generation", gen, ": best fitness", max(fitness), "\taverage fitness", sum(fitness)/len(fitness))

    # evolution begins
    while gen < gen_limit:
        
        # pick parents, theres two optiions SUS or Rank selection, SUS should be paired with tournament and rank should be paired with Truncation
        parents1, pmachine_count1 = p_selection.SUS_parent_selection(population,fitness, mating_pool_size,machine_count)
        parents2, pmachine_count2 = p_selection.rank_selection(population,fitness, mating_pool_size,machine_count)
        parents3, pmachine_count3 = p_selection.boltzmann_selection(population,fitness, mating_pool_size,machine_count)
        parents,pmachine_count=p_selection.combine_random([parents1,parents2,parents3],[pmachine_count1,pmachine_count2,pmachine_count3])

        # in order to randomly pair up parents
        random_idx=list(range(len(parents)))
        random.shuffle(random_idx)
    
        # reproduction
        offspring =[]
        offspring_fitness = []
        offspring_machine_count = []
        i= 0 # initialize the counter for parents in the mating pool
        
        # offspring are generated using selected parents in the mating pool
        while len(offspring) < mating_pool_size:
        
            # recombination
            if random.random() < xover_rate:            
                off1,off2,mac1,mac2 = recombination.swap(parents[random_idx[i]], parents[random_idx[i+1]])
            else:
                off1 = parents[random_idx[i]].copy()
                mac1 = pmachine_count[random_idx[i]]
                off2 = parents[random_idx[i+1]].copy()
                mac2= pmachine_count[random_idx[i]]

            # mutation machine reassignment
            if random.random() < mut_rate:
                off1, mac1 = mutation.machine_reassignment(off1,mac1)
            if random.random() < mut_rate:
                off2, mac2 = mutation.machine_reassignment(off2,mac2)
            
              # mutation machine adding
            if random.random() < add_rate:
                off1, mac1 = mutation.machine_add(off1,mac1)
            if random.random() < add_rate:
                off2, mac2 = mutation.machine_add(off2,mac2)

            # mutation machine subtracting
            if random.random() < subtract_rate and mac1 >1:
                off1, mac1 = mutation.machine_subtract(off1,mac1)
            if random.random() < subtract_rate and mac2 >1:
                off2, mac2 = mutation.machine_subtract(off2,mac2)

            #Add the offspring
            offspring.append(off1)
            offspring_fitness.append(evaluation.calculate_fitness(off1))
            offspring_machine_count.append(mac1)
            offspring.append(off2)
        
            offspring_fitness.append(evaluation.calculate_fitness(off2))
            offspring_machine_count.append(mac2)
            i = i+2  # update the counter

        # organize the population of next generation, with either tournament or truncation selection
        population1, fitness1, machine_count1 = survivor.tournament_selection(population, fitness, offspring, offspring_fitness, machine_count,offspring_machine_count)
        population2, fitness2, machine_count2 = survivor.truncation_selection(population, fitness, offspring, offspring_fitness, machine_count,offspring_machine_count)

        population,fitness,machine_count=survivor.combine_random([population1,population2],[fitness1,fitness2],[machine_count1,machine_count2])
        
        gen = gen + 1  # update the generation counter
        end_time=time.time()
        print("generation", gen, ": best fitness", max(fitness), "average fitness", sum(fitness)/len(fitness), "time", end_time-start_time, "seconds")
        
    # evolution ends
    
    # print the final best solution(s)
    end_time=time.time()
    k = 0
    for i in range (0, popsize):
        if fitness[i] == max(fitness):
            print("best solution", k, population[i], fitness[i], machine_count[i])
            k = k+1
    print("Total time taken was ",end_time-start_time)

# end of main


main()


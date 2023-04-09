
# Calculate the fitness of a solution based on the number of conflicting jobs
def calculate_fitness(individual):
    conflicts_time = 0
    num_machines=0
    for i in range(len(individual)):
        s1 = individual[i]["start"]
        e1 = individual[i]["end"]
        if(individual[i]["machine"]>num_machines):
            num_machines=individual[i]["machine"]
        for j in range(i + 1, len(individual)):
            # different machines
            if individual[i]["machine"] != individual[j]["machine"]:
                continue
            s2 = individual[j]["start"]
            e2 = individual[j]["end"]
            overlap_start = max(s1, s2)
            overlap_end = min(e1, e2)
            #If theres a conflicting job add the overlap if not add 0
            conflicts_time += max(0, overlap_end - overlap_start)
    #Normalize with amount of machines
    conflicts_time*=num_machines
    # convert conflict_time minimization problem to a maximization problem
    if(conflicts_time==0):
        return 1
    return 1/conflicts_time


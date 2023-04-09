import random

#Chooses a cut off point and swaps the machines used at those jobs between two parents
def swap(parent1, parent2):
    offspring1 = parent1
    offspring2 = parent2
    machine_count1=0
    machine_count2=0
    #Randomly choose a cut off point
    cutOffPoint = random.sample(range(len(parent1)),1)
    #Swap values up to the cut off point
    for i in range(cutOffPoint[0]):
        offspring1[i]["machine"]=parent2[i]["machine"] 
        offspring2[i]["machine"]=parent1[i]["machine"]
    #Recount machines as that may have switched
    for i in range(len(offspring1)):
        if offspring1[i]["machine"]>machine_count1:
            machine_count1=offspring1[i]["machine"]
        if offspring2[i]["machine"]>machine_count2:
            machine_count2=offspring2[i]["machine"]    
    return offspring1,offspring2,machine_count1,machine_count2
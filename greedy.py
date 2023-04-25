#greedy algorithm that greedily picks tasks whenever a time slot is open
#tasks will be sorted in order of their finish times
#the first task to complete will be the task that finishes earliest
#Assigns task to first device available
#Starts at two machines will add more machines as needed.

import time

#List of times of the jobs required to be completed
#Can add more times in the format of 0-2400 to test. Please make sure initial and end times have the same volume
initial_times=[0,100,200,300,400,500,330,600,730,900,1000,600,1400,1300,1500,700,800,900,1000,1100,1200]
end_times=[30,230,300,450,500,530,600,800,900,1000,1200,800,1600,1700,1630,730,900,1100,1300,1200,1400]

def greedy ():
    #Initialzing time for data collection
    start_Time=time.time()
    num_starting_machines=2
    #Sorts jobs by ending times
    index=list(range(len(end_times)))
    sorted_index= sorted(index,key=lambda x:end_times[x])
    conflict=True
    #Continue until a soloution with no conflicts is found
    while(conflict):
        solution = [] 
        conflict=False
        #Initializing soloution for x amount of machines
        for i in range(num_starting_machines):
            solution.append([(0,0)])
        #Iterate through the times and assign to machines
        for i in range(len(end_times)):
            machine=False
            for j in range(len(solution)):
                #If the conditions are right assign job to machine and move on to the next job
                if (initial_times[sorted_index[i]] >= solution[j][len(solution[j])-1][1]):  #if current time is set before or at the new task's start time
                    solution[j].append((initial_times[sorted_index[i]],end_times[sorted_index[i]]))
                    machine=True
                    break
            #If no solution is found add a machine and move on
            if(machine==False):
                num_starting_machines+=1
                conflict=True
                break
    #Pops out the (0,0) that was used for logic purposes
    for i in range(len(solution)):
        solution[i].pop(0)
    end_Time=time.time()
    return solution, end_Time-start_Time

#Print out the results
def main():
    soloution,time=greedy()
    print("Solution",soloution,"Time",time)
    return 0

main()

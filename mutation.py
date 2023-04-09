import random

#For 1/5 of the jobs randomly reassign a machine
def machine_reassignment(individual,num_machines):
    jobs_to_change=random.sample(range(len(individual)),len(individual)//5)
    for i in range(len(jobs_to_change)):
        individual[jobs_to_change[i]]["machine"]=random.randint(1, num_machines)
    total_machine=0
    #As new solution may have less machines recount
    for i in range(len(individual)):
         if(individual[i]["machine"]>total_machine):
              total_machine=individual[i]["machine"]
    return individual, total_machine

#Add an machine to the solution and change one of the jobs to this machine
def machine_add(individual,num_machines):
    job_to_change=random.randint(0,len(individual)-1)
    individual[job_to_change]["machine"]=num_machines+1
    return individual, num_machines+1

#Remove a machine to the solution and reassign a new solution
def machine_subtract(individual,num_machines):
    for i in range(len(individual)):
            individual[i]["machine"] = random.randint(1, num_machines-1)  # Assign a random machine to the job
    return individual ,num_machines-1
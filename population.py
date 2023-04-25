import random

# Define the problem parameters

num_machines = 2
initial_times=[0,100,200,300,400,500,330,600,730,900,1000,600,1400,1300,1500,700,800,900,1000,1100,1200]
end_times=[30,230,300,450,500,530,600,800,900,1000,1200,800,1600,1700,1630,730,900,1100,1300,1200,1400]
num_jobs = len(initial_times)
# Generate an initial population of random solutions
def generate_population(size):
    population = []
    machine_count=[]
    #Generate size amount of solutions
    for i in range(size):
        individual = []
        for j in range(num_jobs):
            machine = random.randint(1, num_machines)  # Assign a random machine to the job
            start_time = initial_times[j] 
            end_time = end_times[j]  
            job = {
                "machine" : machine,
                "start" : start_time,
                "end" : end_time,
            }
            individual.append(job)
        #Machine count is number of machineses used at each solution initially 2 in this case
        population.append(individual)
        machine_count.append(num_machines)
    return population,machine_count

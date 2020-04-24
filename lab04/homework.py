import random
import queens_fitness

p_mutation = 0.2
num_of_generations = 1000


def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print("Generation {}:".format(generation))
        print_population(population, fitness_fn)

        new_population = set()

        # for i in range(len(population)):
        #     mother, father = random_selection(population, queens_fitness.fitness_fn_negative)
        #     child = reproduce(mother, father)

        #     if random.uniform(0, 1) < p_mutation:
        #         child = mutate(child)

        #     new_population.add(child)

            
        for i in range(len(population)):
            mother, father = random_selection(population, fitness_function)
            child = reproduce(mother, father)
            child2 = reproduce(mother, father)
            if random.uniform(0, 1) < p_mutation:
                child = mutate(child)

            new_population.add(child)
            if random.uniform(0, 1) < p_mutation:
                child2 = mutate(child2)

            new_population.add(child2)

        # Add new population to population, use union to disregard
        # duplicate individuals
        population = population.union(new_population)
        if len(population) >= 20:
            listpopulation = list(population)
            listpopulation.sort(key=fitness_function)
            half = len(listpopulation) // 2
            population = set(listpopulation[half:])


        fittest_individual = get_fittest_individual(population, fitness_fn)

        if minimal_fitness <= fitness_fn(fittest_individual):
            break

    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)
    print("Belongs to " + str(generation) + " Generation")
    return fittest_individual


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


def reproduce(mother, father):
    '''
    Reproduce two individuals with single-point crossover
    Return the child individual
    '''
    child = []
    random_number = random.randint(0,7)
    x = 0
    while x < random_number:
        child.append(mother[x])
        x = x + 1
    while x <= 7:
        child.append(father[x])
        x = x + 1

    return tuple(child)
    #return child


def mutate(individual):
    '''
    Mutate an individual by randomly assigning one of its bits
    Return the mutated individual
    '''
    newindividual = list(individual)
    
    r = random.randint(0,len(newindividual) - 1)
    newindividual[r] = random.randint(0,7)
    return tuple(newindividual)
    #return mutation


#TODO utilize fitness_fn
def random_selection(population, fitness_fn):
    """
    Compute fitness of each in population according to fitness_fn and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
    """

    # Python sets are randomly ordered. Since we traverse the set twice, we
    # want to do it in the same order. So let's convert it temporarily to a
    # list.
    ordered_population = list(population)
    somelist = []
    mother = None
    father = None
    for indi in population:
        fitlevel = fitness_fn(indi)
        for x in range (0,int(fitlevel)):
            somelist.append(indi)
    if somelist:
        random_number = random.randint(0, len(somelist) - 1)
        mother = somelist.pop(random_number)
    if somelist:
        random_number = random_number - 1
        father = somelist.pop(random_number)
    return mother, father



    #return selected
    return ordered_population[0], ordered_population[1]

def fitness_function(individual):
    '''
    Computes the decimal value of the individual
    Return the fitness level of the individual

    Explanation:
    enumerate(list) returns a list of pairs (position, element):

    enumerate((4, 6, 2, 8)) -> [(0, 4), (1, 6), (2, 2), (3, 8)]

    enumerate(reversed((1, 1, 0))) -> [(0, 0), (1, 1), (2, 1)]
    '''
    fitness = queens_fitness.fitness_fn_positive(individual)
    return fitness
    #return fitness


def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    '''
    Randomly generate count individuals of length n
    Note since its a set it disregards duplicate elements.
    '''
    return set([
        tuple(random.randint(0, 7) for _ in range(n))
        for _ in range(count)
    ])


def main():
    minimal_fitness = 28

    # Curly brackets also creates a set, if there isn't a colon to indicate a dictionary
    # initial_population = {
    #     (1, 1, 0),
    #     (0, 0, 0),
    #     (0, 1, 0),
    #     (1, 0, 0)
    # }
    initial_population = get_initial_population(8, 3)

    fittest = genetic_algorithm(initial_population, fitness_function, minimal_fitness)
    print('Fittest Individual: ' + str(fittest))


if __name__ == '__main__':
    main()

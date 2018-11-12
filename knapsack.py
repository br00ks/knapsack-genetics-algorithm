# author: Karin Lampesberger

import random
from random import randint
from helper import total_sum, test_fitness

# items to be packed in knapsack
ITEMS = []
# maximum weight of knapsack
MAX_WEIGHT = 50
# size of population
POPULATION_SIZE = 100
# number of generations
MAX_GENERATION = 100
# representation of the population
MUTATION_PROB = 0.001
# crossover probability
CROSSOVER_PROB = 0.95
# elitism
ELITISM_MAX = 2


# reads the items from an input file
# first value is weight, second value is value
def read_items():
    file_items = open("medium", "r")
    for line in file_items.readlines():
        ITEMS.append([int(line.split(" ")[0]), int(line.split(" ")[1])])
    print(ITEMS)


# returns first generation with randomly created chromosomes
def initialize_first_generation(size):
    print('###### generate first generation ######')
    # length of chromosome = number of items
    first_pop = [[random.randint(0, 1) for x in range(0, len(ITEMS))] for x in range(0, size)]
    population = first_pop
    print('----> first population created, added to POPULATION:')
    print(population)
    return population


def fitness(population):
    print('###### get fitness values for chromosomes ######')
    fitness_values = []
    for index, chromosome in enumerate(population):
        total_weight = total_sum(chromosome, 0, ITEMS)
        total_value = total_sum(chromosome, 1, ITEMS)

        while total_weight > MAX_WEIGHT:
            unpacked_something = False
            while not unpacked_something:
                random_index = randint(0, (len(chromosome) - 1))
                if chromosome[random_index] == 1:
                    chromosome[random_index] = 0
                    total_weight = total_sum(chromosome, 0, ITEMS)
                    total_value = total_sum(chromosome, 1, ITEMS)
                    unpacked_something = True
        fitness_values.append(total_value)
    return fitness_values, population


# create a new generation by using elitism
# take the 2 best chromosomes from last generation and add it to the new generation
# then randomly select by roulette wheel two parens, do crossover and mutate
# add those 2 children to the new generation
def create_new_generation(population, fit):
    print('##### create new generation #####')
    new_generation = []

    # add elites to new generation
    elites = add_elites(population, fit)
    new_generation.extend(elites)

    while len(new_generation) < POPULATION_SIZE:
        # randomly select 2 chromosomes (roulette wheel selection)
        parent1, parent2 = select(population, fit)

        # perform crossover on the 2 selected chromosomes
        chromosomes = crossover(parent1, parent2)

        # perform mutation on the chromosomes obtained
        new_generation.append(mutate(chromosomes[0]))
        new_generation.append(mutate(chromosomes[1]))

    return new_generation


# get the best two chromosomes from a population
def add_elites(population, fit):
    first_highest = 0
    first_index = 0
    second_highest = 0
    second_index = 0
    for index, f in enumerate(fit):
        if f > second_highest:
            if f > first_highest:
                first_highest = f
                first_index = index
            else:
                second_highest = f
                second_index = index
    elites = [population[first_index], population[second_index]]

    return elites


# select parents from a population
def select(population, fit):
    f_sum = sum(fit)
    return pick_parent(f_sum, population, fit), pick_parent(f_sum, population, fit)


# pick parents using roulette wheel selection
def pick_parent(f_sum, population, fit):
    random_integer = random.randint(0, f_sum)
    partial_sum = 0
    for index, chromosome in enumerate(population):
        f_value = fit[index]
        partial_sum = partial_sum + f_value
        if partial_sum >= random_integer:
            return chromosome


# perform one point crossover
def crossover(parent1, parent2):
    random_rate = random.random()
    # only do crossover if random rate < crossover probability
    if random_rate < CROSSOVER_PROB:
        random_crossover_point = random.randint(1, len(parent1) - 1)
        new_parent1 = parent1[:random_crossover_point]
        new_parent2 = parent2[:random_crossover_point]
        new_parent1.extend(parent2[random_crossover_point:])
        new_parent2.extend(parent1[random_crossover_point:])
        return new_parent1, new_parent2
    return parent1, parent2


# mutate each bit with a certain probability
def mutate(chromosome):
    mutated_chromosome = []
    for bit in chromosome:
        random_rate = random.random()
        if random_rate < MUTATION_PROB:
            mutated_bit = 1 if bit is 0 else 1
            mutated_chromosome.append(mutated_bit)
        else:
            mutated_chromosome.append(bit)
    return mutated_chromosome


# function that returns the chromosome with highest value
def get_most_valuable_chromosome(fit, population):
    winner = []
    max_fit = 0
    for index, chromosome in enumerate(population):
        if fit[index] > max_fit:
            max_fit = fit[index]
            winner = population[index]
    return winner


# gets the item for a chromosome
def get_items_for_solution(solution):
    items = []
    for index, bit in enumerate(solution):
        if bit is 1:
            items.append(ITEMS[index])
    return items


def main():
    print("0-1 knapsack problem")

    # read items and add them to ITEMS array[weight, value]
    read_items()

    # initialize first population by randomly generating a population
    population = initialize_first_generation(POPULATION_SIZE)
    fitness_values = []
    generation = 0

    found_best_solution = False

    while not found_best_solution:
        # calculate fitness
        fitness_values, population = fitness(population)
        total_fitness = sum(fitness_values)
        print('fitness')
        print(fitness_values)
        print('generation ' + str(generation) + " has total fitness of:     " + str(total_fitness))

        # test fitness
        if test_fitness(fitness_values, 90):
            found_best_solution = True
        elif test_fitness(fitness_values, 90) and generation > MAX_GENERATION:
            found_best_solution = True
        else:
            print('solution not found yet')
            generation += 1
            # create a new generation
            population = create_new_generation(population, fitness_values)

    # print chromosome with best fitness
    print('--------------------------------------------------------------')
    print('We found a solution!')
    print('the chromosome with highest value:')
    solution = get_most_valuable_chromosome(fitness_values, population)
    print(solution)
    print('The following items are included in the knapsack: ')
    print(get_items_for_solution(solution))


main()

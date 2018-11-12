# author: Karin Lampesberger
# helper functions


# returns the sum of values or weights of items
def total_sum(chromosome, weight_or_value, items):
    t_sum = 0
    for index, bit in enumerate(chromosome):
        if bit is 1:
            t_sum += items[index][weight_or_value]
    return t_sum


# tests what percentage of the chromosomes in population has the same fitness value
def test_fitness(fitness, rate):
    fitness_percentage = 0

    # first count occurrence of fitness values
    fitness_counted = {}
    for index, f in enumerate(fitness):
        if f in fitness_counted:
            fitness_counted[f] += 1
        else:
            fitness_counted[f] = 1

    # second sort by highest value first and lowest last
    sorted_fitness_values = sorted(fitness_counted.items(), key=lambda x: x[1], reverse=True)

    fitness_percentage = (sorted_fitness_values[0][1] * 100) / len(fitness)
    print('fitness percentage: ' + str(fitness_percentage))

    if fitness_percentage > rate:
        return True
    else:
        return False

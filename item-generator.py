import random


def main():
    file = open("testfile", "w")
    number_of_items = 100
    max_value = 1500
    max_weight = 300
    for i in range(number_of_items):
        # weight and value
        random_weight = random.randint(1, max_weight)
        random_value = random.randint(1, max_value)
        string = str(random_weight) + " " + str(random_value)
        file.write(string + '\n')

main()
from matplotlib import pyplot

pyplot.rcParams["figure.figsize"] = [8.00, 6.00]
pyplot.rcParams["figure.autolayout"] = True

def generate_initial(length):
    arr = [0] * length
    arr[-1] = 1
    return arr

def apply_rule(cells):
    next_generation = []
    cells = [0] + cells + [0]
    rules = {(0, 0, 0): 0,(0, 0, 1): 1,(0, 1, 0): 1,(0, 1, 1): 1,(1, 0, 0): 0,(1, 0, 1): 1,(1, 1, 0): 1,(1, 1, 1): 0}

    for element in range(len(cells) - 2):
        pattern = tuple(cells[element:element + 3])
        next_generation.append(rules[pattern])

    return next_generation

def display_generations(generations):
    data = generations
    pyplot.imshow(data, cmap='Greens_r')
    pyplot.show()

initial_generation = generate_initial(101)

generations = [initial_generation]
for element in range(100):
    next_generation = apply_rule(generations[-1])
    generations.append(next_generation)

display_generations(generations)

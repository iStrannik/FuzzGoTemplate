import random


def random_probability_change(probabilities, key=None):
    if not key:
        key = random.choice(list(probabilities.keys()))
    total = len(probabilities[key])
    new_probabilities = generate_random_probabilities(total)
    print(f'Before mutating {key}')
    print(probabilities)
    keys = list(probabilities[key].keys())
    for i in range(len(keys)):
        probabilities[key][keys[i]] = new_probabilities[i]
    print(f'After mutating {key}')
    print(probabilities)
    return probabilities


def generate_random_probabilities(n):
    new_probabilities = []
    sum = 0.0
    for _ in range(n):
        new_probabilities.append(random.uniform(0, 1))
        sum += new_probabilities[-1]
    for i in range(n):
        new_probabilities[i] /= sum
    random.shuffle(new_probabilities)
    return new_probabilities
import random

def random_probability_change(probabilities):
    key = random.choice(list(probabilities.keys()))
    total = len(probabilities[key])
    new_probabilities = []
    high = 1.0
    for i in range(total - 1):
        new_probabilities.append(random.uniform(0, high))
        high = high - new_probabilities[-1]
    new_probabilities.append(high)
    random.shuffle(new_probabilities)
    print(f'Before mutating {key}')
    print(probabilities)
    keys = list(probabilities[key].keys())
    for i in range(len(keys)):
        probabilities[key][keys[i]] = new_probabilities[i]
    print(f'After mutating {key}')
    print(probabilities)
    return probabilities

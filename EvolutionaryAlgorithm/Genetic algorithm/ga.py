import numpy as np

def object(x):
    return np.sum(x ** 2)

def selection(P, fitness):
    cumulative_sum = np.cumsum(fitness)
    total_sum = cumulative_sum[-1]
    selection_probs = cumulative_sum / total_sum
    r = np.random.rand()
    for i, prob in enumerate(selection_probs):
        if r <= prob:
            return P[i]
    return P[-1]

def crossover(parent1, parent2, crossover_rate=0.9):
    if np.random.rand() < crossover_rate:
        crossover_point = np.random.randint(1, len(parent1) - 1)
        child1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
        child2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
        return child1, child2
    else:
        return parent1, parent2

def mutation(individual, mutation_rate=0.1):
    if np.random.rand() < mutation_rate:
        mutation_point = np.random.randint(len(individual))
        individual[mutation_point] = np.random.uniform(-5, 5)
    return individual

NP = 50
D = 5
G = 100
P = np.random.uniform(-5, 5, size=(NP, D))
best = P[np.argmin([object(ind) for ind in P])]

for g in range(G):
    new_P = []
    fitness = np.array([1 / (object(ind) + 1e-6) for ind in P])
    for _ in range(NP // 2):
        parent1 = selection(P, fitness)
        parent2 = selection(P, fitness)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutation(child1)
        child2 = mutation(child2)
        new_P.extend([child1, child2])

    P = np.array(new_P)
    current_best = P[np.argmin([object(ind) for ind in P])]
    if object(current_best) < object(best):
        best = current_best

print(f"最优解：{best}")
print(f"最小值：{object(best)}")

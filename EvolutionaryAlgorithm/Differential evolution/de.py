import numpy as np


def object(x):
    return np.sum(x ** 2)


NP = 50
D = 5
G = 100
F = 1.0
CR = 0.1
P = np.random.uniform(-5, 5, size=(NP, D))
G_best = P[np.argmin([object(ind) for ind in P])]
for g in range(G):
    for i in range(NP):
        a, b, c, d, e = P[np.random.choice(NP, 5)]
        u = a + F * (b - c)
        v = np.copy(P[i])
        mask = np.random.rand(D) <= CR
        v[mask] = u[mask]

        if object(v) < object(P[i]):
            P[i] = v
            if object(P[i]) < object(G_best):
                G_best = P[i]

print(f"最优解：{G_best}")
print(f"最小值：{object(G_best)}")

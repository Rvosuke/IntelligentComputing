import numpy as np
from numpy.random import randint, rand, choice
from math import ceil, log2


# 目标函数
def objective_function(x):
    return x ** 2 + 10 * np.sin(x)


# 编码
def encoding(min_var: float, max_var: float, scale_var: float, popsize: int) -> np.ndarray:
    """
    生成初始种群的二进制编码。

    :param min_var: 变量的最小值，用于确定编码的下界。
    :param max_var: 变量的最大值，用于确定编码的上界。
    :param scale_var: 编码精度的比例因子，决定了每个变量的位数。
    :param popsize: 种群大小，即生成的个体数量。
    :return: 一个二维数组，表示种群的二进制编码，每行代表一个个体。
    """
    # 确定每个变量所需的位数，以确保能够覆盖[min_var, max_var]范围内的所有可能值
    bits = ceil(log2((max_var - min_var) / scale_var))  # ceil()向上取整

    # 生成二进制编码的初始种群，每个个体由`bits`位二进制数表示
    return randint(0, 2, (popsize, bits))


# 解码
def decoding(bin_gen, min_var, scale_var):
    # 将二进制转换为十进制
    decimal_gen = bin_gen.dot(2 ** np.arange(bin_gen.shape[1])[::-1])
    # 缩放到变量的实际范围
    real_gen = min_var + decimal_gen * scale_var
    return real_gen


# 选择
def selection(population, fitness):
    # 根据适应度对种群进行排序
    sorted_indices = np.argsort(fitness)  # argsort()返回排序后的索引
    # 选择适应度最好的一半个体
    selected = population[sorted_indices][:len(population) // 2]
    return selected


# 交叉
def crossover(selected, crossover_rate=0.7):
    offspring = []
    for _ in range(len(selected) // 2):
        if rand() < crossover_rate:
            # 随机选择两个父代进行交叉
            parents = selected[choice(len(selected), 2, replace=False)]
            cross_point = randint(1, len(parents[0]))
            # 产生后代
            offspring1 = np.concatenate([parents[0][:cross_point], parents[1][cross_point:]])  # concatenate()连接两个数组
            offspring2 = np.concatenate([parents[1][:cross_point], parents[0][cross_point:]])
            offspring.extend([offspring1, offspring2])  # extend()在列表末尾一次性追加另一个序列中的多个值
    return np.array(offspring)


# 变异
def mutation(population: np.ndarray, mutation_rate: float = 0.01) -> np.ndarray:
    """
    对种群中的个体进行变异操作。

    :param population: 当前种群的二进制编码，每行代表一个个体。
    :param mutation_rate: 变异率，决定了每个基因发生变异的概率。
    :return: 变异后的种群。

    遍历种群中的每个个体，对于每个个体，根据变异率随机决定是否进行变异。
    如果决定进行变异，随机选择一个基因位进行反转（0变为1，1变为0）。
    """
    for i in range(len(population)):
        if rand() < mutation_rate:
            mutation_point = np.random.randint(len(population[i]))
            population[i][mutation_point] = 1 - population[i][mutation_point]

    return population


# 主函数
def main(min_var=-5, max_var=5, scale_var=1e-3, popsize=10):
    # 生成初始种群
    population = encoding(min_var, max_var, scale_var, popsize)
    # 进化100代
    for _ in range(100):
        # 计算适应度
        fitness = objective_function(decoding(population, min_var, scale_var))
        # 选择
        selected = selection(population, fitness)
        # 交叉
        offspring = crossover(selected)
        # 变异
        population = mutation(offspring)

    # 计算最终种群的适应度
    fitness = objective_function(decoding(population, -10, 0.01))
    # 找到最优个体的索引
    best_idx = np.argmax(fitness)
    # 打印最优个体的二进制编码和十进制解码结果
    print(population[best_idx], decoding(population[best_idx], -10, 0.01))



from scipy.optimize import differential_evolution

# 目标函数
def objective_function(x):
    return x ** 2 + 10 * np.sin(x)

bounds = [(-5, 5)]  # 变量的上下界

result = differential_evolution(objective_function, bounds)

print(result.x, result.fun)
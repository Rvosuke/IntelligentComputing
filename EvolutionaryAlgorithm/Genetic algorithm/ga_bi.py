import numpy as np


def encoding(min_var, max_var, scale_var, popsize):
    bits = np.ceil(np.log2((max_var - min_var) / scale_var)).astype(int)
    bin_gen = np.random.randint(2, size=(popsize, np.sum(bits)))

    return bin_gen, bits


def decoding(bin_gen, bits, min_var, max_var):
    num_var = len(bits)
    popsize = bin_gen.shape[0]
    scale_dec = (max_var - min_var) / (2 ** bits - 1)
    cum_bits = np.cumsum(bits)
    cum_bits = np.insert(cum_bits, 0, 0)

    var = []
    for i in range(num_var):
        bin_var = bin_gen[:, cum_bits[i]:cum_bits[i + 1]]
        powers = 2 ** (np.arange(bin_var.shape[1])[::-1])
        var.append(np.sum(bin_var * powers, axis=1) * scale_dec[i] + min_var[i])

    var_gen = np.column_stack(var)

    fitness = objective_function(var_gen)

    return var_gen, fitness


def selection(old_gen, fitness):
    popsize = len(fitness)
    max_fitness = np.max(fitness)
    index1 = np.argmax(fitness)
    min_fitness = np.min(fitness)
    index2 = np.argmin(fitness)
    best_indiv = old_gen[index1, :]

    index = np.arange(popsize)
    index[index1] = 0
    index[index2] = 0
    index = index[index != 0]

    evo_gen = old_gen[index, :]
    evo_fitness = fitness[index]
    evo_popsize = popsize - 2

    ps = evo_fitness / np.sum(evo_fitness)
    pscum = np.cumsum(ps)
    r = np.random.rand(evo_popsize)
    selected = np.sum(pscum[:, None] < r, axis=0)
    
    evo_gen = evo_gen[selected, :]
    evo_gen = np.array(evo_gen)

    return evo_gen, best_indiv, max_fitness


def crossover(old_gen, pc):
    # 对种群进行随机排序
    mating = np.argsort(np.random.rand(old_gen.shape[0]))
    mat_gen = old_gen[mating, :]
    
    # 确定配对和基因位数
    pairs = mat_gen.shape[0] // 2
    bits = mat_gen.shape[1]

    # 确定进行交叉的配对
    cpairs = np.random.rand(pairs) < pc

    # 生成交叉点
    cpoints = np.random.randint(1, bits, size=pairs)
    cpoints = cpairs * cpoints

    # 创建新一代种群
    new_gen = np.empty_like(old_gen)
    
    # 执行交叉操作
    for i in range(pairs):
        point = cpoints[i]
        if point > 0:
            new_gen[2*i, :point] = mat_gen[2*i, :point]
            new_gen[2*i, point:] = mat_gen[2*i + 1, point:]
            new_gen[2*i + 1, :point] = mat_gen[2*i + 1, :point]
            new_gen[2*i + 1, point:] = mat_gen[2*i, point:]
        else:
            new_gen[2*i] = mat_gen[2*i]
            new_gen[2*i + 1] = mat_gen[2*i + 1]

    return new_gen


def mutation(old_gen, pm):
    # 创建与old_gen同形状的随机数组，并找出小于pm的元素位置
    mpoints = np.random.rand(*old_gen.shape) < pm

    # 创建新的种群
    new_gen = np.array(old_gen, copy=True)

    # 执行突变操作
    new_gen[mpoints] = 1 - old_gen[mpoints]

    return new_gen


# 目标函数
def objective_function(x):
    return np.cos(5 * x) - np.sin(3 * x) + 10


# 遗传算法参数
popsize = 20
scale_var = 0.0001
pc = 0.6  # 交叉概率
pm = 0.1  # 变异概率
min_var = np.array([1])  # 变量的最小值
max_var = np.array([7])  # 变量的最大值

# 编码
bin_gen, bits = encoding(min_var, max_var, scale_var, popsize)

# 遗传算法的迭代次数
iterations = 100

for _ in range(iterations):
    var_gen, fitness = decoding(bin_gen, bits, min_var, max_var)
    bin_gen, best_indiv, best_fitness = selection(bin_gen, fitness)
    # 交叉
    bin_gen = crossover(bin_gen, pc)

    # 变异
    bin_gen = mutation(bin_gen, pm)


# 找到适应度最高的个体
best_index = np.argmax(fitness)
best_individual = var_gen[best_index]
best_fitness = fitness[best_index]

print("最佳个体的值：", best_individual)
print("最高适应度：", best_fitness)

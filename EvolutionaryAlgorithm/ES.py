import numpy as np

# 参数定义
D = 3  # 特征向量的维度
tau_prime = (np.sqrt(2 * D))**-1  # 全局学习率
tau = (np.sqrt(2 * np.sqrt(D)))**-1  # 个体学习率
beta = 0.0873  # 旋转角度变异的学习率，通常是一个较小的常数

# 示例特征向量和策略参数
x_i = np.array([1.0, 2.0, 3.0])  # 可以是任意的初始值
delta_i = np.array([0.1, 0.1, 0.1])  # 可以是任意的初始值

# 变异策略参数
delta_i_prime = delta_i * np.exp(tau_prime * np.random.randn() + tau * np.random.randn(D))

# 旋转角度的变异
alpha = np.zeros((D, D))  # 初始化旋转角度矩阵
for k in range(D - 1):
    for l in range(k + 1, D):
        alpha[k, l] = beta * np.random.randn()

# 构建旋转矩阵
R = np.eye(D)  # 初始化为单位矩阵
for k in range(D - 1):
    for l in range(k + 1, D):
        R_kl = np.eye(D)
        R_kl[k, k] = R_kl[l, l] = np.cos(alpha[k, l])
        R_kl[k, l] = -np.sin(alpha[k, l])
        R_kl[l, k] = np.sin(alpha[k, l])
        R = np.dot(R, R_kl)  # 应用旋转
print(R)
# 生成随机向量η
eta = np.random.randn(D) * delta_i_prime

# 计算变异向量ξ
xi = np.dot(R, eta)

# 变异后的特征向量
x_i_prime = x_i + xi

x_i_prime

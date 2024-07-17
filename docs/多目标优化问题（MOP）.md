# 多目标优化问题（MOP）

在多目标优化问题（Multiobjective Optimization Problems, MOP）中，我们面临的挑战是同时优化两个或更多的冲突目标函数。因为在多个目标中很难找到一个单一的最优解，我们通常寻找所谓的Pareto最优解集。

1. **Pareto Dominance (帕累托支配)**: 如果一个解在所有目标上至少和另一个解一样好，并且至少在一个目标上更好，那么我们说这个解支配另一个解。

2. **Pareto Optimal Set (帕累托最优解集)**: 这个集合包括所有非支配解，也就是没有任何其他解能够支配它们的解。

3. **Pareto Front (帕累托前沿)**: 这是在*目标空间*中的Pareto最优解集的图像，表现为一个曲线或者表面，代表了所有Pareto最优解在目标空间中的*投影*。

现在，让我们看看一个例子：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240111132356929.png" alt="image-20240111132356929" style="zoom:33%;" />

- 优化目标是最小化两个函数：$f_1 = x^2$  和 $f_2 = (x - 2)^2$ 。
- 我们的决策变量`x`的范围被限制在`-2`到`4`之间。

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240111132416651.png" alt="image-20240111132416651" style="zoom:50%;" />

在图中，`f1`和`f2`分别以蓝色和红色表示。我们可以观察到，当`f1`最小化时，`f2`并不是最小的，反之亦然。这就是为什么我们需要Pareto最优解集，它告诉我们在这两个目标之间可以达到的最佳权衡点。在图中，这个集合由图例中黑色虚线之间的点组成，即[0, 2]，这些点代表了在给定约束下的最优解。

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240111132628996.png" alt="image-20240111132628996" style="zoom:50%;" />

图中的Pareto前沿就是显示在目标空间中的曲线。这条曲线上的每一点都是一个Pareto最优解，因为在这一点上你不能改善一个目标而不损害另一个目标。在图中，Pareto前沿是一个由所有最优解组成的曲线，这个曲线展示了在考虑所有目标时可能达到的最佳权衡。

# 汽车购买问题

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240111134108389.png" alt="image-20240111134108389" style="zoom:50%;" />

众所周知，有些车很便宜但开起来并不舒服，而另一些车很舒服但我们买不起。
买车时我们应该考虑这两方面，所以这是一个有两个目标的优化问题：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240111133803737.png" alt="image-20240111133803737" style="zoom: 50%;" />

其中$f_1,f_2$ 是两个冲突的目标，无法同时达到最优，所以我们不得不权衡利弊。

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240111134144232.png" alt="image-20240111134144232" style="zoom:50%;" />

可以通过**进化算法**解决这个问题。

首先，我们生成一个种群作为我们的购买参考。

受$f_1,f_2$ 的影响，算法将促使种群向左上方进化。

直到个体无法再优化为止，算法得到一个最优解集供客户选择。

# 多目标进化算法

## NSGA-II

非支配排序（Nondominated Sorting）和拥挤度距离排序（Crowding Distance Sorting）是NSGA-II算法中的两个关键概念。

1. **非支配排序（Nondominated Sorting）**:
   在NSGA-II算法中，非支配排序用于将种群中的个体分成不同的非支配层级。

   一种简单的非支配排序方法是，对于种群中的每个个体，计算它被其他个体支配的次数（称为支配计数）以及它支配的其他个体的集合。

   种群中的个体被分为不同的非支配前沿，其中第一前沿包含所有不被任何其他个体支配的个体（即支配计数为零的个体）。

   接下来，对于每个非第一前沿的个体，访问它支配的个体集合中的每个成员，并将这些成员的支配计数减一。通过这种方式，可以识别出属于第二非支配前沿的个体（此时支配计数为零的个体）。此过程持续进行，直到识别出所有的非支配前沿。

   <img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240112132638114.png" alt="image-20240112132638114" style="zoom:50%;" />

2. **拥挤度距离排序（Crowding Distance Sorting）**:
   在NSGA-II算法中，拥挤度距离用于评估种群中个体的多样性。计算每个个体的拥挤度距离，即在每个目标函数中，计算该个体与其两侧邻居<!--如何判断两侧邻居？-->在该目标上的平均距离。这个距离可被视为由最近邻居构成的立方体的周长的估计值。 

   对于种群中每个目标函数，首先根据该目标函数值的大小对种群进行排序。然后，为每个目标函数的边界解（即具有最小和最大函数值的解）分配无限大的距离值。

   <img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240112165926155.png" alt="image-20240112165926155" style="zoom:50%;" />

   对于其他中间解，分配的距离值等于两个相邻解的函数值之差的绝对值（经过标准化处理）。进行这种计算后，每个个体的总拥挤度距离值是对应于每个目标的个别距离值之和。

   <img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240112165845667.png" alt="image-20240112165845667" style="zoom:50%;" />

在比较两个解时，如果它们具有不同的非支配等级，则选择具有较低（更好）等级的解。如果两个解属于相同的非支配前沿，则选择位于较不拥挤区域的解。通过这种方式，算法在其不同阶段的选择过程中被引导，以实现Pareto最优前沿的均匀分布。

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240112170144643.png" alt="image-20240112170144643" style="zoom: 50%;" />

这张图展示了NSGA-II算法的框架和流程，包括非支配排序和拥挤度距离排序两个关键步骤。以下是对框架图的详细解释：

1. **变量名**:
   - $ P_t $: 当前种群，种群大小为 $ N $。
   - $ Q_t $: 当前种群生成的子代种群，大小也为 $ N $。
   - $ R_t $: 由当前种群 $ P_t $ 和子代种群 $ Q_t $ 合并而成的种群，其大小为 $ 2N $。
   - $ F_1, F_2, F_3, \ldots $: 表示非支配排序中得到的不同的非支配前沿，$ F_1 $ 是最优前沿。
   - $ P_{t+1} $: 下一代种群，其大小为 $ N $。

2. **流程图详细的过程**:
   - **非支配排序**:
     - 将合并后的种群 $ R_t $ 进行非支配排序，识别出不同的非支配前沿 $ F_1, F_2, F_3, \ldots $。
     - 这些前沿按照非支配等级进行排列，$ F_1 $ 是最优前沿，意味着它的个体没有被任何其他个体支配。
     - 排序后，较优的非支配前沿（如 $ F_1 $）将被优先选择进入下一代种群 $ P_{t+1} $。

   - **拥挤度距离排序**:
     - 在每个非支配前沿中，对个体根据它们的拥挤度距离进行排序。这个距离反映了个体周围解的分布密度，即个体的多样性。
     - 在选取进入下一代种群 $ P_{t+1} $ 的个体时，不仅考虑它们的非支配等级，也考虑其拥挤度距离。
     - 当下一代种群 $ P_{t+1} $ 的大小达到 $ N $ 时，流程停止，剩余的个体将被拒绝（Rejected）。

通过这个流程，NSGA-II算法确保了种群的质量（通过非支配排序确定优质解）和多样性（通过拥挤度距离保证解的分散性），从而在多目标优化问题中有效地逼近Pareto最优前沿。

## MOEA/D

与 NSGA-II 不同，MOEA/D 基于传统的分解，初始化一组权重向量并利用邻居信息来更新种群。

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240112173635134.png" alt="image-20240112173635134" style="zoom:50%;" />

这张图说明了MOEA/D算法如何将多目标优化问题分解为一系列单目标优化问题，并求解这些问题来近似整个Pareto最优前沿。具体的解释如下：

- **最小化 $ f_1(\mathbf{\hat{x}}), f_2(\mathbf{\hat{x}}) $**: 这是一个多目标优化问题，其中 $ f_1 $ 和 $ f_2 $ 是需要被最小化的目标函数，而 $ \mathbf{\hat{x}} $ 是决策变量向量。

- **最小化 $ \alpha f_1(\mathbf{\hat{x}}) + (1 - \alpha) f_2(\mathbf{\hat{x}}) $**: 这是MOEA/D算法中的关键步骤，它将多目标问题分解为一系列单目标问题。在这里，$ \alpha $ 是权重，$ 0 \leq \alpha \leq 1 $，它定义了在两个目标函数之间的权衡。通过改变 $ \alpha $ 的值，可以在整个目标函数空间中搜索不同的权衡解，以形成Pareto最优解集。

- $ \alpha_1 = 0.0 $ 到 $ \alpha_{11} = 1.0 $: 这些是权重系数，分别代表了在目标函数 $ f_1 $ 和 $ f_2 $ 之间的不同偏好。例如，当 $ \alpha = 0 $ 时，优化完全关注于最小化 $ f_1 $，而当 $ \alpha = 1 $ 时，优化完全关注于最小化 $ f_2 $。

- **$ \mathbf{\hat{x}}^*_1, \mathbf{\hat{x}}^*_2, \ldots, \mathbf{\hat{x}}^*_{11} $**: 这些是对应于不同权重 $ \alpha $ 值的最优解。当使用不同的权重组合解决单目标优化问题时，这些最优解在目标函数空间中形成了Pareto最优前沿的近似。

- **Pareto Optimal Solutions**: 这个椭圆表示在两个目标函数空间中形成的Pareto最优前沿。理想情况下，通过解决一系列用不同权重 $ \alpha $ 分解出的单目标问题，MOEA/D能够生成整个Pareto最优前沿的一个良好近似。

在MOEA/D算法的实际实现中，每个权重向量对应一个单目标优化问题，算法通过更新解与其邻居信息来逐渐逼近Pareto前沿。这个邻居信息是基于权重向量之间的距离，邻近的权重向量通常会产生相似的解。通过这种方式，算法能够有效地在多目标函数空间中均匀地搜索解，以便找到一个均匀分布的Pareto最优解集。

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240112174432247.png" alt="image-20240112174432247" style="zoom: 40%;" /><img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240112174557410.png" alt="image-20240112174557410" style="zoom:40%;" />

这两幅图展示了MOEA/D（基于分解的多目标进化算法）的进化过程。MOEA/D的主要特点是它通过将多目标优化问题分解成一系列的单目标优化问题来进行求解。以下是具体的算法步骤：

1. **Generate NP weight vectors (生成权重向量)**:

  这个步骤涉及生成一个均匀分布的权重向量集合，其中NP代表种群大小。每个权重向量都对应于目标空间中的一个方向，它们代表了多目标优化问题中不同目标之间的权衡。

2. **Generate an individual, corresponding to each weight vector (为每个权重向量生成个体)**:

  对每个权重向量，算法生成一个个体，该个体代表了根据对应权重向量分解得到的单目标优化问题的解。

3. **Calculate the neighbors (计算邻居)**:

   在这个步骤中，算法计算每个个体的邻居。邻居的定义是基于权重向量之间的距离，即在权重向量空间中彼此接近的个体被认为是邻居。

4. **Generate an offspring with two selected neighbors (用两个选定的邻居生成后代)**:

   通过选取两个邻居个体，算法生成一个新的后代个体。这个过程通常涉及交叉和变异操作。

5. **Evaluate the offspring and replace its parent if it is better (评估后代并在更优时替换其父代)**:

   新生成的后代个体会被评估，如果它比其父代更优（即更接近Pareto前沿或具有更好的适应度值），则在种群中替换其父代个体。

图中的蓝色曲线代表真实的Pareto前沿，而红点代表算法通过这些权重向量生成的解集。

图中的浅蓝色点线圈指示了通过邻居信息更新过程中产生的新的潜在Pareto优解，这显示了算法是如何通过局部搜索和邻居信息来迭代改进解集，逐渐接近真实的Pareto前沿。

MOEA/D算法的核心思想是通过分解和局部搜索相结合的方式，充分利用邻居信息来引导种群向Pareto最优解集进化。这两幅图展示了MOEA/D算法如何在多目标空间中均匀地分布解，并通过邻居间的交互来提升解的质量。

**三个问题**

1. 如何将种群与权重向量关联起来？

   每个个体都与相应的权重向量相关联

2. 如何进化种群？

   邻居的个体被选择来产生新的后代

3. 如何选择邻居？

   使用欧几里得距离

MODE/D的框架如下图：

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240112175422029.png" alt="image-20240112175422029" style="zoom:50%;" />
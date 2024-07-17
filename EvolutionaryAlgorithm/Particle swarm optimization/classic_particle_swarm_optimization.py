import numpy as np


class ParticleSwarmOptimization:
    def __init__(self, n, d, w, c1, c2, termination_condition, f, model = "classic"):
        """
        :param n: Number of particles in the swarm
        :param d: Number of dimensions
        :param w: Inertia weight
        :param c1: Cognitive acceleration coefficient
        :param c2: Social acceleration coefficient
        :param termination_condition: Function to determine when to stop the optimizer
        :param f: Objective function to minimize
        """
        self.n = n  # Number of particles
        self.d = d  # Dimension of the problem
        self.w = w  # Inertia weight
        self.c1 = c1  # Cognitive acceleration coefficient
        self.c2 = c2  # Social acceleration coefficient
        self.termination_condition = termination_condition
        self.f = f  # Objective function
        self.P = None  # Positions of particles
        self.V = None  # Velocities of particles
        self.P_best = None  # Personal best positions
        self.G_best = None  # Global best position
        self.model = model

    def initialize(self):
        """
        Initializes the swarm, velocities, and personal best positions.
        """
        self.P = np.random.uniform(low=-5, high=5, size=(self.n, self.d))
        self.V = np.zeros((self.n, self.d))
        self.P_best = np.copy(self.P)
        G_best_index = np.argmin([self.f(p) for p in self.P_best])
        self.G_best = self.P_best[G_best_index]

    def classic_velocity_update(self, i):
        """
        Updates the velocity of a particle using the classical velocity update formula.
        """
        r1, r2 = np.random.uniform(), np.random.uniform()
        self.V[i] = self.w * self.V[i] + self.c1 * r1 * (self.P_best[i] - self.P[i]) + self.c2 * r2 * (self.G_best - self.P[i])

    def general_velocity_update(self, i):
        """
        Updates the velocity of a particle using a more general velocity update formula.
        """
        r1, r2 = np.random.uniform(), np.random.uniform()
        self.V[i] = self.w * (self.V[i] + self.c1 * r1 * (self.P_best[i] - self.P[i])) + self.c2 * r2 * (self.G_best - self.P[i])

    def run(self):
        """
        Runs the Particle Swarm Optimization algorithm.
        """
        t = 0
        self.initialize()

        while not self.termination_condition(t):
            for i in range(self.n):
                # Update the velocity of each particle
                if self.model == "general":
                	self.general_velocity_update(i)
                elif self.model == "classic":
	                self.classic_velocity_update(i)
                # Update the position of each particle
                self.P[i] += self.V[i]
                # Update the personal best of each particle
                if self.f(self.P[i]) < self.f(self.P_best[i]):
                    self.P_best[i] = self.P[i]
                # Update the global best
                if self.f(self.P[i]) < self.f(self.G_best):
                    self.G_best = self.P[i]

            t += 1

        return self.G_best

def example():
	# Define the objective function to minimize
	def objective_function(x):
	    return x[0]**2 - x[0] + x[1]**2 - x[1]

	# Define the termination condition
	def termination_condition(t):
	    return t >= 100  # Stop after 100 iterations

	# Initialize PSO with 30 particles, 2 dimensions, weights, and coefficients
	pso = ParticleSwarmOptimization(
	    n=30, d=2, w=0.5, c1=1.5, c2=1.5,
	    termination_condition=termination_condition, f=objective_function
	)

	# Run the PSO algorithm
	best_position = pso.run()
	result = objective_function(best_position)
	print("The best position is: ", best_position)
	print("The result is: ", result)


if __name__ == '__main__':
	example()
	
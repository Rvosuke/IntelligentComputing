import random


def main():
	generation_number = 0
	
	# Sample NP points from the search space to form the initial population
	num_population = 10
	population = initial_population(num_population, search_space)
	
	while True:
		# Evaluate the objective function at each population point
		for i in range(num_population):
			mutant_vector = mutation_DE(population, i)
			trial_vector = crossover_DE(population, i, mutant_vector)
			population = selection_DE(population, i, trial_vector)

		# if a preset stopping condition is met, stop the search
		if stopping_condition(generation_number):
			break
		else:
			generation_number += 1

	return population


def mutation_DE(population, index, num_population, scale_factor):
	base_vector = population[index]
	best_vector = best_individual(population)
	F = scale_factor
	# Select five random indexes from the num_population
	random_indexes = random.sample(range(num_population), 5)
	rand_1 = population[random_indexes[0]] + F * (population[random_indexes[1]] - population[random_indexes[2]])
	rand_2 = population[random_indexes[0]] + F * (population[random_indexes[1]] - population[random_indexes[2]]) + F * (population[random_indexes[3]] - population[random_indexes[4]])

	best_1 = best_vector + F * (population[random_indexes[1]] - population[random_indexes[2]])
	best_2 = best_vector + F * (population[random_indexes[1]] - population[random_indexes[2]]) + F * (population[random_indexes[3]] - population[random_indexes[4]])

	current2best_1 = base_vector + F * (best_vector - base_vector) + F * (population[random_indexes[3]] - population[random_indexes[4]])
	current2rand_1 = base_vector + F * (population[random_indexes[1]] - base_vector) + F * (population[random_indexes[3]] - population[random_indexes[4]])

	return random.choice([rand_1, rand_2, best_1, best_2, current2best_1, current2rand_1])


def crossover_binomial(population, index, mutant_vector, control_parameter):
	target_vector = population[index]
	trial_vector = []
	for i in range(len(target_vector)):
		if random.random() <= control_parameter:
			trial_vector.append(mutant_vector[i])
		else:
			trial_vector.append(target_vector[i])
	return trial_vector
	

def crossover_exponential(population, index, mutant_vector, control_parameter):
	# I didnt implement this yet
	target_vector = population[index]
	trial_vector = []
	for i in range(len(target_vector)):
		P = control_parameter ** (v-1) * (1-CR)
		if P >= 0.5:
			trial_vector.append(mutant_vector[i])
		else:
			trial_vector.append(target_vector[i])
	return trial_vector


def selection_DE(population, index, trial_vector):
	if objective_function(trial_vector) < objective_function(population[index]):
		return trial_vector
	else:
		return population[index]


def initial_population(num_population, search_space):
	population = []
	for i in range(num_population):
		population.append(random.sample(search_space, len(search_space)))
	return population


def stopping_condition(generation_number):
	if generation_number == 100:
		return True
	else:
		return False

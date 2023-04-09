import random
import numpy as np
from PIL import Image, ImageDraw


def load_target_image(image_path):
    target_image = Image.open(image_path).convert('RGBA')
    target_image = np.array(target_image).astype(np.float32) / 255.0
    return target_image


def roulette_wheel_selection(population, fitnesses):
    total_fitness = np.sum(fitnesses)
    rel_fitnesses = fitnesses / total_fitness
    index = np.searchsorted(np.cumsum(rel_fitnesses), random.random())
    return population[index]


def tournament_selection(population, fitnesses, tournament_size=5):
    tournament = random.sample(population, tournament_size)
    tournament_fitnesses = [fitnesses[population.index(individual)] for individual in tournament]
    best_individual = tournament[np.argmax(tournament_fitnesses)]
    return best_individual


def save_and_display_image(image, save_path):
    image_uint8 = (image * 255).astype(np.uint8)
    image = Image.fromarray(np.uint8(image_uint8))
    image.save(save_path)
    image.show()


class GeneticAlgorithm:
    def __init__(self, image_path, num_triangles=100, population_size=20, num_generations=100, mutation_rate=0.1,
                 crossover_rate=0.8):
        self.image_path = image_path
        self.target_image = load_target_image(image_path)
        self.num_triangles = num_triangles
        self.population_size = population_size
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.image_width = self.target_image.shape[1]
        self.image_height = self.target_image.shape[0]
        self.mutation_scale = np.sqrt(2) / np.sqrt(2 * np.sqrt(self.num_triangles))
        self.current_population = self.initialize_population()
        self.best_fitness = float('-inf')
        self.best_individual = None
        self.current_generation = 0

    def initialize_population(self):
        population = []
        for i in range(self.population_size):
            individual = self.create_individual()
            population.append(individual)
        return population

    def create_individual(self):
        individual = []
        for i in range(self.num_triangles):
            vertices = [(np.random.randint(0, self.image_width), np.random.randint(0, self.image_height)) for _ in
                        range(3)]
            color = tuple(np.random.uniform(0, 1, 4))
            individual.append(tuple(vertices) + color)  # 修改此行，将 vertices 转换为元组
        return individual

    def render_individual(self, individual):
        image = Image.new('RGBA', (self.image_width, self.image_height), (255, 255, 255, 0))
        for triangle in individual:
            vertices, color = triangle[:-4], tuple(int(c * 255) for c in triangle[-4:])
            draw = ImageDraw.Draw(image, 'RGBA')
            draw.polygon(vertices, fill=color)
        image = np.array(image).astype(np.float32) / 255.0
        image[:, :, 3] = np.clip(image[:, :, 3], 0, 1)  # 修复透明度通道
        return image

    def fitness(self, individual):
        rendered_image = self.render_individual(individual)
        difference = np.mean(np.abs(rendered_image - self.target_image))
        fitness = -difference
        return fitness

    def adaptive_crossover_rate(self):
        if self.current_generation < self.num_generations / 4:
            return self.crossover_rate
        elif self.current_generation < self.num_generations / 2:
            return self.crossover_rate / 2
        else:
            return self.crossover_rate / 4

    def crossover(self, parent1, parent2):
        child1, child2 = [], []
        for i in range(self.num_triangles):
            if random.random() < self.adaptive_crossover_rate():
                child1.append(parent1[i])
                child2.append(parent2[i])
            else:
                child1.append(parent2[i])
                child2.append(parent1[i])
        return child1, child2

    def mutation(self, individual):
        mutated_individual = []
        for i in range(self.num_triangles):
            if random.random() < self.mutation_rate:
                vertices, color = individual[i][:-4], individual[i][-4:]
                new_vertices = [(int(max(0, min(self.image_width - 1, v[0] + random.gauss(0, self.mutation_scale)))),
                                 int(max(0, min(self.image_height - 1, v[1] + random.gauss(0, self.mutation_scale)))))
                                for v in vertices]
                new_color = tuple(
                    max(0, min(255, int(c * 255 + random.gauss(0, self.mutation_scale))) / 255.0) for c in color)
                mutated_individual.append(tuple(new_vertices) + new_color)  # 修改此行，将 new_vertices 转换为元组
            else:
                mutated_individual.append(individual[i])
        return mutated_individual

    def evolve(self):
        for generation in range(self.num_generations):
            self.current_generation = generation
            fitnesses = [self.fitness(individual) for individual in self.current_population]
            max_fitness = max(fitnesses)
            if max_fitness > self.best_fitness:
                self.best_fitness = max_fitness
                self.best_individual = self.current_population[np.argmax(fitnesses)]
            print(f'Generation {generation}: Best fitness = {self.best_fitness:.4f}')
            next_population = []
            for i in range(self.population_size // 2):
                parent1 = tournament_selection(self.current_population, fitnesses)
                parent2 = tournament_selection(self.current_population, fitnesses)
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutation(child1)
                child2 = self.mutation(child2)
                next_population.extend([child1, child2])
            self.current_population = next_population


if __name__ == '__main__':
    ga = GeneticAlgorithm(image_path='chrome.png', num_triangles=128, population_size=20, num_generations=100,
                          mutation_rate=0.3, crossover_rate=0.8)
    ga.evolve()
    final_image = ga.render_individual(ga.best_individual)
    save_and_display_image(final_image, 'chrome_fit.png')

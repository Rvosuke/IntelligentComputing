import numpy as np
import random
# import cv2
from PIL import Image, ImageDraw

# Parameters
population_size = 20
num_triangles = 128
mutation_rate = 0.1
crossover_rate = 0.8
num_generations = 100


def load_target_image(image_path):
    # Load the target image from the specified path
    target_image = Image.open(image_path)

    # Convert the target image to RGBA if needed
    if target_image.mode != 'RGBA':
        target_image = target_image.convert('RGBA')

    # Convert the target image to ndarray
    target_image = np.array(target_image)

    # Convert the target image to floating point representation in the range [0, 1]
    target_image = target_image.astype(np.float32) / 255.0

    return target_image


# def create_individual(num_triangles, image_width, image_height):
#     """Create a random individual (chromosome)"""
#     # Each triangle has 3 vertices (6 coordinates) and 4 color values (RGBA)
#     individual = []
#
#     for i in range(num_triangles):
#         # Generate random triangle vertices
#         for j in range(3):
#             x = int(np.random.uniform(0, image_width + 1))
#             y = int(np.random.uniform(0, image_height + 1))
#             individual.extend([x, y])
#
#         # Generate random color values (RGBA)
#         r = random.random()
#         g = random.random()
#         b = random.random()
#         a = random.random()
#         individual.extend([r, g, b, a])
#
#     return individual
#     # return [random.random() for _ in range(9 * num_triangles)]
# def create_individual(num_triangles, image_width, image_height, target_image):
#     """Create a random individual (chromosome)"""
#     # Each triangle has 3 vertices (6 coordinates) and 4 color values (RGBA)
#     individual = []
#
#     for i in range(num_triangles):
#         # Generate random triangle vertices
#         for j in range(3):
#             x = int(np.random.uniform(0, image_width + 1))
#             y = int(np.random.uniform(0, image_height + 1))
#             individual.extend([x, y])
#
#         # Generate random color values (RGBA) based on the target_image
#         x = random.randint(0, image_width - 1)
#         y = random.randint(0, image_height - 1)
#         r, g, b, a = target_image[y, x, :]
#
#         individual.extend([r, g, b, a])
#
#     return individual
def create_individual(num_triangles, image_width, image_height, target_image):
    """Create a random individual (chromosome)"""
    # Each triangle has 3 vertices (6 coordinates) and 4 color values (RGBA)
    individual = []

    for i in range(num_triangles):
        # Generate random triangle vertices
        for j in range(3):
            x = int(np.random.uniform(0, image_width + 1))
            y = int(np.random.uniform(0, image_height + 1))
            individual.extend([x, y])

        # Ensure the three vertices are different to form a triangle
        while (individual[-6:-4] == individual[-4:-2]) or (individual[-6:-4] == individual[-2:]) or (individual[-4:-2] == individual[-2:]):
            individual[-2] = int(np.random.uniform(0, image_width + 1))
            individual[-1] = int(np.random.uniform(0, image_height + 1))

        # Generate random color values (RGBA) based on the target_image
        x = random.randint(0, image_width - 1)
        y = random.randint(0, image_height - 1)
        r, g, b, a = target_image[y, x, :]

        individual.extend([r, g, b, a])

    return individual


def initialize_population(population_size, num_triangles, image_width, image_height, target_image):
    # Initialize the population
    return [create_individual(num_triangles, image_width, image_height, target_image) for _ in range(population_size)]


def clip_point(point, width, height):
    """检查和修正顶点坐标是否在画布范围内"""
    x, y = point
    x = max(min(x, width), 0)
    y = max(min(y, height), 0)
    return x, y


def render_triangles(individual, width, height):
    # Create a blank image with a white background
    image = Image.new('RGBA', (width, height), (255, 255, 255, 0))

    for i in range(int(len(individual)/10)):
        # Extract the triangle's vertices and color (RGBA) values from the individual
        x1, y1 = clip_point((individual[i * 10 + 0], individual[i * 10 + 1]), width, height)
        x2, y2 = clip_point((individual[i * 10 + 2], individual[i * 10 + 3]), width, height)
        x3, y3 = clip_point((individual[i * 10 + 4], individual[i * 10 + 5]), width, height)
        r, g, b, a = [int(value * 255) for value in individual[i * 10 + 6:i * 10 + 10]]

        # Draw the triangle on the image
        triangle = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(triangle, 'RGBA')
        draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=(r, g, b, a))

        # Overlay the triangle onto the main image
        image = Image.alpha_composite(image, triangle)
    image = np.array(image).astype(np.float32) / 255.0
    return image


def fitness(individual, target_image):
    # Render the triangles from the individual
    rendered_image = render_triangles(individual, target_image.shape[1], target_image.shape[0])

    # Compute the difference between the rendered image and target image
    difference = np.mean(np.abs(rendered_image - target_image))

    # Define fitness as the negative difference (higher fitness means smaller difference)
    return -difference


def selection(population, fitnesses):
    # Calculate the total fitness
    total_fitness = sum(fitnesses)

    # Calculate the relative fitness for each individual
    relative_fitnesses = [fitness / total_fitness for fitness in fitnesses]

    # Generate a random number in the range [0, 1)
    r = random.random()

    # Choose a parent using roulette wheel selection
    cumulative_sum = 0
    for index, rel_fitness in enumerate(relative_fitnesses):
        cumulative_sum += rel_fitness
        if r <= cumulative_sum:
            return population[index]

    # If the above loop does not return, return the last individual
    return population[-1]


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1))

    # Perform single-point crossover
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2


def mutation(individual, mutation_rate, mutation_scale):
    mutated_individual = []

    for gene in individual:
        # Check if mutation should be applied
        if random.random() < mutation_rate:
            # Apply Gaussian mutation
            mutated_gene = gene + random.gauss(0, mutation_scale)

            # Make sure the mutated gene is within the valid range [0, 1]
            mutated_gene = min(max(mutated_gene, 0), 1)
        else:
            # If no mutation, keep the original gene
            mutated_gene = gene

        mutated_individual.append(mutated_gene)

    return mutated_individual


def save_and_display_image(final_image, save_path):
    # Convert the image back to the range [0, 255] and convert to uint8
    final_image_uint8 = (final_image * 255).astype(np.uint8)
    final_image = Image.fromarray(np.uint8(final_image_uint8))
    # Save the final image to the specified path
    final_image.save(save_path)

    # Display the final image
    final_image.show()


def main():
    # Load the target image
    image_path = 'chrome.png'
    target_image = load_target_image(image_path)

    # Initialize the population
    population_size = 20
    num_triangles = 128
    image_width = target_image.shape[1]
    image_height = target_image.shape[0]

    population = initialize_population(population_size, num_triangles, image_width, image_height, target_image)

    # Define GA parameters
    generations = 50
    mutation_rate = 0.3
    mutation_scale = 0.05

    # Run the genetic algorithm
    for generation in range(generations):
        # Evaluate the fitness of each individual in the population
        fitnesses = [fitness(individual, target_image) for individual in population]

        # Select parents and perform crossover and mutation to create offspring
        offspring = []
        for _ in range(population_size // 2):
            parent1 = selection(population, fitnesses)
            parent2 = selection(population, fitnesses)

            child1, child2 = crossover(parent1, parent2)
            child1 = mutation(child1, mutation_rate, mutation_scale)
            child2 = mutation(child2, mutation_rate, mutation_scale)

            offspring.append(child1)
            offspring.append(child2)

        # Replace the old population with the offspring
        population = offspring

    # Find the best individual in the final population
    best_individual = max(population, key=lambda x: fitness(x, target_image))

    # Render the final image from the best individual
    final_image = render_triangles(best_individual, image_width, image_height)

    # Save and display the final image
    save_path = 'chromeFit.png'
    save_and_display_image(final_image, save_path)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print('Running time：', end - start, 's')

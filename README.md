

# Genetic Algorithm for Image Approximation

This Python script utilizes a genetic algorithm to approximate a target image using semi-transparent triangles. It creates a series of images that evolve over time, representing the progress of the algorithm in finding a close approximation of the target image.

## Overview

The genetic algorithm works as follows:

1. A population of individuals is created, each consisting of a collection of semi-transparent triangles.
2. Each individual's fitness is evaluated based on the difference between its pixel values and those of the target image.
3. The individuals in the population are selected for reproduction based on their fitness.
4. The offspring are created through crossover (swapping triangles between two parents) and mutation (randomly altering the properties of a triangle).
5. The new generation replaces the old one, and the process repeats until a satisfactory approximation is reached or a specified number of generations have elapsed.

## Requirements

- Python 3.6 or later
- PIL (Python Imaging Library)

## Usage

1. Ensure you have the required libraries installed:

```python
pip install pillow
```

1. Set the `target_image_path` variable in the script to the path of your target image.
2. Adjust the following parameters as needed:
   - `triangle_count`: The number of triangles per individual.
   - `population_size`: The size of the population.
   - `generations`: The number of generations to run the algorithm for.
   - `crossover_rate`: The probability of crossover between two parents.
   - `mutation_rate`: The probability of a triangle undergoing mutation.
3. Run the script:

```python
python genetic_image_approximation.py
```

1. The output images will be saved to the `output` directory. The script saves an image at every `save_interval` generations to visualize the progress of the algorithm.

## Example

The following example demonstrates how to use the script with a custom target image, a population size of 20, a triangle count of 128, and a total of 2000 generations:

```python
pythonCopy codetarget_image_path = "path/to/your/target/image.png"
triangle_count = 128
population_size = 20
output_dir = "output"
save_interval = 100

approximator = ImageApproximator(target_image_path, triangle_count, population_size, output_dir, save_interval)
generations = 2000
crossover_rate = 0.7
mutation_rate = 0.1
approximator.evolve(generations, crossover_rate, mutation_rate)
```

Adjust the parameters as needed to achieve the desired level of approximation.

# Genetic Algorithm for Image Fitting

This repository contains a Python implementation of a Genetic Algorithm (GA) for fitting an image using a collection of triangles. The goal of this project is to approximate a target image (e.g., Google Chrome logo) using a set of triangles with different vertices, colors, and transparency levels.

## Dependencies

- Python 3.6+
- NumPy
- Pillow (Python Imaging Library)

## Usage

1. Clone the repository:

```
bashCopy codegit clone https://github.com/yourusername/genetic-image-fitting.git
cd genetic-image-fitting
```

1. Modify the `main()` function in `ga_image_fitting.py` to set your desired parameters and the path to the target image.
2. Run the script:

```
bashCopy code
python ga_image_fitting.py
```

1. The script will evolve the population and save the final image approximating the target image.

## Overview

The Genetic Algorithm follows these main steps:

1. **Encoding**: Each individual (chromosome) is represented as a list of triangle vertices' coordinates and color values (RGBA).
2. **Initialization**: Generate an initial population of random individuals.
3. **Fitness evaluation**: Compute the fitness of each individual by rendering the triangles and calculating the difference between the rendered image and the target image.
4. **Selection**: Choose parents from the population using roulette wheel selection.
5. **Crossover**: Perform single-point or multi-point crossover between selected parents to generate offspring.
6. **Mutation**: Apply mutation to the offspring's genes with a certain probability.
7. **Evolution**: Repeat the selection, crossover, and mutation process until a stopping condition is met (e.g., a maximum number of generations).

The implementation uses the Python Imaging Library (PIL) to load, convert, and display images. The fitness evaluation compares the rendered image (as PIL Image) with the target image (as a NumPy array).

## Contributing

Contributions to improve the algorithm, optimize performance, or enhance the project in any way are welcome. Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License.

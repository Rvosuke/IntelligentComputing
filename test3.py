#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random as r
from PIL import Image, ImageDraw
import numpy as np


class Color:
    def __init__(self):
        self.r = r.randint(0, 255)
        self.g = r.randint(0, 255)
        self.b = r.randint(0, 255)
        self.a = r.randint(95, 115)


class Triangle:
    def __init__(self, size=(255, 255)):
        self.ax, self.ay = r.randint(0, size[0]), r.randint(0, size[1])
        self.bx, self.by = r.randint(0, size[0]), r.randint(0, size[1])
        self.cx, self.cy = r.randint(0, size[0]), r.randint(0, size[1])
        self.color = Color()

    def draw(self, size=(256, 256)):
        img = Image.new('RGBA', size)
        draw = ImageDraw.Draw(img)
        draw.polygon([(self.ax, self.ay),
                      (self.bx, self.by),
                      (self.cx, self.cy)],
                     fill=(self.color.r, self.color.g, self.color.b, self.color.a))
        return img


class ImageApproximator:
    def __init__(self, target_image_path, triangle_count, population_size, output_dir, save_interval):
        self.target_image = Image.open(target_image_path).resize((256, 256)).convert('RGBA')
        self.target_pixels = np.array(self.target_image)
        self.triangle_count = triangle_count
        self.population_size = population_size
        self.output_dir = output_dir
        self.save_interval = save_interval

        self.population = []
        for _ in range(population_size):
            individual = [Triangle() for _ in range(triangle_count)]
            self.population.append(individual)

    def selection(self):
        fitnesses = [self.calculate_fitness(individual) for individual in self.population]
        selected_population = []
        for _ in range(self.population_size):
            candidates = [self.population[i] for i in np.random.choice(len(self.population), 2)]
            winner = min(candidates, key=lambda x: self.calculate_fitness(x))
            selected_population.append(winner)
        return selected_population

    def crossover(self, parent1, parent2):
        crossover_point = r.randint(1, self.triangle_count - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def mutation(self, individual, mutation_rate):
        for i in range(self.triangle_count):
            if r.random() < mutation_rate:
                individual[i] = Triangle()

    def evolve(self, generations, crossover_rate, mutation_rate):
        for gen in range(generations):
            # Selection
            selected_population = self.selection()

            # Crossover
            child_population = []
            for i in range(0, self.population_size, 2):
                parent1, parent2 = selected_population[i], selected_population[i + 1]
                if r.random() < crossover_rate:
                    child1, child2 = self.crossover(parent1, parent2)
                else:
                    child1, child2 = parent1[:], parent2[:]

                    # Mutation
                self.mutation(child1, mutation_rate)
                self.mutation(child2, mutation_rate)

                child_population.extend([child1, child2])

            self.population = child_population

            if gen % self.save_interval == 0:
                self.save_image(gen)

    def calculate_fitness(self, individual):
        img = Image.new('RGBA', (256, 256))
        draw = ImageDraw.Draw(img)
        draw.polygon([(0, 0), (0, 255), (255, 255), (255, 0)], fill=(255, 255, 255, 255))
        for triangle in individual:
            img = Image.alpha_composite(img, triangle.draw())

        diff = np.sum((np.array(img) - self.target_pixels) ** 2)
        return diff

    def save_image(self, gen):
        best_individual = min(self.population, key=lambda x: self.calculate_fitness(x))
        img = Image.new('RGBA', (256, 256))
        draw = ImageDraw.Draw(img)
        draw.polygon([(0, 0), (0, 255), (255, 255), (255, 0)], fill=(255, 255, 255, 255))
        for triangle in best_individual:
            img = Image.alpha_composite(img, triangle.draw())

        img.save(os.path.join(self.output_dir, f"output_{gen}.png"))


if __name__ == '__main__':
    target_image_path = "chrome.png"
    triangle_count = 128
    population_size = 20
    output_dir = "output"
    save_interval = 100
    approximator = ImageApproximator(target_image_path, triangle_count, population_size, output_dir, save_interval)
    generations = 1000
    crossover_rate = 0.7
    mutation_rate = 0.1
    approximator.evolve(generations, crossover_rate, mutation_rate)

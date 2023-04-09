#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import gc
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

    def mutate(self, mutate_rate):
        if r.random() < mutate_rate:
            self.ax, self.ay = r.randint(0, 255), r.randint(0, 255)
            self.bx, self.by = r.randint(0, 255), r.randint(0, 255)
            self.cx, self.cy = r.randint(0, 255), r.randint(0, 255)
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
    def __init__(self, target_image_path, triangle_count, output_dir, save_interval):
        self.target_image = Image.open(target_image_path).resize((256, 256)).convert('RGBA')
        self.target_pixels = [np.array(x) for x in list(self.target_image.split())]
        self.triangle_count = triangle_count
        self.output_dir = output_dir
        self.save_interval = save_interval

        self.population = []
        for _ in range(triangle_count):
            self.population.append(Triangle())

    def evolve(self, generations, mutate_rate):
        for gen in range(generations):
            child_population = []

            # Roulette wheel selection
            fitness_list = [1 / (1 + self.calculate_fitness([triangle])) for triangle in self.population]
            fitness_sum = sum(fitness_list)
            probability_list = [fitness / fitness_sum for fitness in fitness_list]

            # Crossover and mutation
            for _ in range(self.triangle_count):
                parent1, parent2 = np.random.choice(self.population, size=2, replace=False, p=probability_list)
                crossover_point = r.randint(1, len(parent1.__dict__) - 1)
                child_triangle = Triangle()
                child_triangle.__dict__ = {**parent1.__dict__, **parent2.__dict__}
                child_triangle.mutate(mutate_rate)
                child_population.append(child_triangle)

            parent_fitness = self.calculate_fitness(self.population)
            child_fitness = self.calculate_fitness(child_population)

            if child_fitness < parent_fitness:
                self.population = child_population

            if gen % self.save_interval == 0:
                self.save_image(gen)

    def calculate_fitness(self, population):
        img = Image.new('RGBA', (256, 256))
        draw = ImageDraw.Draw(img)
        draw.polygon([(0, 0), (0, 255), (255, 255), (255, 0)], fill=(255, 255, 255, 255))
        for triangle in population:
            img = Image.alpha_composite(img, triangle.draw())

        fitness = 0
        arrs = [np.array(x) for x in list(img.split())]
        for i in range(4):
            fitness += np.sum(np.abs(self.target_pixels[i] - arrs[i]))
        return fitness

    def save_image(self, generation):
        img = Image.new('RGBA', (256, 256))
        draw = ImageDraw.Draw(img)
        draw.polygon([(0, 0), (0, 255), (255, 255), (255, 0)], fill=(255, 255, 255, 255))
        for triangle in self.population:
            img = Image.alpha_composite(img, triangle.draw())

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        img.save(os.path.join(self.output_dir, f"gen_{generation}.png"), "PNG")


if __name__ == '__main__':
    target_image_path = "chrome.png"
    triangle_count = 128
    output_dir = "output"
    save_interval = 100
    generations = 500
    mutate_rate = 0.1
    approximator = ImageApproximator(target_image_path, triangle_count, output_dir, save_interval)
    approximator.evolve(generations, mutate_rate)

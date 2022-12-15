import numpy as np
import math


def normalize(y):
    # Values based on the dataset before normalization
    minimum = 71.969
    maximum = 444.847
    return 1 - (y - minimum)/(maximum - minimum)


def check_violation(threshold, solution):
    # Cereals & Grains
    group1 = [1, 11, 12, 14, 15, 22, 23]
    group1_names = [list(solution.keys())[i] for i in group1]
    values1 = [solution[x] for x in group1_names]
    food_in_group1 = sum(values1) * 100
    idealG1 = 400
    distG1 = food_in_group1 - idealG1

    # Pulses & Vegetables
    group2 = [0, 6, 10, 13]
    group2_names = [list(solution.keys())[i] for i in group2]
    values2 = [solution[x] for x in group2_names]
    food_in_group2 = sum(values2) * 100
    idealG2 = 65
    distG2 = food_in_group2 - idealG2

    # Oils & Fats
    group3 = [21]
    group3_names = [list(solution.keys())[i] for i in group3]
    values3 = [solution[x] for x in group3_names]
    food_in_group3 = sum(values3) * 100
    idealG3 = 27.5
    distG3 = food_in_group3 - idealG3

    # Mixed & Blended Foods
    group4 = [5, 24, 16, 17, 18, 19]
    group4_names = [list(solution.keys())[i] for i in group4]
    values4 = [solution[x] for x in group4_names]
    food_in_group4 = sum(values4) * 100
    idealG4 = 45
    distG4 = food_in_group4 - idealG4

    # Meat & Fish & Dairy
    group5 = [2, 3, 4, 7, 8]
    group5_names = [list(solution.keys())[i] for i in group5]
    values5 = [solution[x] for x in group5_names]
    food_in_group5 = sum(values5) * 100
    idealG5 = 30
    distG5 = food_in_group5 - idealG5

    real_palatability = np.round(math.sqrt(distG1 ** 2 + (5.7 * distG2) ** 2 + (16 * distG3) ** 2
                                           + (4.4 * distG4) ** 2 + (6.6 * distG5) ** 2), 3)
    real_palatability_norm = normalize(real_palatability)
    return 1 - int(real_palatability_norm >= threshold), real_palatability_norm
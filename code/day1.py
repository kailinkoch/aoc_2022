"""

Day 1

"""

import numpy as np

def get_data(input_path):
    """ Calculate the total calories of each elf """ 
    calories_itemized = []
    calories_total = []
    with open(input_path, 'r') as file:
        for line in file:
            if line.strip() == '':
                calories_total.append(np.sum(calories_itemized))
                calories_itemized = []
            else:
                calories_itemized.append(int(line.strip()))           
    return calories_total

def get_max_calories(calories_total):
    """ Find the most calories carried """
    max = np.argmax(calories_total)
    return calories_total[max]

def get_top_3_calories(calories_total):
    """ Find the total calories carried by the top 3 elves """
    sorting = np.sort(calories_total)
    return np.sum(sorting[-3:])

def run_part_one(data):
    max_calories = get_max_calories(data)
    return max_calories

def run_part_two(data):
    top_3 = get_top_3_calories(data)
    return top_3
    

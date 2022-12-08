"""

Day 1

"""

import numpy as np
from argparse import ArgumentParser

parser = ArgumentParser(description='Process some integers.')
parser.add_argument('--input_path', default = 'inputs/day1.txt', help = "path to input file")

def total_calories(input_path):
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

def main(args):
    calories_total = total_calories(args.input_path)
    max_calories = get_max_calories(calories_total)
    top_3 = get_top_3_calories(calories_total)
    print(max_calories, top_3)
    
if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
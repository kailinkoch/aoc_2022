"""

Run any day of advent of code solution

"""

import numpy as np
import code
from argparse import ArgumentParser
import importlib

parser = ArgumentParser()
parser.add_argument('--days', default = '1', help = 'puzzle day or days')

def run_code(input_path, day_num):
    name = 'code.day' + day_num 
    day_code = importlib.import_module(name)
    data = day_code.get_data(input_path)
    part_one = day_code.run_part_one(data)
    part_two = day_code.run_part_two(data)
    return part_one, part_two

def pretty_print(day, results):
    print('-------------------------------')
    print(f'DAY {day} RESULTS')
    print(f'part 1 solution = {results[0]}')
    print(f'part 2 solution = {results[1]}')
    print('-------------------------------')

def main(args):
    days = args.days.split(',')
    for day in days:
        input_path = f'inputs/day{day}.txt'
        results = run_code(input_path, day)
        pretty_print(day,results)

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)

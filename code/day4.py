"""

Day 4

"""

import numpy as np

def get_data(input_path):
    """ Read in data""" 
    with open(input_path, 'r') as file:
        for line in file:
          data = [line.strip().split(',') for line in file]
          data = [[x.split('-') for x in line] for line in data]
          data = [[[int(y) for y in x] for x in line] for line in data]
    return data

def check_inclusivity(person1, person2):
    return (person1[0]>= person2[0] and person1[1]<=person2[1]) or (person2[0]>= person1[0] and person2[1]<=person1[1])
    
def run_part_one(data):
    results = [check_inclusivity(person1,person2) for person1, person2 in data]
    return sum(results)

def run_part_two(data):
    results = 'to be implemented'
    return results



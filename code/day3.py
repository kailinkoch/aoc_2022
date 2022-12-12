  
"""

Day 3

"""

import numpy as np
import string

def get_data(input_path):
    with open(input_path, 'r') as file:
        backpacks = [[line[0:int(len(line)/2)], line[int(len(line)/2):].strip()] for line in file]
    return backpacks

def same_letter(back_pack, group = False):
    same_letter = ''.join(set(back_pack[0]).intersection(back_pack[1]))
    if group:
        back_pack = [pack[0]+pack[1] for pack in back_pack]
        same_letter = ''.join(set(back_pack[0]).intersection(back_pack[1], back_pack[2]))
    return same_letter

def convert_letters_numbers(letter):
    order = list(string.ascii_lowercase + string.ascii_uppercase)
    return order.index(letter)+1

def run_part_one(backpacks):
    letters = [same_letter(pack) for pack in backpacks]
    priorities = [convert_letters_numbers(letter) for letter in letters]
    return sum(priorities)

def run_part_two(backpacks):
    letters_three = [same_letter(backpacks[i:i+3], group=True) for i in range(0, len(backpacks),3)]
    priorities_three =  [convert_letters_numbers(letter) for letter in letters_three]
    return sum(priorities_three)




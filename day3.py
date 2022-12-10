  
"""

Day 3

"""

import numpy as np
import string
from argparse import ArgumentParser

parser = ArgumentParser(description='Process some integers.')
parser.add_argument('--input_path', default = 'inputs/day3.txt', help = "path to input file")

def read_file(input_path):
    with open(input_path, 'r') as file:
        backpacks = [[line[0:len(line)/2], line[len(line)/2:].strip()] for line in file]
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

def main(args):
    backpacks = read_file(args.input_path)
    letters = [same_letter(pack) for pack in backpacks]
    letters_three = [same_letter(backpacks[i:i+3], group=True) for i in range(0, len(backpacks),3)]
    priorities = [convert_letters_numbers(letter) for letter in letters]
    priorities_three =  [convert_letters_numbers(letter) for letter in letters_three]
    print(np.sum(priorities))
    print(np.sum(priorities_three))

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)


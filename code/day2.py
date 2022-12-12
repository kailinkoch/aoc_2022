"""

Day 2

"""

import pandas as pd 

def get_data(input_path):
    data = pd.read_csv(input_path, sep=' ', header=None)
    data.columns = ['opponent', 'me']
    return data

def normalize(data):
    map = {}
    map[1] = ['A', 'X']
    map[2] = ['B','Y']
    map[3] = ['C','Z']
    for key,val in map.items():
        data.replace([v for v in val], key, inplace=True)
    return data

def score_round(opponent_move, my_move):
    pairs = {}
    pairs[1] = 3
    pairs[2] = 1
    pairs[3] = 2

    if pairs[opponent_move] == my_move:
        return 0
    if opponent_move == my_move:
        return 3
    if pairs[my_move] == opponent_move:
        return 6

def score_outcome(opponent_move, outcome):
    losses = {}
    losses[1] = 3
    losses[2] = 1
    losses[3] = 2
    
    wins = {}
    wins[3] = 1
    wins[1] = 2
    wins[2] = 3
    if outcome == 1:
        return losses[opponent_move] + 0
    if outcome == 2:
        return opponent_move + 3
    if outcome == 3: 
        return wins[opponent_move] + 6

def run_part_one(data):
    normalize(data)
    data['score_round_move'] = data.apply(lambda row : score_round(row['opponent'], row['me']), axis=1)
    data['total_part_1'] = data['score_round_move'] + data['me']
    return data['total_part_1'].sum()

def run_part_two(data):
    normalize(data)
    data['score_round_outcome'] = data.apply(lambda row : score_outcome(row['opponent'], row['me']), axis=1)
    data['total_part_2'] = data['score_round_outcome']
    return data['total_part_2'].sum()


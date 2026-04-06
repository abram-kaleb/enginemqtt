# starting_air.py
import random


def get_starting_air_data():
    starting_data = {}

    # 8/1 - 8/3 Anlassluft
    starting_data[157] = round(random.uniform(
        27.0, 30.0), 1)  # 8/1 - Druck v. Motor
    starting_data[158] = random.choice(
        [0, 1])                 # 8/2 - Verdichter 1
    starting_data[159] = random.choice(
        [0, 1])                 # 8/3 - Verdichter 2

    # Sisa kolom (160-166)
    for i in range(160, 167):
        starting_data[i] = 0.0

    return starting_data

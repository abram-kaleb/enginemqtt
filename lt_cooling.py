# lt_cooling.py
import random


def get_lt_cooling_data():
    lt_data = {}

    # 4/1 - 4/6 Temperatures
    # 4/1 - Temp. v. Ladeluftkühler
    lt_data[72] = round(random.uniform(20.0, 22.0), 1)
    # 4/2 - Temp. n. Ladeluftkühler
    lt_data[73] = round(random.uniform(22.0, 24.0), 1)
    # 4/3 - Identical to 4/2
    lt_data[74] = lt_data[73]
    # 4/4 - Temp. n. Schmierölkühler
    lt_data[75] = round(random.uniform(27.0, 30.0), 1)
    # 4/5 - Temp. n. Zylinderkühlwasserkühler
    lt_data[76] = round(random.uniform(38.0, 40.0), 1)
    # 4/6 - Temp. Eintritt warme Seite
    lt_data[77] = lt_data[76]

    # 4/7 - 4/8 Flow & Pressure
    lt_data[78] = round(random.uniform(12.0, 15.0), 1)   # 4/7 - Durchfluß
    lt_data[79] = round(random.uniform(2.0, 3.0), 1)    # 4/8 - Druck

    # 4/9 - 4/10 Pump Status
    # 4/9 - Stand by LT Pumpe
    lt_data[80] = random.choice([0, 1])
    lt_data[81] = random.choice([0, 1])                  # 4/10 - Kühlturmpumpe

    # 4/11 - 4/13 Pressure, Fan, Temp
    # 4/11 - Druck Kühlturmpumpe
    lt_data[82] = round(random.uniform(1.5, 2.2), 1)
    # 4/12 - Gebläse Kühlturm
    lt_data[83] = random.choice([0, 1])
    # 4/13 - Temp. Behälter, kalte Seite
    lt_data[84] = round(random.uniform(20.0, 23.0), 1)

    # 4/14 - 4/15 Brake Water Pumps
    # 4/14 - Bremsenwasser Zulaufpumpe
    lt_data[85] = random.choice([0, 1])
    # 4/15 - Bremsenwasser Ablaufpumpe
    lt_data[86] = random.choice([0, 1])

    return lt_data

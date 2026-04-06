# fuel.py
import random


def get_fuel_data():
    fuel_data = {}

    # 7/1 - 7/5 Kraftstoff MDO
    fuel_data[107] = round(random.uniform(3.4, 3.8),
                           1)   # 7/1 - Druck v. Filter
    # 7/2 - Druck n. Doppelfilter
    fuel_data[108] = round(random.uniform(2.7, 3.1), 1)
    fuel_data[109] = round(random.uniform(40.0, 43.0),
                           1)  # 7/3 - Temp. v. Motor
    fuel_data[110] = round(random.uniform(80.0, 85.0), 1)  # 7/4 - Durchsatz
    fuel_data[111] = round(random.uniform(20.0, 22.0),
                           1)  # 7/5 - Füllstand Tagestank

    # 7/6 - 7/30 Kraftstoff HFO (Sesuai data input: mayoritas 0)
    for i in range(112, 137):
        fuel_data[i] = 0.0

    # 7/31 - 7/50 Kraftstoff Flüssiggas (Sesuai data input: 0)
    for i in range(137, 157):
        fuel_data[i] = 0.0

    return fuel_data

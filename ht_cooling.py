# ht_cooling.py
import random


def get_ht_cooling_data():
    ht_data = {}

    # 3/1 - 3/11 Temperature & Pressure
    ht_data[56] = round(random.uniform(2.5, 3.0), 1)    # 3/1 - Druck v. Motor
    ht_data[57] = round(random.uniform(70.0, 74.0), 1)   # 3/2 - Temp. v. Motor
    ht_data[58] = round(random.uniform(72.0, 75.0),
                        1)   # 3/3 - Temp. n. Zyl. 1
    ht_data[59] = round(random.uniform(73.0, 76.0),
                        1)   # 3/4 - Temp. n. Zyl. 2
    ht_data[60] = round(random.uniform(73.0, 76.0),
                        1)   # 3/5 - Temp. n. Zyl. 3
    ht_data[61] = round(random.uniform(73.0, 76.0),
                        1)   # 3/6 - Temp. n. Zyl. 4
    ht_data[62] = round(random.uniform(72.0, 75.0),
                        1)   # 3/7 - Temp. n. Zyl. 5
    ht_data[63] = round(random.uniform(74.0, 77.0),
                        1)   # 3/8 - Temp. n. Zyl. 6
    ht_data[64] = round(random.uniform(75.0, 78.0), 1)   # 3/9 - Temp. n. Motor
    ht_data[65] = round(random.uniform(75.0, 78.0),
                        1)   # 3/10 - Temp. v. Kühler
    ht_data[66] = round(random.uniform(71.0, 74.0),
                        1)   # 3/11 - Temp. n. Kühler

    # 3/12 - 3/13 Flow & Pressure
    ht_data[67] = round(random.uniform(30.0, 40.0), 1)   # 3/12 - Durchfluß
    ht_data[68] = round(random.uniform(1.8, 2.5), 1)    # 3/13 - Druck

    # 3/14 - 3/15 Pump Status (0/1)
    # 3/14 - Stand by Pumpe
    ht_data[69] = random.choice([0, 1])
    # 3/15 - Druckhaltepumpe
    ht_data[70] = random.choice([0, 1])

    # 3/16 Niveau
    ht_data[71] = round(random.uniform(0.0, 0.5), 2)    # 3/16 - Niveau Ex-Tank

    return ht_data

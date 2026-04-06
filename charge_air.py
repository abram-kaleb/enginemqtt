# charge_air.py
import random


def get_charge_air_data():
    charge_data = {}

    # 6/1 - 6/4 Temperatures & Pressure
    charge_data[100] = round(random.uniform(
        21.0, 24.0), 1)    # 6/1 - Temp. v. ATL
    # 6/2 - Temp. v. Ladeluftkühler
    charge_data[101] = round(random.uniform(70.0, 75.0), 1)
    # 6/3 - Temp. n. Ladeluftkühler
    charge_data[102] = round(random.uniform(33.0, 36.0), 1)
    # 6/4 - Druck n. Ladeluftkühler
    charge_data[103] = round(random.uniform(3.8, 4.2), 1)

    # 6/5 - 6/7 Differential Pressure & Throughput
    # 6/5 - Druckdifferenz Blende
    charge_data[104] = round(random.uniform(12.0, 16.0), 1)
    charge_data[105] = 0.0                                   # 6/6 - Empty
    charge_data[106] = round(random.uniform(
        580.0, 620.0), 1)  # 6/7 - Durchsatz

    return charge_data

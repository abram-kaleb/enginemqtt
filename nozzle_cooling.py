# nozzle_cooling.py
import random


def get_nozzle_cooling_data():
    nozzle_data = {}

    # 9/1 - 9/4 Pressure, Temp, Flow
    # 9/1 - Druck v. Motor
    nozzle_data[160] = 0.0
    # 9/2 - Temp. v. Motor
    nozzle_data[161] = 0.0
    # 9/3 - Temp. n. Motor
    nozzle_data[162] = 0.0
    nozzle_data[163] = 0.0                                 # 9/4 - Durchsatz

    # 9/5 - 9/8 Status & Others
    nozzle_data[164] = random.choice([0, 1])               # 9/5 - Umwälzpumpe
    nozzle_data[165] = random.choice(
        [0, 1])               # 9/6 - Stand by Pumpe
    # 9/7 - Diff-Druck Filter
    nozzle_data[166] = 0.0
    # 9/8 - Niveau Umlauftank
    # Catatan: Karena indeks maksimal data_list adalah 166,
    # pastikan list data di app.py cukup untuk menampung indeks ini.
    nozzle_data[166] = round(random.uniform(0.0, 0.5), 2)

    return nozzle_data

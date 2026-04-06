# lube_oil.py
import random


def get_lube_oil_data():
    lube_data = {}

    # 5/1 - 5/4 Pressure & Temperatures
    lube_data[87] = round(random.uniform(3.2, 3.8),
                          1)    # 5/1 - Druck n. Pumpe
    lube_data[88] = round(random.uniform(68.0, 72.0),
                          1)   # 5/2 - Temp. n. Pumpe
    # 5/3 - Temp. v. Kühler
    lube_data[89] = lube_data[88]
    lube_data[90] = round(random.uniform(58.0, 62.0),
                          1)   # 5/4 - Temp. n. Kühler

    # 5/5 - 5/7 Filters & Motor Entry
    # 5/5 - Differenzdruck Doppelfilter
    lube_data[91] = round(random.uniform(0.3, 0.5), 1)
    # 5/6 - Druck v. Motor/ n. Filter
    lube_data[92] = round(random.uniform(2.8, 3.3), 1)
    lube_data[93] = round(random.uniform(60.0, 63.0),
                          1)   # 5/7 - Temp. v. Motor

    # 5/8 - 5/10 Flow & Status
    lube_data[94] = 0.0                                   # 5/8 - Durchfluß
    # 5/9 - Stand by Pumpe
    lube_data[95] = random.choice([0, 1])
    lube_data[96] = random.choice([0, 1])                 # 5/10 - Separator

    # 5/11 - 5/13 Fine filter, Last bearing, Oil mist
    # 5/11 - Diff-Druck Feinfilter
    lube_data[97] = round(random.uniform(0.2, 0.4), 1)
    # 5/12 - Temp. v. letztem Lager
    lube_data[98] = lube_data[93]
    # 5/13 - Ölnebelkonzentration
    lube_data[99] = 0.0

    return lube_data

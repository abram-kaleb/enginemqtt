# exhaust.py
import random


def get_exhaust_data():
    extra_data = {}

    # 2/1 - 2/6 Abgassystem - Temp. n. Zylinder 1-6
    extra_data[22] = round(random.uniform(130.0, 545.0),
                           1)  # Temp. n. Zylinder 1
    extra_data[23] = round(random.uniform(320.0, 335.0),
                           1)  # Temp. n. Zylinder 2
    extra_data[24] = round(random.uniform(300.0, 310.0),
                           1)  # Temp. n. Zylinder 3
    extra_data[25] = round(random.uniform(315.0, 325.0),
                           1)  # Temp. n. Zylinder 4
    extra_data[26] = round(random.uniform(310.0, 325.0),
                           1)  # Temp. n. Zylinder 5
    extra_data[27] = round(random.uniform(300.0, 315.0),
                           1)  # Temp. n. Zylinder 6

    extra_data[28] = round(random.uniform(
        410.0, 425.0), 1)  # 2/7 - Temp. v. ATL
    extra_data[29] = round(random.uniform(
        360.0, 375.0), 1)  # 2/8 - Temp. n. ATL
    extra_data[30] = round(random.uniform(0.1, 0.5),
                           2)      # 2/9 - Druck v. ATL
    extra_data[31] = round(random.uniform(0.05, 0.15),
                           3)    # 2/10 - Druck n. ATL
    extra_data[32] = round(random.uniform(
        18000.0, 19000.0), 1)  # 2/11 - Drehzahl ATL
    # 2/12 - Temp. vor Schalldämpfer
    extra_data[33] = round(random.uniform(320.0, 335.0), 1)
    # 2/13 - Abgastemperaturdifferenz
    extra_data[34] = round(random.uniform(330.0, 340.0), 1)

    # 2/14 - 2/22 (Druck 1-4, Temp 1-4, Placeholder)
    for i in range(35, 44):
        extra_data[i] = 0.0

    extra_data[44] = 0.0  # 2/23 - Konz 1
    extra_data[45] = 0.0  # 2/24 - Konz 2

    # 2/25 - 2/34 Mobil 1-10
    extra_data[46] = round(random.uniform(10.0, 15.0), 1)   # Mobil 1
    extra_data[47] = round(random.uniform(5.0, 6.0), 1)     # Mobil 2
    extra_data[48] = round(random.uniform(85.0, 90.0), 1)    # Mobil 3
    extra_data[49] = round(random.uniform(7.0, 8.5), 1)     # Mobil 4
    extra_data[50] = round(random.uniform(55.0, 60.0), 1)    # Mobil 5
    extra_data[51] = round(random.uniform(50.0, 58.0), 1)    # Mobil 6
    extra_data[52] = round(random.uniform(2.0, 3.5), 1)     # Mobil 7
    extra_data[53] = round(random.uniform(960.0, 980.0), 1)  # Mobil 8
    extra_data[54] = round(random.uniform(0.3, 0.5), 2)     # Mobil 9
    extra_data[55] = round(random.uniform(55.0, 65.0), 1)    # Mobil 10

    # Isi sisa kolom sampai 166 dengan 0 agar tidak None
    for i in range(56, 167):
        extra_data[i] = 0.0

    return extra_data

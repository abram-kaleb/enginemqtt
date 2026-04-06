# engine.py
import random
from datetime import datetime


def get_engine_sim():
    # Menginisialisasi list dengan 167 elemen (0-166)
    data = [0.0] * 167

    # 1/1 - 1/4 Status & Control
    # 1/1 - Fahrhebel Drehzahl
    data[1] = 0.0
    # 1/2 - Fahrhebel Bremslast
    data[2] = 0.0
    # 1/3 - Stopp/Betrieb
    data[3] = 1
    # 1/4 - Umschalter Pult/Maschine
    data[4] = random.choice([0, 1])

    # 1/5 - 1/6 DateTime
    now = datetime.now()
    data[5] = int(now.strftime("%Y%m%d"))              # 1/5 - Datum (YYYYMMDD)
    data[6] = int(now.strftime("%H%M%S"))              # 1/6 - Uhrzeit (HHMMSS)

    # 1/7 - 1/10 Performance
    data[7] = 490.0                                    # 1/7 - Betriebsstunden
    data[8] = round(random.uniform(800, 801),
                    1)       # 1/8 - Drehzahl Motor
    # 1/9 - Bremsleistung
    data[9] = round(random.uniform(800.0, 1000.0), 1)
    data[10] = round(random.uniform(9.0, 10.0), 1)     # 1/10 - Füllung Motor

    # 1/11 - 1/16 Pressures
    data[11] = round(random.uniform(25.0, 26.0), 1)    # 1/11 - Anlaßluftdruck
    data[12] = round(random.uniform(3.0, 4.0), 1)      # 1/12 - Schmieröldruck
    data[13] = round(random.uniform(2.5, 3.5), 1)      # 1/13 - Kraftstoffdruck
    # 1/14 - LT Kühlwasserdruck
    data[14] = round(random.uniform(0.1, 0.3), 1)
    # 1/15 - HT Kühlwasserdruck
    data[15] = round(random.uniform(0.1, 0.3), 1)
    data[16] = 0.0                                     # 1/16 - Ladeluftdruck

    # 1/17 - 1/19 Ambient
    data[17] = round(random.uniform(1010.0, 1020.0),
                     2)  # 1/17 - Druck Maschinenraum
    # 1/18 - Temp. Maschinenraum
    data[18] = round(random.uniform(19.0, 22.0), 1)
    # 1/19 - Rel. Luftfeuchte
    data[19] = round(random.uniform(50.0, 60.0), 1)

    # 1/20 - 1/21 Emergency & Counter
    data[20] = 0                                       # 1/20 - Not-Aus-Taster
    data[21] = 29.3                                    # 1/21 - Startzähler

    return data

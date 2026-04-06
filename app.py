import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime
from engine import get_engine_sim
from exhaust import get_exhaust_data
from ht_cooling import get_ht_cooling_data
from lt_cooling import get_lt_cooling_data
from lube_oil import get_lube_oil_data
from charge_air import get_charge_air_data
from fuel import get_fuel_data
from starting_air import get_starting_air_data
from nozzle_cooling import get_nozzle_cooling_data


def start_streaming():
    # Konfigurasi MQTT
    mqtt_broker = "127.0.0.1"
    mqtt_port = 1883
    mqtt_topic = "engine/simulation/data"

    client = mqtt.Client()

    try:
        client.connect(mqtt_broker, mqtt_port, 60)
        client.loop_start()
        print(f"Streaming ke MQTT ({mqtt_broker}:{mqtt_port}) dimulai...")

        while True:
            # Ambil data dasar
            data_list = list(get_engine_sim())

            # List fungsi modul tambahan
            modules = [
                get_exhaust_data,
                get_ht_cooling_data,
                get_lt_cooling_data,
                get_lube_oil_data,
                get_charge_air_data,
                get_fuel_data,
                get_starting_air_data,
                get_nozzle_cooling_data
            ]

            # Update data_list dengan data dari modul-modul
            for module_func in modules:
                extra_data = module_func()
                for idx, value in extra_data.items():
                    if idx < len(data_list):
                        data_list[idx] = value

            # Bungkus data ke format JSON untuk dikirim via MQTT
            payload = {
                "timestamp": datetime.now().isoformat(),
                "values": data_list
            }

            client.publish(mqtt_topic, json.dumps(payload))

            print(
                f"[{datetime.now().strftime('%H:%M:%S')}] Data terkirim ke topik: {mqtt_topic}")
            time.sleep(1)

    except Exception as error:
        print(f"Error: {error}")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    start_streaming()

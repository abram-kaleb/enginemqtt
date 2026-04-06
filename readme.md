# Engine Digital Twin Simulation

Proyek ini adalah simulasi Digital Twin untuk mesin industri/kapal yang menghasilkan data operasional real-time. Sistem ini mensimulasikan berbagai subsistem mesin dan mengirimkan data tersebut ke broker MQTT dalam format JSON.

## Fitur Utama

- **Simulasi Parameter Mesin**: Mensimulasikan lebih dari 160 parameter mesin termasuk tekanan, suhu, dan metrik performa.
- **Modularitas**: Terdiri dari berbagai modul khusus untuk setiap sistem mesin (Pendingin, Pelumas, Bahan Bakar, dll).
- **Streaming MQTT**: Mengirimkan data secara real-time ke broker MQTT untuk integrasi dengan dashboard atau sistem analisis data.
- **Data Dinamis**: Menggunakan generator nilai acak yang realistis untuk mensimulasikan kondisi operasional yang berubah-ubah.

## Struktur Proyek

- `app.py`: Titik masuk utama aplikasi yang mengelola koneksi MQTT dan loop simulasi.
- `engine.py`: Simulasi data dasar, status kontrol, dan performa mesin.
- `exhaust.py`: Data sistem gas buang.
- `ht_cooling.py` & `lt_cooling.py`: Data sistem pendingin (High Temperature & Low Temperature).
- `lube_oil.py`: Data sistem minyak pelumas.
- `fuel.py`: Data sistem bahan bakar.
- `charge_air.py`: Data sistem udara masuk.
- `starting_air.py`: Data sistem udara start.
- `nozzle_cooling.py`: Data sistem pendingin nozzle.

## Prasyarat

- Python 3.x
- Broker MQTT (misalnya Mosquitto) yang berjalan secara lokal atau remote.
- Library `paho-mqtt`:
  ```bash
  pip install paho-mqtt
  ```

## Cara Penggunaan

1. Pastikan broker MQTT Anda sudah aktif (default: `localhost:1883`).
2. Jalankan simulasi dengan perintah:
   ```bash
   python app.py
   ```
   atau menggunakan file batch:
   ```bash
   run.bat
   ```
3. Simulasi akan mulai mengirimkan data ke topik MQTT: `engine/simulation/data`.

## Format Data

Data dikirim dalam format JSON dengan struktur sebagai berikut:
```json
{
  "timestamp": "2026-04-06T12:00:00.000000",
  "values": [0.0, 1.2, 45.5, ...]
}
```
`values` berisi array elemen yang dipetakan ke parameter mesin spesifik (misalnya indeks 8 untuk RPM, indeks 12 untuk tekanan oli, dll).

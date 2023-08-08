# nomor-scraper

Script ini bertujuan untuk mengekstrak data dari web [nomor.net](https://nomor.net), dalam hal ini adalah kode wilayah di seluruh Indonesia (6 digit pertama dalam NIK).

Requirements:
- Python 3
- Google Chrome versi 115 ke atas

Steps:
- buat virtual env untuk Python (misal, nomor-env) `python -m venv nomor-env`
- aktifkan virtual environment `source nomor-env/bin/activate` (Linux)
- install packages yang dibutuhkan `pip install -r requirements.txt`
- jalankan script `python3 app.py`

Data yang sudah diekstrak ada di `data.csv`
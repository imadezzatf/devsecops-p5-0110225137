# Task Manager CLI

![DevSecOps Pipeline](https://github.com/imadezzatf/devsecops-p5-0110225137/actions/workflows/devsecops.yml/badge.svg)

## 1. Nama Aplikasi dan Fungsinya

**Task Manager CLI** adalah aplikasi manajemen tugas berbasis command line.
Pengguna dapat menambah tugas dengan tingkat prioritas (low, medium, high),
melihat daftar tugas, menandai tugas selesai, menghapus tugas, dan melihat
statistik progres. Data disimpan secara lokal dalam file JSON.

Aplikasi ini dibuat untuk tugas mata kuliah DevSecOps Pertemuan 5
(Integrasi SAST dalam CI/CD Pipeline dengan GitHub Actions).

## 2. Bahasa dan Framework

- Bahasa: Python 3.11+
- Library: hanya standard library (argparse, json, dataclasses)
- Testing: pytest

## 3. Cara Menjalankan

```bash
# 1. Clone repository
git clone https://github.com/imadezzatf/devsecops-p5-0110225137.git
cd devsecops-p5-0110225137

# 2. Buat virtual environment dan install dependencies
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt

# 3. Jalankan aplikasi
python -m src.main add "Belajar DevSecOps" -p high
python -m src.main list
python -m src.main done 1
python -m src.main stats
python -m src.main delete 1

# 4. Jalankan unit test
python -m pytest tests/ -v
```

## 4. Overview Pipeline CI/CD

Pipeline didefinisikan di `.github/workflows/devsecops.yml` menggunakan
GitHub Actions.

**Trigger:** push ke branch `main` dan pull request ke branch `main`.

| Job | Fungsi |
|-----|--------|
| `build` | Install dependencies dan menjalankan unit test (pytest) |
| `sast-scan` | Menjalankan SAST menggunakan Bandit. Berjalan setelah `build` sukses (`needs: build`) |

Runner yang digunakan: `ubuntu-latest`.
Jika Bandit menemukan kerentanan, job `sast-scan` gagal sehingga berfungsi
sebagai Quality Gate sederhana.

## Struktur Project

```
.
├── .github/workflows/devsecops.yml
├── src/
│   ├── main.py       # entry point CLI
│   ├── models.py     # class Task
│   ├── storage.py    # baca/tulis JSON
│   ├── stats.py      # statistik tugas
│   └── utils.py      # validasi dan format
├── tests/test_app.py
├── requirements.txt
└── README.md
```

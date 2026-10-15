"""Penyimpanan dan pembacaan tugas dari file JSON."""
import json
import os

from src.models import Task


def load_tasks(path):
    """Membaca daftar tugas. Mengembalikan list kosong jika file belum ada."""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Task.from_dict(item) for item in data]


def save_tasks(tasks, path):
    """Menyimpan daftar tugas ke file JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2, ensure_ascii=False)


def next_id(tasks):
    """Menghasilkan ID berikutnya."""
    if not tasks:
        return 1
    return max(t.id for t in tasks) + 1
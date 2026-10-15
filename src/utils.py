"""Fungsi bantu: validasi dan format tampilan."""

MAX_TITLE_LENGTH = 100


def validate_title(title):
    """Membersihkan dan memvalidasi judul tugas."""
    if title is None:
        raise ValueError("Judul tidak boleh kosong")
    cleaned = title.strip()
    if not cleaned:
        raise ValueError("Judul tidak boleh kosong")
    if len(cleaned) > MAX_TITLE_LENGTH:
        raise ValueError(f"Judul maksimal {MAX_TITLE_LENGTH} karakter")
    return cleaned


def format_task(task):
    """Mengubah Task menjadi teks satu baris."""
    mark = "x" if task.done else " "
    return f"[{mark}] #{task.id} {task.title} ({task.priority})"
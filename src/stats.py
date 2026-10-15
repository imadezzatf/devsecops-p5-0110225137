"""Perhitungan statistik tugas."""
from src.models import PRIORITIES


def summarize(tasks):
    """Meringkas jumlah tugas, progres, dan sebaran prioritas."""
    total = len(tasks)
    done = sum(1 for t in tasks if t.done)
    rate = round(done / total * 100, 1) if total else 0.0
    by_priority = {p: 0 for p in PRIORITIES}
    for t in tasks:
        by_priority[t.priority] += 1
    return {
        "total": total,
        "done": done,
        "pending": total - done,
        "completion_rate": rate,
        "by_priority": by_priority,
    }
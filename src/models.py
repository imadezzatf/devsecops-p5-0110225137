"""Model data untuk aplikasi Task Manager."""
from dataclasses import dataclass, field, asdict
from datetime import datetime

PRIORITIES = ("low", "medium", "high")


@dataclass
class Task:
    id: int
    title: str
    priority: str = "medium"
    done: bool = False
    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )

    def __post_init__(self):
        if self.priority not in PRIORITIES:
            raise ValueError(f"Priority harus salah satu dari {PRIORITIES}")

    def mark_done(self):
        self.done = True

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
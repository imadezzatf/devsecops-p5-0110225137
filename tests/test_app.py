import pytest

from src.models import Task
from src.utils import validate_title, format_task
from src.storage import load_tasks, save_tasks, next_id
from src.stats import summarize


def test_task_default_values():
    t = Task(id=1, title="Belajar")
    assert t.priority == "medium"
    assert t.done is False


def test_task_invalid_priority():
    with pytest.raises(ValueError):
        Task(id=1, title="X", priority="urgent")


def test_mark_done():
    t = Task(id=1, title="X")
    t.mark_done()
    assert t.done is True


def test_validate_title_strips_spaces():
    assert validate_title("  halo  ") == "halo"


def test_validate_title_empty():
    with pytest.raises(ValueError):
        validate_title("   ")


def test_format_task():
    t = Task(id=2, title="Ngoding", priority="high")
    assert format_task(t) == "[ ] #2 Ngoding (high)"


def test_next_id():
    assert next_id([]) == 1
    assert next_id([Task(id=5, title="A")]) == 6


def test_save_and_load(tmp_path):
    path = tmp_path / "tasks.json"
    save_tasks([Task(id=1, title="A"), Task(id=2, title="B")], str(path))
    loaded = load_tasks(str(path))
    assert [t.title for t in loaded] == ["A", "B"]


def test_load_missing_file(tmp_path):
    assert load_tasks(str(tmp_path / "tidak_ada.json")) == []


def test_summarize():
    a = Task(id=1, title="A", priority="high")
    b = Task(id=2, title="B")
    a.mark_done()
    s = summarize([a, b])
    assert s["total"] == 2
    assert s["done"] == 1
    assert s["completion_rate"] == 50.0
    assert s["by_priority"]["high"] == 1
"""Entry point aplikasi Task Manager CLI."""
import argparse

from src.models import Task, PRIORITIES
from src.storage import load_tasks, save_tasks, next_id
from src.utils import validate_title, format_task
from src.stats import summarize

DEFAULT_FILE = "tasks.json"


def build_parser():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    parser.add_argument("--file", default=DEFAULT_FILE, help="File penyimpanan")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="Tambah tugas")
    add.add_argument("title")
    add.add_argument("-p", "--priority", choices=PRIORITIES, default="medium")

    sub.add_parser("list", help="Tampilkan semua tugas")

    done = sub.add_parser("done", help="Tandai tugas selesai")
    done.add_argument("id", type=int)

    delete = sub.add_parser("delete", help="Hapus tugas")
    delete.add_argument("id", type=int)

    sub.add_parser("stats", help="Tampilkan statistik")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    tasks = load_tasks(args.file)

    if args.command == "add":
        task = Task(id=next_id(tasks), title=validate_title(args.title),
                    priority=args.priority)
        tasks.append(task)
        save_tasks(tasks, args.file)
        print("Ditambahkan:", format_task(task))

    elif args.command == "list":
        if not tasks:
            print("Belum ada tugas.")
        for t in tasks:
            print(format_task(t))

    elif args.command == "done":
        for t in tasks:
            if t.id == args.id:
                t.mark_done()
                save_tasks(tasks, args.file)
                print("Selesai:", format_task(t))
                return
        print(f"Tugas #{args.id} tidak ditemukan.")

    elif args.command == "delete":
        remaining = [t for t in tasks if t.id != args.id]
        if len(remaining) == len(tasks):
            print(f"Tugas #{args.id} tidak ditemukan.")
            return
        save_tasks(remaining, args.file)
        print(f"Tugas #{args.id} dihapus.")

    elif args.command == "stats":
        s = summarize(tasks)
        print(f"Total: {s['total']} | Selesai: {s['done']} | "
              f"Pending: {s['pending']} | Progres: {s['completion_rate']}%")
        print("Per prioritas:", s["by_priority"])


if __name__ == "__main__":
    main()
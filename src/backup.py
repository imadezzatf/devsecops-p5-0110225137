import subprocess


def backup_file(filename):
    subprocess.run(["cp", filename, "backup/"], check=True)
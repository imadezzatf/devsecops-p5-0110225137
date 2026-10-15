import subprocess


def backup_file(filename):
    subprocess.call("cp " + filename + " backup/", shell=True)
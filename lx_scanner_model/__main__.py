import os
import subprocess

from lx_scanner_model.settings import OUTPUT_DIR
from lx_scanner_model.worker import Worker


def main():
    make_output_directory()
    worker = Worker()
    worker.launch()


def make_output_directory():
    if os.path.exists(OUTPUT_DIR):
        return

    try:
        os.makedirs(OUTPUT_DIR)
    except PermissionError:
        print(
            "Permission denied: Unable to create directory"
            f" '{OUTPUT_DIR}'. Attempting to use sudo."
        )
        result = subprocess.run(["sudo", "mkdir", "-p", OUTPUT_DIR], check=True)
        if result.returncode == 0:
            subprocess.run(
                ["sudo", "chown", f"{os.getlogin()}:{os.getlogin()}", OUTPUT_DIR],
                check=True,
            )
            print(f"Directory '{OUTPUT_DIR}' created with sudo.")
        else:
            print("Failed to create directory even with sudo.")

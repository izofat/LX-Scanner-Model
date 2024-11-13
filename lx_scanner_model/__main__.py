import os
import subprocess

from lx_scanner_model.logger import Logger
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
        Logger.info(
            "Permission denied: Unable to create directory"
            " '%s'. Attempting to use sudo.",
            OUTPUT_DIR,
        )
        result = subprocess.run(["sudo", "mkdir", "-p", OUTPUT_DIR], check=True)
        if result.returncode == 0:
            subprocess.run(
                ["sudo", "chown", f"{os.getlogin()}:{os.getlogin()}", OUTPUT_DIR],
                check=True,
            )
            Logger.info("Directory '%s' created with sudo.", OUTPUT_DIR)
        else:
            Logger.info("Failed to create directory even with sudo.")

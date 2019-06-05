import os
import sys


class StdOutToFileLogger:
    """
    Print the standard output (StdOut) to a file and still print it to the standard output.
    """

    def __init__(self, log_file_path):
        self.log_file_path = log_file_path
        self.log = None
        self.terminal = None

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        self.log.flush()
        os.fsync(self.log)

    def flush(self):
        pass

    def __enter__(self):
        self.terminal = sys.stdout
        sys.stdout = self
        self.log = open(self.log_file_path, "a")

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.terminal
        self.log.close()

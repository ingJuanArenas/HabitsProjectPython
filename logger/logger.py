from typing import Callable

class LogContext:
    def __init__(self, filename:str):
        self.filename= filename
    def __enter__(self):
        self.file= open(self.filename, "a", encoding="utf-8")
        return self.file
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

def decorator(func: Callable):
    def wrapper(*args, **kargs):
        with LogContext("habits.txt") as log:
            log.write(f"Executing {func.__name__} with args: {args}\n")
            result = func(*args, **kargs)
            log.write(f"Finished executing {func.__name__} with result: {result}\n")
            return result
    return wrapper
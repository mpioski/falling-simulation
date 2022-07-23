from time import time


class Timer:
    def __init__(self, txt):
        self.txt = txt

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        print("[TIMER] {}: {:.3f}s".format(self.txt, self.end - self.start))

    def total(self):
        return time() - self.start

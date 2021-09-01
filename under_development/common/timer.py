import time
import datetime

class TimeError(Exception):
    """A custom exception used to repost error in use of Timer class"""

class Timer:
    def __init__(self, text="Elapsed time: {:0.4f} seconds", logger=print):
        self._start_time = None
        self.text = text
        self.logger = logger

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimeError(f"Timer is running. Use .stop() to stop it.")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimeError(f"Timer is not running. Use .start() to start it.")

        elapsed_seconds = time.perf_counter() - self._start_time
        conversion = datetime.timedelta(seconds=elapsed_seconds)
        elapsed_time = str(conversion)

        self._start_time = None

        if self.logger:
            self.logger(self.text.format(elapsed_seconds))
            self.logger(f"Elapsed time: {elapsed_time}".format(elapsed_time))

        return elapsed_seconds, elapsed_time, 

# if __name__ == "__main__":
#     t = Timer()
#     t.start()
#     time.sleep(1)
#     t.stop()
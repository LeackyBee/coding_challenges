class Logger:

    def __init__(self):
        self._enabled = False


    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False

    def debug(self, message = ""):
        if self._enabled:
            print(str(message))

    def print(self, message = ""):
        print(str(message))

    def is_enabled(self):
        return self._enabled


logger = Logger()

class Logger:

    def __init__(self):
        self._enabled = False


    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False

    def print(self, message):
        if self._enabled:
            print(str(message))


logger = Logger()

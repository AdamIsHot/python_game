class move:
    def __init__(self, direction = 0):
        self._direction = direction

    def get_direction(self):
        return self._direction

    def set_direction(self, x):
        self._direction = x
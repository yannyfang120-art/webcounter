class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def increase(self):
        self.value = self.value + 1

    def increment(self, amount):
        self.value = self.value + amount

    def decrease(self):
        self.value = self.value - 1

    def reset(self):
        self.value = 0

    def set_value(self, value):
        self.value = value
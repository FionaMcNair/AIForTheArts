class HelloWorld:
    def __init__(self, message="Hello, world!", repeat=1):
        self._message = message
        self._repeat = repeat

    def get_message(self):
        return self._message

    def set_message(self, new_message):
        self._message = new_message

    def display_message(self):
        return (self._message + " ") * self._repeat


class ExcitedHelloWorld(HelloWorld):
    def __init__(self, message="Hello, world!", repeat=1, excitement_level=1):
        super().__init__(message, repeat)
        self.excitement_level = excitement_level

    def display_message(self):
        return (self.get_message() + "!" * self.excitement_level) * self._repeat

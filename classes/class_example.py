from main import log, example


@example
def init_class():
    piet = User("Piet", 24)
    bert = User("Bert", 42)

    log.info(f"Users: {piet.get_name()} and {bert.get_name()}")

    del piet, bert


class User:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def get_name(self):
        return self.__name

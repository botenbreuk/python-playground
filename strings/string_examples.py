from utils.logger import log
from main import example


@example
def format_string():
    name = "Alice"
    age = 30
    city = "New York"
    formatted_string = f"My name is {name}, I am {age} years old, and I live in {city}."
    log.info(formatted_string)


@example
def to_lowercase():
    name = "Piet"
    log.info(f"Name in lowercase: {name.lower()}")


@example
def to_uppercase():
    name = "Piet"
    log.info(f"Name in uppercase: {name.upper()}")

import os

from utils.logger import log
from main import example
from grid import read_grid


@example(name="First program")
def first_program() -> None:
    log.info("My first program")
    price = 100
    qty = 5
    total = price * qty
    log.info("Total = {}".format(total))


@example(name="Simple forloop")
def simple_forloop() -> None:
    for i in range(10):
        log.info("i = {}".format(i))


@example(name="Dictionary and logger")
def dict_and_logger() -> None:
    textObject = {"key": "value"}
    log.info("Key: {}".format(textObject["key"]))
    log.info("Hello world! Var: {}".format("Test"))


@example(name="dictionary list and retrieve data")
def list_dict_example() -> None:
    testObject2 = [{"name": "Jaap"}, {"name": "Piet"}]
    for i in range(len(testObject2)):
        log.info("Name: {}".format(testObject2[0]["name"]))


@example(name="String splitting and for loop with filter")
def string_split_loop() -> None:
    newList = []
    test = "0 || 0 || 0 || 0 || 0".split()
    for x in test:
        if x == "||":
            continue
        newList.append(x)
    log.info("New list: {}".format(newList))


@example(name="Read grid txt files and create 2D array")
def read_grid_example() -> None:
    dir_loc = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_loc}/grid.txt") as f:
        grid = read_grid(f.readlines())
    log.info("Grid: {}".format(grid))
    log.info("Grid[4][2]: {}".format(grid[4][2]))


@example(name="Console input", disable=True)
def console_input_example() -> None:
    testInput = str(input("Positie? \n"))
    log.info("Test input: {}".format([*testInput]))

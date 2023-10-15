from utils import read_grid
import logging

# Logger config
logging.basicConfig(format='[%(asctime)s] [%(levelname)s]: %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S', level=logging.DEBUG)
log = logging.getLogger(__name__)

# Print and basic variables
print("My first program")
price = 100
qty = 5
total = price * qty
print("Total = ", total)

# Simple forloop
for i in range(10):
    print(i)

# Dictionary and logger
textObject = {'key': 'value'}
print(textObject['key'])
log.info('Hello world! Var: {}'.format("Test"))

# dictionary list and retrieve data
testObject2 = [{'name': 'Jaap'}, {'name': 'Piet'}]
for i in range(len(testObject2)):
    print(testObject2[0]["name"])

# String splitting and for loop with filter
newList = []
test = "0 || 0 || 0 || 0 || 0".split()
for x in test:
    if x == "||":
        continue
    newList.append(x)
print(newList)

# Read grid txt files and create 2D array
with open('grid.txt') as f:
    grid = read_grid(f.readlines())
print(grid)
print(grid[4][2])

# Command lint input and output and character splitting
testInput = str(input("Positie? \n"))
print([*testInput])

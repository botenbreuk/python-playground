from utils import read_grid
import logging

logging.basicConfig(format='[%(asctime)s] [%(levelname)s]: %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S', level=logging.DEBUG)
log = logging.getLogger(__name__)

print("My first program")
price = 100
qty = 5
total = price * qty
print("Total = ", total)

for i in range(11):
    print(i)


textObject = {'key': 'value'}
print(textObject['key'])
log.info('Hello world! Var: {}'.format("Test"))

testObject2 = [{'name': 'Jaap'}, {'name': 'Piet'}]
for i in range(len(testObject2)):
    print(testObject2[0]["name"])

newList = []
test = "0 || 0 || 0 || 0 || 0".split()
for x in test:
    if x == "||":
        continue
    newList.append(x)

print(newList)

# testInput = str(input("Positie? \n"))
# print([*testInput])

with open('grid.txt') as f:
    grid = read_grid(f.readlines())

print(grid)
print(grid[4][2])

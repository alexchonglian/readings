import random
random.seed(1234)

import logging
from pprint import pprint
from sys import stdout as STDOUT

# Write all output to a temporary directory
import atexit
import gc
import io
import os
import tempfile

TEST_DIR = tempfile.TemporaryDirectory()
atexit.register(TEST_DIR.cleanup)

# Make sure Windows processes exit cleanly
OLD_CWD = os.getcwd()
atexit.register(lambda: os.chdir(OLD_CWD))
os.chdir(TEST_DIR.name)

def close_open_files():
    everything = gc.get_objects()
    for obj in everything:
        if isinstance(obj, io.IOBase):
            obj.close()

atexit.register(close_open_files)

def example(i): print(f'\n==== Example {i} ====')

example(1)
ALIVE = '*'
EMPTY = '-'

class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = [[EMPTY] * self.width for _ in range(self.height)]

    def get(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def set(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

    def __str__(self):
        return ''.join(
            ''.join(row)+'\n' for row in self.rows
        )

def count_neighbors(y, x, get):
    directions = {(x,y) for x in range(-1,2) for y in range(-1,2)} - {(0,0)}
    neighbor_states = [get(y+dy, x+dx) for dx, dy in directions]
    return neighbor_states.count(ALIVE)

async def game_logic(state, neighbors):
    data = await my_socket.read(50)

async def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY     # Die: Too few
        elif neighbors > 3:
            return EMPTY     # Die: Too many
    else:
        if neighbors == 3:
            return ALIVE     # Regenerate
    return state

example(2)
async def step_cell(y, x, get, set):
    state = get(y, x)
    neibrs = count_neighbors(y, x, get)
    next_state = await game_logic(state, neibrs)
    set(y, x, next_state)


example(3)
import asyncio

async def simulate(grid):
    next_grid = Grid(grid.height, grid.width)
    tasks = []
    for y in range(grid.height):
        for x in range(grid.width):
            task = step_cell(y, x, grid.get, grid.set)
            tasks.append(task)
    await asyncio.gather(*tasks)
    return next_grid

example(4)
class ColumnPrinter:
    def __init__(self):
        self.columns = []

    def append(self, data):
        self.columns.append(data)

    def __str__(self):
        row_count = 1
        for data in self.columns:
            row_count = max(
                row_count, len(data.splitlines()) + 1)

        rows = [''] * row_count
        for j in range(row_count):
            for i, data in enumerate(self.columns):
                line = data.splitlines()[max(0, j - 1)]
                if j == 0:
                    padding = ' ' * (len(line) // 2)
                    rows[j] += padding + str(i) + padding
                else:
                    rows[j] += line

                if (i + 1) < len(self.columns):
                    rows[j] += ' | '

        return '\n'.join(rows)

logging.getLogger().setLevel(logging.ERROR)

grid = Grid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)

columns = ColumnPrinter()
for i in range(5):
    columns.append(str(grid))
    grid = asyncio.run(simulate(grid))   # Run the event loop

print(columns)

logging.getLogger().setLevel(logging.DEBUG)


example(5)
try:
    async def game_logic(state, neighbors):
        raise OSError('Problem with I/O')
    
    logging.getLogger().setLevel(logging.ERROR)
    
    asyncio.run(game_logic(ALIVE, 3))
    
    logging.getLogger().setLevel(logging.DEBUG)
except:
    logging.exception('Expected')
else:
    assert False


example(6)
async def count_neighbors(y, x, get):
    directions = {(x,y) for x in range(-1,2) for y in range(-1,2)} - {(0,0)}
    neighbor_states = [get(y+dy, x+dx) for dx, dy in directions]
    return neighbor_states.count(ALIVE)

async def step_cell(y, x, get, set):
    state = get(y, x)
    neighbors = await count_neighbors(y, x, get)
    next_state = await game_logic(state, neighbors)
    set(y, x, next_state)

async def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY     # Die: Too few
        elif neighbors > 3:
            return EMPTY     # Die: Too many
    else:
        if neighbors == 3:
            return ALIVE     # Regenerate
    return state

logging.getLogger().setLevel(logging.ERROR)

grid = Grid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)

columns = ColumnPrinter()
for i in range(5):
    columns.append(str(grid))
    grid = asyncio.run(simulate(grid))

print(columns)

logging.getLogger().setLevel(logging.DEBUG)

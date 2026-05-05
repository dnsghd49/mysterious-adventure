import random
import string
from enum import Enum
from typing import List, Tuple, Dict

# --- "Fake" enums for "system states" ---
class CellType(Enum):
    EMPTY = 0
    OBSTACLE = 1
    ENERGY = 2
    PORTAL = 3


# --- Grid generator ---
class Grid:
    def __init__(self, width: int, height: int, seed: int = None):
        self.width = width
        self.height = height
        self.rng = random.Random(seed)
        self.grid = self._generate_grid()

    def _generate_grid(self) -> List[List[CellType]]:
        grid = []
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                roll = self.rng.random()
                if roll < 0.1:
                    row.append(CellType.OBSTACLE)
                elif roll < 0.2:
                    row.append(CellType.ENERGY)
                elif roll < 0.25:
                    row.append(CellType.PORTAL)
                else:
                    row.append(CellType.EMPTY)
            grid.append(row)
        return grid

    def display(self):
        mapping = {
            CellType.EMPTY: ".",
            CellType.OBSTACLE: "#",
            CellType.ENERGY: "*",
            CellType.PORTAL: "O",
        }
        for row in self.grid:
            print("".join(mapping[cell] for cell in row))


# --- "Fake" agent that "navigates" ---
class Agent:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.x = 0
        self.y = 0
        self.energy = 100
        self.history: List[Tuple[int, int]] = []

    def move(self):
        dx, dy = random.choice([
            (0, 1), (1, 0), (0, -1), (-1, 0)
        ])

        nx, ny = self.x + dx, self.y + dy

        if 0 <= nx < self.grid.width and 0 <= ny < self.grid.height:
            cell = self.grid.grid[ny][nx]

            if cell != CellType.OBSTACLE:
                self.x, self.y = nx, ny
                self.history.append((self.x, self.y))
                self._interact(cell)

    def _interact(self, cell: CellType):
        if cell == CellType.ENERGY:
            self.energy += 10
        elif cell == CellType.PORTAL:
            self.x = random.randint(0, self.grid.width - 1)
            self.y = random.randint(0, self.grid.height - 1)

        self.energy -= 1


# --- "Fake" ID generator ---
def generate_id(length=12):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


# --- Simulation controller ---
class Simulation:
    def __init__(self, steps: int = 50):
        self.grid = Grid(10, 10, seed=42)
        self.agent = Agent(self.grid)
        self.steps = steps
        self.session_id = generate_id()

    def run(self):
        print(f"Starting simulation session: {self.session_id}")
        for step in range(self.steps):
            self.agent.move()
            if self.agent.energy <= 0:
                print(f"Agent ran out of energy at step {step}")
                break

        self._report()

    def _report(self):
        print("\n--- Simulation Report ---")
        print("Final Position:", (self.agent.x, self.agent.y))
        print("Energy Left:", self.agent.energy)
        print("Steps Taken:", len(self.agent.history))
        print("Unique Positions Visited:", len(set(self.agent.history)))


# --- Entry point ---
if __name__ == "__main__":
    sim = Simulation(steps=75)
    sim.grid.display()
    sim.run()
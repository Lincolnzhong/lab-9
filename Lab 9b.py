import random

class Agent:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def move(self, grid):
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        while True:
            dx, dy = random.choice(moves)
            new_x, new_y = self.x + dx, self.y + dy
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid[new_y][new_x] is None:
                grid[self.y][self.x] = None
                grid[new_y][new_x] = self
                self.x, self.y = new_x, new_y
                break

class World:
    def __init__(self, width, height, num_agents):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.agents = []


        for i in range(num_agents):
            while True:
                x, y = random.randint(0, width - 1), random.randint(0, height - 1)
                if self.grid[y][x] is None:
                    agent = Agent(i, x, y)
                    self.grid[y][x] = agent
                    self.agents.append(agent)
                    break

    def update(self):
        for agent in self.agents:
            agent.move(self.grid)

    def display(self):
        for row in self.grid:
            print(' '.join(['.' if cell is None else 'A' for cell in row]))

def main():
    world = World(10, 10, 5)
    for _ in range(10):
        world.update()
        world.display()
        print("--------")

if __name__ == "__main__":
    main()
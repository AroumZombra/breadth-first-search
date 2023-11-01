
from queue import Queue
import time
class Maze():
    """A pathfinding problem."""

    def __init__(self, grid, location):
        """Instances differ by their current agent locations."""
        self.grid = grid
        self.location = location

    def display(self):
        """Print the maze, marking the current agent location."""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if (r, c) == self.location:
                    print('\033[96m*\x1b[0m', end=' ')   # print a blue *
                else:
                    print(self.grid[r][c], end=' ')      # prints a space or wall
            print()
        print()

    def moves(self):
        """Return a list of possible moves given the current agent location."""
        moves = []
        r, c = self.location
        # Check all four directions: up, down, left, right
        if r > 0 and self.grid[r-1][c] == ' ':
            moves.append('N')
        if r < len(self.grid)-1 and self.grid[r+1][c] == ' ':
            moves.append('S')
        if c > 0 and self.grid[r][c-1] == ' ':
            moves.append('W')
        if c < len(self.grid[r])-1 and self.grid[r][c+1] == ' ':
            moves.append('E')
        return moves

    def neighbor(self, move):
        """Return another Maze instance with a move made."""
        r, c = self.location
        if move == 'N':
            return Maze(self.grid, (r-1, c))
        elif move == 'S':
            return Maze(self.grid, (r+1, c))
        elif move == 'W':
            return Maze(self.grid, (r, c-1))
        elif move == 'E':
            return Maze(self.grid, (r, c+1))
        else:
            return self


class Agent():
    """Knows how to find the exit to a maze with BFS."""

    def bfs(self, maze, goal):
        """Return an ordered list of moves to get the maze to match the goal."""
        frontier = Queue()
        frontier.put(maze)
        came_from = {}
        came_from[maze.location] = None

        while not frontier.empty():
            current = frontier.get()

            if current.location == goal.location:
                break

            for move in current.moves():
                neighbor = current.neighbor(move)
                if neighbor.location not in came_from:
                    frontier.put(neighbor)
                    came_from[neighbor.location] = (current, move)

        # Reconstruct the path from start to goal
        path = []
        current = goal
        while current.location != maze.location:
            current, move = came_from[current.location]
            path.append(move)
        path.reverse()
        return path


def main():
    """Create a maze, solve it with BFS, and console-animate."""

    grid = ["XXXXXXXXXXXXXXXXXXXX",
            "X     X    X       X",
            "X XXXXX XXXX XXX XXX",
            "X       X      X X X",
            "X X XXX XXXXXX X X X",
            "X X   X        X X X",
            "X XXX XXXXXX XXXXX X",
            "X XXX    X X X     X",
            "X    XXX       XXXXX",
            "XXXXX   XXXXXX     X",
            "X   XXX X X    X X X",
            "XXX XXX X X XXXX X X",
            "X     X X   XX X X X",
            "XXXXX     XXXX X XXX",
            "X     X XXX    X   X",
            "X XXXXX X XXXX XXX X",
            "X X     X  X X     X",
            "X X XXXXXX X XXXXX X",
            "X X                X",
            "XXXXXXXXXXXXXXXXXX X"]

    maze = Maze(grid, (1, 1))
    maze.display()

    agent = Agent()
    goal = Maze(grid, (19, 18))
    path = agent.bfs(maze, goal)

    while path:
        move = path.pop(0)
        maze = maze.neighbor(move)
        time.sleep(0.50)
        maze.display()


if __name__ == '__main__':
    main()

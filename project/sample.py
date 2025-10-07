
import random  # For random choices when multiple paths are available
class VirtualCharacter:
    def __init__(self, maze, start_pos, goal_pos):
        self.maze = maze  # The maze grid (0 = open path, 1 = wall, 2 = goal)
        self.position = start_pos  # Starting position (row, col)
        self.goal = goal_pos  # Goal position (row, col)
        self.visited = set()  # Memory: tracks visited positions to avoid loops
        self.path = []  # Records the path taken for backtracking if needed
    
    def is_valid_move(self, row, col):
        # Check if a move is safe (within bounds, not a wall, not visited to avoid loops)
        rows, cols = len(self.maze), len(self.maze[0])
        return (0 <= row < rows and 0 <= col < cols and
                self.maze[row][col] != 1 and  # Not a wall
                (row, col) not in self.visited)  # Not visited before
    
    def get_possible_moves(self):
        # Intelligent decision: Find all valid next moves
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
        moves = []
        for dr, dc in directions:
            new_row, new_col = self.position[0] + dr, self.position[1] + dc
            if self.is_valid_move(new_row, new_col):
                # Prioritize moves closer to goal (simple distance check for "intelligence")
                distance_to_goal = abs(new_row - self.goal[0]) + abs(new_col - self.goal[1])
                moves.append((new_row, new_col, distance_to_goal))
        # Sort by distance to goal (smallest first) for smarter choice
        moves.sort(key=lambda x: x[2])
        return moves
    
    def move(self):
        # Main intelligent behavior: Choose and make the best move
        possible_moves = self.get_possible_moves()
        if not possible_moves:
            print("No valid moves! Stuck.")
            return False
        
        # Pick the smartest move (closest to goal)
        best_move = possible_moves[0][:2]  # (row, col)
        self.position = best_move
        self.visited.add(best_move)
        self.path.append(best_move)
        print(f"Character moved to: {best_move}")
        
        # Check if goal reached
        if best_move == self.goal:
            print("Goal reached! Intelligent navigation successful.")
            return True
        return False
    
   
# Example maze (5x5 grid): 0=open, 1=wall, 2=goal
maze = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 2]  # 2 is the goal
]
# Create and run the virtual character
start = (0, 0)  # Start at top-left
goal = (4, 4)   # Goal at bottom-right
character = VirtualCharacter(maze, start, goal)
print("Starting maze exploration...")
print("Maze layout:")
for row in maze:
    print(row)
steps = 0
max_steps = 20  # Prevent infinite loops
while steps < max_steps:
    if character.move():
        break
    steps += 1
print(f"Path taken: {character.path}")
print("Exploration complete.")
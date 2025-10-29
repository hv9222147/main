# # import random

# # empty = '~'
# # water = 'W'
# # rock = 'R'
# # tree = 'T'
# # depot = 'D'

# # def generate_project_map(width, height, rock_prob=0.1, tree_prob=0.2, water_prob=0.1):

# #     project_map = []
# #     for y in range(height):
# #         row = []
# #         for x in range(weight):
# #             rand_val = random.random()
# #             if rand_val < rock_prob:
# #                 row.append(rock)
# #             elif rand_val < rock_prob + tree_prob:
# #                 row.append(tree)
# #             elif rand_val < rock_prob + tree_prob + water_prob:
# #                  row.append(water)
# #             else:
# #                 row.append(empty)
# #         project_map.append(row)
# #     return project_mapht:



# import random

# # ---------- Terrain Types ----------
# EMPTY = '.'
# ROCK = 'R'
# TREE = 'T'
# WATER = 'W'
# DEPOT = 'D'

# # ---------- Cell Class ----------
# class Cell:
#     def __init__(self, terrain=EMPTY, occupant=None):
#         self.terrain = terrain     # What kind of ground (Rock, Tree, etc.)
#         self.occupant = occupant   # Which unit is standing here (C, W, M, etc.)

#     def __str__(self):
#         # If someone is on this cell, show their letter; otherwise show terrain
#         return self.occupant if self.occupant else self.terrain


# # ---------- Map Class ----------
# class Battlefield:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         # Create a 2D list (matrix) of Cell objects
#         self.grid = [[Cell() for _ in range(width)] for _ in range(height)]

#     def generate(self):
#         """Fill the map with random terrain."""
#         for y in range(self.height):
#             for x in range(self.width):
#                 r = random.random()
#                 if r < 0.1:            # 10% chance → Rock
#                     self.grid[y][x].terrain = ROCK
#                 elif r < 0.3:          # Next 20% → Tree
#                     self.grid[y][x].terrain = TREE
#                 elif r < 0.4:          # Next 10% → Water
#                     self.grid[y][x].terrain = WATER
#                 else:
#                     self.grid[y][x].terrain = EMPTY  # Remaining 60%

#         # Place 2 depots (for demo)
#         self.grid[1][1].terrain = DEPOT
#         self.grid[self.height - 2][self.width - 2].terrain = DEPOT

#     def place_unit(self, x, y, symbol):
#         """Place a soldier/commander/medic on the map."""
#         if 0 <= x < self.width and 0 <= y < self.height:
#             self.grid[y][x].occupant = symbol

#     def display(self):
#         """Show the battlefield."""
#         print("\nBattlefield Map:\n")
#         for row in self.grid:
#             print(" ".join(str(cell) for cell in row))
#         print()


# # ---------- Example Use ----------
# if __name__ == "__main__":
#     bf = Battlefield(12, 8)
#     bf.generate()

#     # Place some units
#     bf.place_unit(0, 0, 'C')  # Commander
#     bf.place_unit(2, 0, 'W')  # Warrior
#     bf.place_unit(3, 0, 'M')  # Medic
#     bf.place_unit(4, 0, 'P')  # Supply soldier

#     bf.display()



# Define terrain types
class Terrain:
    ROCK = "R"
    TREE = "T"
    WATER = "W"
    EMPTY = "."
    DEPOT = "D"

# Define a cell on the battlefield
class Cell:
    def __init__(self, terrain, occupant=None):
        self.terrain = terrain
        self.occupant = occupant  # could be 'soldier', 'tank', etc.

    def __repr__(self):
        """This helps print the cell in a readable way."""
        return f"{self.terrain[:2]}"  # show first two letters (e.g., 'Ro' for Rock)

# Define the battlefield map (2D matrix)
class Battlefield:
    def __init__(self, width, height):
        # create an empty map filled with 'Empty' terrain
        self.map = [[Cell(Terrain.EMPTY) for _ in range(width)] for _ in range(height)]

    def set_terrain(self, x, y, terrain):
        """Set the terrain type at a specific coordinate."""
        self.map[y][x].terrain = terrain

    def display(self):
        """Print the battlefield in a grid format."""
        for row in self.map:
            print(" ".join(str(cell) for cell in row))

# Create a 5x5 battlefield
battlefield = Battlefield(5, 5)

# Set some terrain types
battlefield.set_terrain(1, 1, Terrain.ROCK)
battlefield.set_terrain(2, 3, Terrain.TREE)
battlefield.set_terrain(0, 4, Terrain.WATER)
battlefield.set_terrain(3, 0, Terrain.DEPOT)

# Display the battlefield
battlefield.display()

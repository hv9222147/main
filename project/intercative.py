
# # # # Interactive Math Quiz for Kids
# # # import random  # This helps pick random numbers for questions
# # # # Welcome message
# # # print("Welcome to the Fun Math Quiz, Kiddo! 🎉")
# # # print("We'll do 5 easy addition questions. Type your answer and press Enter.")
# # # print("Let's go! 🚀\n")
# # # # Set up the game
# # # score = 0  # Start with 0 points
# # # questions = 5  # Total questions
# # # # Loop for 5 questions
# # # for i in range(questions):
# # #     # Pick two small random numbers (1 to 10)
# # #     num1 = random.randint(1, 10)
# # #     num2 = random.randint(1, 10)
# # #     correct_answer = num1 + num2  # The right answer
    
# # #     # Ask the question
# # #     print(f"Question {i+1}: What is {num1} + {num2}?")
# # #     user_answer = int(input("Your answer: "))  # Get kid's answer
    
# # #     # Check if correct
# # #     if user_answer == correct_answer:
# # #         print("Yay! That's right! 🌟 You got a star!")
# # #         score += 1  # Add 1 point
# # #     else:
# # #         print(f"Oops! It's {correct_answer}. No worries, try next time! 😊")
    
# # #     print()  # Empty line for space
# # # # End of game

# # # # loop for 5  questions:

# # # for i in range(questions):
# # #     num1 = random.randint(1,10)
# # #     num2 = random.randint(1,10)
# # #     correct_answer = num1 + num2 

# # #     print(f"question {i+1}: what is {num1} + {num2}?")
# # #     user_answer = int(input("your asnwer:"))

# # #     if user_answer == correct_answer:
# # #         print("yay! that's right! you got a star!")
# # #         score +=1 
# # #     else:
# # #         print(f"oops! its {correct_answer}. no worries, try next time! ")
        
# # #     print()





# # # Interactive Math, Animals & Fruits Quiz for Kids
# # import random  # This helps pick random questions from categories

# # # Dictionary for animals and their typical colors (using animal names as keys)
# # animals_colors = {
# #     "tiger": "orange",
# #     "elephant": "gray",
# #     "flamingo": "pink",
# #     "penguin": "black",
# #     "lion": "yellow",
# #     "zebra": "white",
# #     "frog": "green",
# #     "polar bear": "white",
# #     "parrot": "green",
# #     "cow": "brown"  # Added one more for variety
# # }

# # # Dictionary for fruits and their typical colors (using fruit names as keys)
# # fruits_colors = {
# #     "apple": "red",
# #     "banana": "yellow",
# #     "orange": "orange",
# #     "grape": "purple",
# #     "strawberry": "red",
# #     "watermelon": "green",
# #     "lemon": "yellow",
# #     "blueberry": "blue",
# #     "cherry": "red",
# #     "pear": "green"
# # }

# # # List of categories
# # categories = ["math", "animal", "fruit"]

# # # Welcome message
# # print("Welcome to the Math, Animals & Fruits Adventure, Kiddo! 🧮🐯🍎")
# # print("We'll do 5 fun questions mixing math, animal names/colors, and fruit names/colors.")
# # print("For math: Type a number. For colors: Type the color (like 'red' or 'Red'). Press Enter.")
# # print("Let's learn and play! 🌟\n")

# # # Set up the game
# # score = 0  # Start with 0 points
# # questions = 5  # Total questions

# # # Loop for 5 questions
# # for i in range(questions):
# #     # Pick a random category
# #     category = random.choice(categories)
    
# #     if category == "math":
# #         # Math question: Simple addition
# #         num1 = random.randint(1, 10)
# #         num2 = random.randint(1, 10)
# #         correct_answer = num1 + num2
# #         print(f"Question {i+1} (Math): What is {num1} + {num2}?")
# #         try:
# #             user_answer = int(input("Your number: "))  # Expect a number
# #         except ValueError:
# #             user_answer = 0  # If not a number, treat as wrong but gentle
# #         if user_answer == correct_answer:
# #             print(f"Yay! That's right! {num1} + {num2} = {correct_answer}! 🌟 You got a star!")
# #             score += 1
# #         else:
# #             print(f"Oops! It's {correct_answer}. Keep practicing math! 😊")
    
# #     elif category == "animal":
# #         # Animal question: Color of animal name
# #         animal = random.choice(list(animals_colors.keys()))
# #         correct_color = animals_colors[animal]
# #         print(f"Question {i+1} (Animal): What color is a {animal}?")
# #         user_answer = input("Your color guess: ").strip().lower()
# #         if user_answer == correct_color:
# #             print(f"Yay! That's right! A {animal} is {correct_color}! 🐾 You got a star!")
# #             score += 1
# #         else:
# #             print(f"Oops! A {animal} is usually {correct_color}. Animals are colorful! 😊")
    
# #     else:  # category == "fruit"
# #         # Fruit question: Color of fruit name
# #         fruit = random.choice(list(fruits_colors.keys()))
# #         correct_color = fruits_colors[fruit]
# #         print(f"Question {i+1} (Fruit): What color is a {fruit}?")
# #         user_answer = input("Your color guess: ").strip().lower()
# #         if user_answer == correct_color:
# #             print(f"Yay! That's right! A {fruit} is {correct_color}! 🍒 You got a star!")
# #             score += 1
# #         else:
# #             print(f"Oops! A {fruit} is usually {correct_color}. Fruits are yummy colors! 😊")
    
# #     print()  # Empty line for space

# # # End of the game
# # print(f"Adventure over! You got {score} out of {questions} correct. Amazing job with math, animals, and fruits! 🏆")
# # if score == questions:
# #     print("Perfect score! You're a super learner in everything! ⭐⭐⭐")
# # elif score >= 3:
# #     print("Awesome! You rock at math, animals, and fruits—keep exploring! 👍")
# # else:
# #     print("Good try! Play again to master more names and colors! 💪")



# """
# Team Tactics — Grid Game Prototype
# Single-file Python prototype implementing:
# - Map generation (tiles: Rock, Tree, Water, Depot)
# - Characters: Commander, Warrior, Medic, SupplySoldier
# - Pathfinding: A* (movement), BFS (safe zone search)
# - Visibility map per character and merged Commander visibility
# - Safety map (danger zones) using enemy sightings
# - Simple AI behaviors and command system
# - Console visualization (text grid) and a small simulation runner

# How to run:
#   python Team-Tactics-GridGame-ProofOfConcept.py

# Notes:
# - This is a proof-of-concept to demonstrate architecture and algorithms.
# - Extensible to add Pygame / web UI later.
# """

# from __future__ import annotations
# import random
# import heapq
# from typing import List, Tuple, Dict, Optional, Set
# import math
# import time

# Point = Tuple[int,int]

# # -------------------- Tile / Map Definitions --------------------
# class TileType:
#     EMPTY = '.'      # passable, visible
#     ROCK  = '#'
#     TREE  = 'T'      # passable but blocks visibility
#     WATER = '~'      # impassable but does not block visibility (you can see across)
#     DEPOT = 'D'      # depot for ammo/med

# class Tile:
#     def __init__(self, ttype: str = TileType.EMPTY):
#         self.type = ttype
#         self.passable = ttype in (TileType.EMPTY, TileType.TREE, TileType.DEPOT)
#         # trees block visibility
#         self.blocks_vision = ttype in (TileType.ROCK, TileType.TREE)

# # -------------------- Map --------------------
# class MapGrid:
#     def __init__(self, w:int, h:int, rock_prob=0.08, tree_prob=0.12, water_prob=0.06, num_depots=2):
#         self.w = w
#         self.h = h
#         self.grid: List[List[Tile]] = [[Tile() for _ in range(w)] for __ in range(h)]
#         self.depots: List[Point] = []
#         self.generate(rock_prob, tree_prob, water_prob, num_depots)

#     def in_bounds(self, p:Point) -> bool:
#         x,y = p
#         return 0 <= x < self.w and 0 <= y < self.h

#     def neighbors(self, p:Point) -> List[Point]:
#         x,y = p
#         candidates = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
#         return [c for c in candidates if self.in_bounds(c) and self.grid[c[1]][c[0]].passable]

#     def generate(self, rock_p, tree_p, water_p, num_depots):
#         for y in range(self.h):
#             for x in range(self.w):
#                 r = random.random()
#                 if r < rock_p:
#                     self.grid[y][x] = Tile(TileType.ROCK)
#                 elif r < rock_p + tree_p:
#                     self.grid[y][x] = Tile(TileType.TREE)
#                 elif r < rock_p + tree_p + water_p:
#                     self.grid[y][x] = Tile(TileType.WATER)
#                 else:
#                     self.grid[y][x] = Tile(TileType.EMPTY)
#         # place depots in passable locations
#         placed = 0
#         attempts = 0
#         while placed < num_depots and attempts < 5000:
#             attempts += 1
#             x = random.randrange(self.w)
#             y = random.randrange(self.h)
#             if self.grid[y][x].passable and self.grid[y][x].type == TileType.EMPTY:
#                 self.grid[y][x] = Tile(TileType.DEPOT)
#                 self.depots.append((x,y))
#                 placed += 1

#     def tile_at(self, p:Point) -> Tile:
#         x,y = p
#         return self.grid[y][x]

#     def display(self, characters:List['Character']=None, visibility:Optional[Set[Point]]=None):
#         # build map of chars
#         char_map: Dict[Point,str] = {}
#         if characters:
#             for ch in characters:
#                 if ch.alive:
#                     char_map[ch.pos] = ch.symbol
#         lines = []
#         for y in range(self.h):
#             row = ''
#             for x in range(self.w):
#                 p = (x,y)
#                 if visibility is not None and p not in visibility:
#                     row += ' '  # unexplored / not visible
#                 elif p in char_map:
#                     row += char_map[p]
#                 else:
#                     row += self.tile_at(p).type
#             lines.append(row)
#         print('\n'.join(lines))

# # -------------------- Pathfinding: A* and BFS --------------------

# def heuristic(a:Point,b:Point) -> float:
#     return abs(a[0]-b[0]) + abs(a[1]-b[1])

# def a_star(grid:MapGrid, start:Point, goal:Point, avoid:Optional[Set[Point]]=None) -> Optional[List[Point]]:
#     if avoid is None: avoid = set()
#     if start == goal: return [start]
#     open_heap = []
#     heapq.heappush(open_heap, (0+heuristic(start,goal), 0, start, None))
#     came_from: Dict[Point, Optional[Point]] = {start: None}
#     gscore: Dict[Point, float] = {start: 0}

#     while open_heap:
#         f, g, current, _ = heapq.heappop(open_heap)
#         if current == goal:
#             path = []
#             cur = current
#             while cur is not None:
#                 path.append(cur)
#                 cur = came_from[cur]
#             path.reverse()
#             return path
#         for nb in grid.neighbors(current):
#             if nb in avoid:
#                 continue
#             tentative_g = gscore[current] + 1
#             if nb not in gscore or tentative_g < gscore[nb]:
#                 gscore[nb] = tentative_g
#                 came_from[nb] = current
#                 heapq.heappush(open_heap, (tentative_g + heuristic(nb,goal), tentative_g, nb, current))
#     return None

# from collections import deque

# def bfs_find_nearest(grid:MapGrid, start:Point, condition) -> Optional[List[Point]]:
#     # condition: fn(pos) -> bool
#     q = deque()
#     q.append(start)
#     came_from = {start: None}
#     while q:
#         cur = q.popleft()
#         if condition(cur):
#             # build path
#             path = []
#             while cur is not None:
#                 path.append(cur)
#                 cur = came_from[cur]
#             path.reverse()
#             return path
#         for nb in grid.neighbors(cur):
#             if nb not in came_from:
#                 came_from[nb] = cur
#                 q.append(nb)
#     return None

# # -------------------- Visibility --------------------

# def los_blocks(grid:MapGrid, a:Point, b:Point) -> bool:
#     # simple bresenham line of sight: if any blocking tile between pts, return True
#     x0,y0 = a; x1,y1 = b
#     dx = abs(x1-x0)
#     dy = -abs(y1-y0)
#     sx = 1 if x0 < x1 else -1
#     sy = 1 if y0 < y1 else -1
#     err = dx + dy
#     while True:
#         if (x0,y0) != a and grid.tile_at((x0,y0)).blocks_vision:
#             return True
#         if (x0,y0) == (x1,y1): break
#         e2 = 2*err
#         if e2 >= dy:
#             err += dy; x0 += sx
#         if e2 <= dx:
#             err += dx; y0 += sy
#     return False

# def visibility_from(grid:MapGrid, origin:Point, radius:int) -> Set[Point]:
#     vis = set()
#     ox,oy = origin
#     for dx in range(-radius, radius+1):
#         for dy in range(-radius, radius+1):
#             x = ox + dx; y = oy + dy
#             p = (x,y)
#             if not grid.in_bounds(p): continue
#             if dx*dx + dy*dy > radius*radius: continue
#             # if line of sight is not blocked
#             if not los_blocks(grid, origin, p):
#                 vis.add(p)
#     return vis

# # -------------------- Safety Map --------------------

# def compute_safety_map(grid:MapGrid, enemy_positions:List[Point], danger_radius=3) -> Dict[Point,float]:
#     safety: Dict[Point,float] = {}
#     for y in range(grid.h):
#         for x in range(grid.w):
#             p = (x,y)
#             base = 0.0
#             for e in enemy_positions:
#                 d = math.hypot(e[0]-x, e[1]-y)
#                 if d <= danger_radius:
#                     base += max(0, (danger_radius - d) / danger_radius)
#             safety[p] = base
#     return safety

# # -------------------- Characters --------------------
# class Character:
#     def __init__(self, name:str, pos:Point, team:int, symbol:str='?'):
#         self.name = name
#         self.pos = pos
#         self.team = team
#         self.symbol = symbol
#         self.health = 100
#         self.max_health = 100
#         self.ammo = 10
#         self.vision = 5
#         self.alive = True
#         self.path: Optional[List[Point]] = None

#     def distance_to(self, p:Point) -> int:
#         return abs(self.pos[0]-p[0]) + abs(self.pos[1]-p[1])

#     def take_damage(self, dmg:int):
#         self.health -= dmg
#         if self.health <= 0:
#             self.alive = False

#     def step_along_path(self):
#         if self.path and len(self.path) > 1:
#             # first is current pos
#             self.path.pop(0)
#             self.pos = self.path[0]

#     def report_status(self):
#         return f"{self.name}(H:{self.health} A:{self.ammo})"

# class Commander(Character):
#     def __init__(self, name, pos, team):
#         super().__init__(name,pos,team,'C')
#         self.aggro_map: Dict[Point,float] = {}

#     def decide(self, gm:'GameManager'):
#         # Combine team vis to issue simple commands.
#         # For demo: if any enemy visible, command nearest warrior to attack, medic to heal, supply to resupply.
#         visible_enemies = gm.get_visible_enemies(self.team)
#         my_team = gm.get_team(self.team)
#         warriors = [c for c in my_team if isinstance(c,Warrior) and c.alive]
#         medics = [c for c in my_team if isinstance(c,Medic) and c.alive]
#         supplies = [c for c in my_team if isinstance(c,SupplySoldier) and c.alive]

#         if visible_enemies and warriors:
#             # pick the closest warrior to the nearest enemy
#             enemy = visible_enemies[0]
#             for w in warriors:
#                 target_path = a_star(gm.grid, w.pos, enemy, avoid=gm.get_avoid_set())
#                 if target_path:
#                     w.path = target_path
#                     w.current_goal = ('attack', enemy)
#                     break
#         else:
#             # patrol: give a random nearby point
#             for w in warriors:
#                 if w.path is None or len(w.path) <= 1:
#                     rx = max(0,min(gm.grid.w-1, w.pos[0] + random.randint(-6,6)))
#                     ry = max(0,min(gm.grid.h-1, w.pos[1] + random.randint(-6,6)))
#                     path = a_star(gm.grid, w.pos, (rx,ry), avoid=gm.get_avoid_set())
#                     if path:
#                         w.path = path
#                         w.current_goal = ('patrol',(rx,ry))
#         # medics and supplies reactively get commands when team reports low status in gm tick.

# class Warrior(Character):
#     def __init__(self, name, pos, team):
#         super().__init__(name,pos,team,'W')
#         self.current_goal = None

#     def act(self, gm:'GameManager'):
#         # If low ammo or health, report to commander
#         if self.ammo <= 0 and gm.has_supply(self.team):
#             # try to head to depot via supply soldier command
#             self.current_goal = ('need_ammo', None)
#         if self.health < 30:
#             self.current_goal = ('need_heal', None)
#         # If path is set, move
#         if self.path:
#             # if next tile is in high danger, attempt to replanning
#             self.step_along_path()
#         # if at target enemy and has ammo, fire
#         visible_enemies = gm.get_visible_enemies(self.team_from(self),only_positions=False)
#         if visible_enemies and self.ammo > 0:
#             # find an enemy in range (melee range 1 or 2)
#             for enemy in visible_enemies:
#                 if self.distance_to(enemy) <= 2:
#                     self.shoot(enemy)
#                     break

#     def shoot(self, enemy_pos:Point):
#         if self.ammo <= 0: return
#         self.ammo -= 1
#         hit_chance = 0.6
#         if random.random() < hit_chance:
#             # caller will resolve damage via GameManager (we store target)
#             self.last_shot_target = enemy_pos

#     def team_from(self, _):
#         return self.team

# class Medic(Character):
#     def __init__(self, name,pos,team):
#         super().__init__(name,pos,team,'M')
#         self.heal_amount = 40

#     def act(self, gm:'GameManager'):
#         # if has command to heal, follow path
#         if self.path:
#             self.step_along_path()
#             # if reached someone injured
#             for ally in gm.get_team(self.team):
#                 if ally.alive and ally.health < ally.max_health and self.distance_to(ally) <= 1:
#                     ally.health = min(ally.max_health, ally.health + self.heal_amount)

# class SupplySoldier(Character):
#     def __init__(self, name,pos,team):
#         super().__init__(name,pos,team,'S')
#         self.carry = 20

#     def act(self, gm:'GameManager'):
#         if self.path:
#             self.step_along_path()
#         # if adjacent to ally with low ammo, refill
#         for ally in gm.get_team(self.team):
#             if ally.alive and ally.ammo < 5 and self.distance_to(ally) <= 1:
#                 needed = min(self.carry, 10 - ally.ammo)
#                 ally.ammo += needed
#                 self.carry -= needed

# # -------------------- Game Manager --------------------
# class GameManager:
#     def __init__(self, w=30, h=18, teams=2):
#         self.grid = MapGrid(w,h)
#         self.teams = teams
#         self.characters: List[Character] = []
#         self.tick_count = 0
#         self.init_teams()

#     def init_teams(self):
#         # spawn teams near opposite sides
#         for t in range(self.teams):
#             side_x = 2 if t == 0 else self.grid.w - 3
#             # commander
#             cpos = self.find_free_near((side_x, self.grid.h//2))
#             cmd = Commander(f'Cmd{t}', cpos, t)
#             self.characters.append(cmd)
#             # warriors
#             for i in range(3):
#                 p = self.find_free_near((side_x, self.grid.h//2 + i + (t* -1)))
#                 w = Warrior(f'W{t}_{i}', p, t)
#                 self.characters.append(w)
#             # medic
#             mpos = self.find_free_near((side_x, self.grid.h//2 + 4))
#             med = Medic(f'M{t}', mpos, t)
#             self.characters.append(med)
#             # supply
#             spos = self.find_free_near((side_x, self.grid.h//2 - 4))
#             sup = SupplySoldier(f'S{t}', spos, t)
#             self.characters.append(sup)

#     def find_free_near(self, center:Point, radius=4) -> Point:
#         cx,cy = center
#         for _ in range(2000):
#             rx = max(0,min(self.grid.w-1, cx + random.randint(-radius, radius)))
#             ry = max(0,min(self.grid.h-1, cy + random.randint(-radius, radius)))
#             if self.grid.tile_at((rx,ry)).passable and not any(ch.pos == (rx,ry) for ch in self.characters):
#                 return (rx,ry)
#         # fallback
#         for y in range(self.grid.h):
#             for x in range(self.grid.w):
#                 if self.grid.tile_at((x,y)).passable and not any(ch.pos == (x,y) for ch in self.characters):
#                     return (x,y)
#         return (0,0)

#     def get_team(self, team:int) -> List[Character]:
#         return [c for c in self.characters if c.team == team]

#     def get_visible_enemies(self, team:int) -> List[Point]:
#         # return a list of enemy positions visible by any of team's members (merge vis)
#         vis = set()
#         for c in self.get_team(team):
#             if not c.alive: continue
#             vis.update(visibility_from(self.grid, c.pos, c.vision))
#         enemies = [e.pos for e in self.characters if e.team != team and e.alive and e.pos in vis]
#         return enemies

#     def has_supply(self, team:int) -> bool:
#         return any(isinstance(c,SupplySoldier) and c.alive for c in self.get_team(team))

#     def get_avoid_set(self) -> Set[Point]:
#         # avoid water and rocks
#         s = set()
#         for y in range(self.grid.h):
#             for x in range(self.grid.w):
#                 t = self.grid.tile_at((x,y))
#                 if not t.passable:
#                     s.add((x,y))
#         return s

#     def tick(self):
#         self.tick_count += 1
#         # update commanders decisions
#         for cmd in [c for c in self.characters if isinstance(c,Commander) and c.alive]:
#             cmd.decide(self)
#         # each character acts
#         for ch in [c for c in self.characters if c.alive]:
#             if isinstance(ch,Warrior):
#                 ch.act(self)
#             elif isinstance(ch,Medic):
#                 ch.act(self)
#             elif isinstance(ch,SupplySoldier):
#                 ch.act(self)
#         # resolve shots (simple: warriors who recorded last_shot_target)
#         shots = []
#         for w in [c for c in self.characters if isinstance(c,Warrior) and c.alive]:
#             tgt = getattr(w, 'last_shot_target', None)
#             if tgt:
#                 shots.append((w,tgt))
#                 delattr(w, 'last_shot_target')
#         for shooter, tgt in shots:
#             # find a character at target
#             for victim in [c for c in self.characters if c.pos == tgt and c.team != shooter.team and c.alive]:
#                 # apply damage
#                 dmg = random.randint(20,40)
#                 victim.take_damage(dmg)
#         # simple auto-depot refill when on depot
#         for ch in [c for c in self.characters if c.alive]:
#             if self.grid.tile_at(ch.pos).type == TileType.DEPOT:
#                 if isinstance(ch,SupplySoldier):
#                     ch.carry = 20
#                 else:
#                     ch.ammo = min(10, ch.ammo + 3)
#                     ch.health = min(ch.max_health, ch.health + 5)
#         # remove dead: keep them but mark dead (symbol 'X')
#         for ch in [c for c in self.characters if not c.alive]:
#             ch.symbol = 'x'

#     def get_all_visible(self, team:int) -> Set[Point]:
#         vis = set()
#         for c in self.get_team(team):
#             if c.alive:
#                 vis.update(visibility_from(self.grid, c.pos, c.vision))
#         return vis

#     def enemy_positions(self, team:int) -> List[Point]:
#         return [c.pos for c in self.characters if c.team]
    







import random
from collections import deque

# ----------------------------
# Environment Module
# ----------------------------
TERRAINS = ['.', '#', 'T', '~', 'M', 'A']  # Empty, Rock, Tree, Water, Med Depot, Ammo Depot

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[random.choice(TERRAINS) for _ in range(width)] for _ in range(height)]

    def display(self):
        for row in self.map:
            print(' '.join(row))
        print()

# ----------------------------
# Pathfinding Module
# ----------------------------
class Pathfinding:
    def __init__(self, env):
        self.env = env

    def is_valid(self, x, y):
        return 0 <= x < self.env.height and 0 <= y < self.env.width and self.env.map[x][y] != '#'

    def bfs(self, start, goal):
        """Simple BFS pathfinding"""
        queue = deque([start])
        visited = {start: None}
        while queue:
            x, y = queue.popleft()
            if (x, y) == goal:
                break
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x + dx, y + dy
                if self.is_valid(nx, ny) and (nx, ny) not in visited:
                    visited[(nx, ny)] = (x, y)
                    queue.append((nx, ny))
        return self.reconstruct_path(visited, goal)

    def reconstruct_path(self, visited, goal):
        path = []
        node = goal
        while node and node in visited:
            path.append(node)
            node = visited[node]
        return path[::-1]

# ----------------------------
# Character Modules
# ----------------------------
class Character:
    def __init__(self, role, x, y):
        self.role = role
        self.x = x
        self.y = y
        self.health = 100
        self.ammo = 10

    def move(self, new_x, new_y):
        self.x, self.y = new_x, new_y
        print(f"{self.role} moved to ({self.x}, {self.y})")

class Commander(Character):
    def plan_action(self):
        print("Commander planning strategy...")

class Warrior(Character):
    def attack(self):
        print("Warrior attacking the enemy!")

class Medic(Character):
    def heal(self, teammate):
        print(f"Medic healing {teammate.role}...")

class SupplySoldier(Character):
    def resupply(self, teammate):
        print(f"Supplying ammo to {teammate.role}...")

# ----------------------------
# Game Engine
# ----------------------------
class GameEngine:
    def __init__(self):
        self.env = Environment(5, 5)
        self.pathfinder = Pathfinding(self.env)
        self.commander = Commander("Commander", 0, 0)
        self.warrior = Warrior("Warrior", 1, 1)
        self.medic = Medic("Medic", 2, 2)
        self.supply = SupplySoldier("Supply", 3, 3)

    # def play_turn(self):
    #     self.env.display()
    #     self.commander.plan_action()
    #     path = self.pathfinder.bfs((0,0), (4,4))
    #     print("Path (BFS):", path)
    #     self.warrior.attack()
    #     self.medic.heal(self.warrior)
    #     self.supply.resupply(self.warrior)

# ----------------------------
# Main Execution
# ----------------------------
if __name__ == "__main__":
    game = GameEngine()
    # game.play_turn()

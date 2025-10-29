
# # # # # Interactive Math Quiz for Kids
# # # # import random  # This helps pick random numbers for questions
# # # # # Welcome message
# # # # print("Welcome to the Fun Math Quiz, Kiddo! 🎉")
# # # # print("We'll do 5 easy addition questions. Type your answer and press Enter.")
# # # # print("Let's go! 🚀\n")
# # # # # Set up the game
# # # # score = 0  # Start with 0 points
# # # # questions = 5  # Total questions
# # # # # Loop for 5 questions
# # # # for i in range(questions):
# # # #     # Pick two small random numbers (1 to 10)
# # # #     num1 = random.randint(1, 10)
# # # #     num2 = random.randint(1, 10)
# # # #     correct_answer = num1 + num2  # The right answer
    
# # # #     # Ask the question
# # # #     print(f"Question {i+1}: What is {num1} + {num2}?")
# # # #     user_answer = int(input("Your answer: "))  # Get kid's answer
    
# # # #     # Check if correct
# # # #     if user_answer == correct_answer:
# # # #         print("Yay! That's right! 🌟 You got a star!")
# # # #         score += 1  # Add 1 point
# # # #     else:
# # # #         print(f"Oops! It's {correct_answer}. No worries, try next time! 😊")
    
# # # #     print()  # Empty line for space
# # # # # End of game

# # # # # loop for 5  questions:

# # # # for i in range(questions):
# # # #     num1 = random.randint(1,10)
# # # #     num2 = random.randint(1,10)
# # # #     correct_answer = num1 + num2 

# # # #     print(f"question {i+1}: what is {num1} + {num2}?")
# # # #     user_answer = int(input("your asnwer:"))

# # # #     if user_answer == correct_answer:
# # # #         print("yay! that's right! you got a star!")
# # # #         score +=1 
# # # #     else:
# # # #         print(f"oops! its {correct_answer}. no worries, try next time! ")
        
# # # #     print()





# # # # Interactive Math, Animals & Fruits Quiz for Kids
# # # import random  # This helps pick random questions from categories

# # # # Dictionary for animals and their typical colors (using animal names as keys)
# # # animals_colors = {
# # #     "tiger": "orange",
# # #     "elephant": "gray",
# # #     "flamingo": "pink",
# # #     "penguin": "black",
# # #     "lion": "yellow",
# # #     "zebra": "white",
# # #     "frog": "green",
# # #     "polar bear": "white",
# # #     "parrot": "green",
# # #     "cow": "brown"  # Added one more for variety
# # # }

# # # # Dictionary for fruits and their typical colors (using fruit names as keys)
# # # fruits_colors = {
# # #     "apple": "red",
# # #     "banana": "yellow",
# # #     "orange": "orange",
# # #     "grape": "purple",
# # #     "strawberry": "red",
# # #     "watermelon": "green",
# # #     "lemon": "yellow",
# # #     "blueberry": "blue",
# # #     "cherry": "red",
# # #     "pear": "green"
# # # }

# # # # List of categories
# # # categories = ["math", "animal", "fruit"]

# # # # Welcome message
# # # print("Welcome to the Math, Animals & Fruits Adventure, Kiddo! 🧮🐯🍎")
# # # print("We'll do 5 fun questions mixing math, animal names/colors, and fruit names/colors.")
# # # print("For math: Type a number. For colors: Type the color (like 'red' or 'Red'). Press Enter.")
# # # print("Let's learn and play! 🌟\n")

# # # # Set up the game
# # # score = 0  # Start with 0 points
# # # questions = 5  # Total questions

# # # # Loop for 5 questions
# # # for i in range(questions):
# # #     # Pick a random category
# # #     category = random.choice(categories)
    
# # #     if category == "math":
# # #         # Math question: Simple addition
# # #         num1 = random.randint(1, 10)
# # #         num2 = random.randint(1, 10)
# # #         correct_answer = num1 + num2
# # #         print(f"Question {i+1} (Math): What is {num1} + {num2}?")
# # #         try:
# # #             user_answer = int(input("Your number: "))  # Expect a number
# # #         except ValueError:
# # #             user_answer = 0  # If not a number, treat as wrong but gentle
# # #         if user_answer == correct_answer:
# # #             print(f"Yay! That's right! {num1} + {num2} = {correct_answer}! 🌟 You got a star!")
# # #             score += 1
# # #         else:
# # #             print(f"Oops! It's {correct_answer}. Keep practicing math! 😊")
    
# # #     elif category == "animal":
# # #         # Animal question: Color of animal name
# # #         animal = random.choice(list(animals_colors.keys()))
# # #         correct_color = animals_colors[animal]
# # #         print(f"Question {i+1} (Animal): What color is a {animal}?")
# # #         user_answer = input("Your color guess: ").strip().lower()
# # #         if user_answer == correct_color:
# # #             print(f"Yay! That's right! A {animal} is {correct_color}! 🐾 You got a star!")
# # #             score += 1
# # #         else:
# # #             print(f"Oops! A {animal} is usually {correct_color}. Animals are colorful! 😊")
    
# # #     else:  # category == "fruit"
# # #         # Fruit question: Color of fruit name
# # #         fruit = random.choice(list(fruits_colors.keys()))
# # #         correct_color = fruits_colors[fruit]
# # #         print(f"Question {i+1} (Fruit): What color is a {fruit}?")
# # #         user_answer = input("Your color guess: ").strip().lower()
# # #         if user_answer == correct_color:
# # #             print(f"Yay! That's right! A {fruit} is {correct_color}! 🍒 You got a star!")
# # #             score += 1
# # #         else:
# # #             print(f"Oops! A {fruit} is usually {correct_color}. Fruits are yummy colors! 😊")
    
# # #     print()  # Empty line for space

# # # # End of the game
# # # print(f"Adventure over! You got {score} out of {questions} correct. Amazing job with math, animals, and fruits! 🏆")
# # # if score == questions:
# # #     print("Perfect score! You're a super learner in everything! ⭐⭐⭐")
# # # elif score >= 3:
# # #     print("Awesome! You rock at math, animals, and fruits—keep exploring! 👍")
# # # else:
# # #     print("Good try! Play again to master more names and colors! 💪")



# # """
# # Team Tactics — Grid Game Prototype
# # Single-file Python prototype implementing:
# # - Map generation (tiles: Rock, Tree, Water, Depot)
# # - Characters: Commander, Warrior, Medic, SupplySoldier
# # - Pathfinding: A* (movement), BFS (safe zone search)
# # - Visibility map per character and merged Commander visibility
# # - Safety map (danger zones) using enemy sightings
# # - Simple AI behaviors and command system
# # - Console visualization (text grid) and a small simulation runner

# # How to run:
# #   python Team-Tactics-GridGame-ProofOfConcept.py

# # Notes:
# # - This is a proof-of-concept to demonstrate architecture and algorithms.
# # - Extensible to add Pygame / web UI later.
# # """

# # from __future__ import annotations
# # import random
# # import heapq
# # from typing import List, Tuple, Dict, Optional, Set
# # import math
# # import time

# # Point = Tuple[int,int]

# # # -------------------- Tile / Map Definitions --------------------
# # class TileType:
# #     EMPTY = '.'      # passable, visible
# #     ROCK  = '#'
# #     TREE  = 'T'      # passable but blocks visibility
# #     WATER = '~'      # impassable but does not block visibility (you can see across)
# #     DEPOT = 'D'      # depot for ammo/med

# # class Tile:
# #     def __init__(self, ttype: str = TileType.EMPTY):
# #         self.type = ttype
# #         self.passable = ttype in (TileType.EMPTY, TileType.TREE, TileType.DEPOT)
# #         # trees block visibility
# #         self.blocks_vision = ttype in (TileType.ROCK, TileType.TREE)

# # # -------------------- Map --------------------
# # class MapGrid:
# #     def __init__(self, w:int, h:int, rock_prob=0.08, tree_prob=0.12, water_prob=0.06, num_depots=2):
# #         self.w = w
# #         self.h = h
# #         self.grid: List[List[Tile]] = [[Tile() for _ in range(w)] for __ in range(h)]
# #         self.depots: List[Point] = []
# #         self.generate(rock_prob, tree_prob, water_prob, num_depots)

# #     def in_bounds(self, p:Point) -> bool:
# #         x,y = p
# #         return 0 <= x < self.w and 0 <= y < self.h

# #     def neighbors(self, p:Point) -> List[Point]:
# #         x,y = p
# #         candidates = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
# #         return [c for c in candidates if self.in_bounds(c) and self.grid[c[1]][c[0]].passable]

# #     def generate(self, rock_p, tree_p, water_p, num_depots):
# #         for y in range(self.h):
# #             for x in range(self.w):
# #                 r = random.random()
# #                 if r < rock_p:
# #                     self.grid[y][x] = Tile(TileType.ROCK)
# #                 elif r < rock_p + tree_p:
# #                     self.grid[y][x] = Tile(TileType.TREE)
# #                 elif r < rock_p + tree_p + water_p:
# #                     self.grid[y][x] = Tile(TileType.WATER)
# #                 else:
# #                     self.grid[y][x] = Tile(TileType.EMPTY)
# #         # place depots in passable locations
# #         placed = 0
# #         attempts = 0
# #         while placed < num_depots and attempts < 5000:
# #             attempts += 1
# #             x = random.randrange(self.w)
# #             y = random.randrange(self.h)
# #             if self.grid[y][x].passable and self.grid[y][x].type == TileType.EMPTY:
# #                 self.grid[y][x] = Tile(TileType.DEPOT)
# #                 self.depots.append((x,y))
# #                 placed += 1

# #     def tile_at(self, p:Point) -> Tile:
# #         x,y = p
# #         return self.grid[y][x]

# #     def display(self, characters:List['Character']=None, visibility:Optional[Set[Point]]=None):
# #         # build map of chars
# #         char_map: Dict[Point,str] = {}
# #         if characters:
# #             for ch in characters:
# #                 if ch.alive:
# #                     char_map[ch.pos] = ch.symbol
# #         lines = []
# #         for y in range(self.h):
# #             row = ''
# #             for x in range(self.w):
# #                 p = (x,y)
# #                 if visibility is not None and p not in visibility:
# #                     row += ' '  # unexplored / not visible
# #                 elif p in char_map:
# #                     row += char_map[p]
# #                 else:
# #                     row += self.tile_at(p).type
# #             lines.append(row)
# #         print('\n'.join(lines))

# # # -------------------- Pathfinding: A* and BFS --------------------

# # def heuristic(a:Point,b:Point) -> float:
# #     return abs(a[0]-b[0]) + abs(a[1]-b[1])

# # def a_star(grid:MapGrid, start:Point, goal:Point, avoid:Optional[Set[Point]]=None) -> Optional[List[Point]]:
# #     if avoid is None: avoid = set()
# #     if start == goal: return [start]
# #     open_heap = []
# #     heapq.heappush(open_heap, (0+heuristic(start,goal), 0, start, None))
# #     came_from: Dict[Point, Optional[Point]] = {start: None}
# #     gscore: Dict[Point, float] = {start: 0}

# #     while open_heap:
# #         f, g, current, _ = heapq.heappop(open_heap)
# #         if current == goal:
# #             path = []
# #             cur = current
# #             while cur is not None:
# #                 path.append(cur)
# #                 cur = came_from[cur]
# #             path.reverse()
# #             return path
# #         for nb in grid.neighbors(current):
# #             if nb in avoid:
# #                 continue
# #             tentative_g = gscore[current] + 1
# #             if nb not in gscore or tentative_g < gscore[nb]:
# #                 gscore[nb] = tentative_g
# #                 came_from[nb] = current
# #                 heapq.heappush(open_heap, (tentative_g + heuristic(nb,goal), tentative_g, nb, current))
# #     return None

# # from collections import deque

# # def bfs_find_nearest(grid:MapGrid, start:Point, condition) -> Optional[List[Point]]:
# #     # condition: fn(pos) -> bool
# #     q = deque()
# #     q.append(start)
# #     came_from = {start: None}
# #     while q:
# #         cur = q.popleft()
# #         if condition(cur):
# #             # build path
# #             path = []
# #             while cur is not None:
# #                 path.append(cur)
# #                 cur = came_from[cur]
# #             path.reverse()
# #             return path
# #         for nb in grid.neighbors(cur):
# #             if nb not in came_from:
# #                 came_from[nb] = cur
# #                 q.append(nb)
# #     return None

# # # -------------------- Visibility --------------------

# # def los_blocks(grid:MapGrid, a:Point, b:Point) -> bool:
# #     # simple bresenham line of sight: if any blocking tile between pts, return True
# #     x0,y0 = a; x1,y1 = b
# #     dx = abs(x1-x0)
# #     dy = -abs(y1-y0)
# #     sx = 1 if x0 < x1 else -1
# #     sy = 1 if y0 < y1 else -1
# #     err = dx + dy
# #     while True:
# #         if (x0,y0) != a and grid.tile_at((x0,y0)).blocks_vision:
# #             return True
# #         if (x0,y0) == (x1,y1): break
# #         e2 = 2*err
# #         if e2 >= dy:
# #             err += dy; x0 += sx
# #         if e2 <= dx:
# #             err += dx; y0 += sy
# #     return False

# # def visibility_from(grid:MapGrid, origin:Point, radius:int) -> Set[Point]:
# #     vis = set()
# #     ox,oy = origin
# #     for dx in range(-radius, radius+1):
# #         for dy in range(-radius, radius+1):
# #             x = ox + dx; y = oy + dy
# #             p = (x,y)
# #             if not grid.in_bounds(p): continue
# #             if dx*dx + dy*dy > radius*radius: continue
# #             # if line of sight is not blocked
# #             if not los_blocks(grid, origin, p):
# #                 vis.add(p)
# #     return vis

# # # -------------------- Safety Map --------------------

# # def compute_safety_map(grid:MapGrid, enemy_positions:List[Point], danger_radius=3) -> Dict[Point,float]:
# #     safety: Dict[Point,float] = {}
# #     for y in range(grid.h):
# #         for x in range(grid.w):
# #             p = (x,y)
# #             base = 0.0
# #             for e in enemy_positions:
# #                 d = math.hypot(e[0]-x, e[1]-y)
# #                 if d <= danger_radius:
# #                     base += max(0, (danger_radius - d) / danger_radius)
# #             safety[p] = base
# #     return safety

# # # -------------------- Characters --------------------
# # class Character:
# #     def __init__(self, name:str, pos:Point, team:int, symbol:str='?'):
# #         self.name = name
# #         self.pos = pos
# #         self.team = team
# #         self.symbol = symbol
# #         self.health = 100
# #         self.max_health = 100
# #         self.ammo = 10
# #         self.vision = 5
# #         self.alive = True
# #         self.path: Optional[List[Point]] = None

# #     def distance_to(self, p:Point) -> int:
# #         return abs(self.pos[0]-p[0]) + abs(self.pos[1]-p[1])

# #     def take_damage(self, dmg:int):
# #         self.health -= dmg
# #         if self.health <= 0:
# #             self.alive = False

# #     def step_along_path(self):
# #         if self.path and len(self.path) > 1:
# #             # first is current pos
# #             self.path.pop(0)
# #             self.pos = self.path[0]

# #     def report_status(self):
# #         return f"{self.name}(H:{self.health} A:{self.ammo})"

# # class Commander(Character):
# #     def __init__(self, name, pos, team):
# #         super().__init__(name,pos,team,'C')
# #         self.aggro_map: Dict[Point,float] = {}

# #     def decide(self, gm:'GameManager'):
# #         # Combine team vis to issue simple commands.
# #         # For demo: if any enemy visible, command nearest warrior to attack, medic to heal, supply to resupply.
# #         visible_enemies = gm.get_visible_enemies(self.team)
# #         my_team = gm.get_team(self.team)
# #         warriors = [c for c in my_team if isinstance(c,Warrior) and c.alive]
# #         medics = [c for c in my_team if isinstance(c,Medic) and c.alive]
# #         supplies = [c for c in my_team if isinstance(c,SupplySoldier) and c.alive]

# #         if visible_enemies and warriors:
# #             # pick the closest warrior to the nearest enemy
# #             enemy = visible_enemies[0]
# #             for w in warriors:
# #                 target_path = a_star(gm.grid, w.pos, enemy, avoid=gm.get_avoid_set())
# #                 if target_path:
# #                     w.path = target_path
# #                     w.current_goal = ('attack', enemy)
# #                     break
# #         else:
# #             # patrol: give a random nearby point
# #             for w in warriors:
# #                 if w.path is None or len(w.path) <= 1:
# #                     rx = max(0,min(gm.grid.w-1, w.pos[0] + random.randint(-6,6)))
# #                     ry = max(0,min(gm.grid.h-1, w.pos[1] + random.randint(-6,6)))
# #                     path = a_star(gm.grid, w.pos, (rx,ry), avoid=gm.get_avoid_set())
# #                     if path:
# #                         w.path = path
# #                         w.current_goal = ('patrol',(rx,ry))
# #         # medics and supplies reactively get commands when team reports low status in gm tick.

# # class Warrior(Character):
# #     def __init__(self, name, pos, team):
# #         super().__init__(name,pos,team,'W')
# #         self.current_goal = None

# #     def act(self, gm:'GameManager'):
# #         # If low ammo or health, report to commander
# #         if self.ammo <= 0 and gm.has_supply(self.team):
# #             # try to head to depot via supply soldier command
# #             self.current_goal = ('need_ammo', None)
# #         if self.health < 30:
# #             self.current_goal = ('need_heal', None)
# #         # If path is set, move
# #         if self.path:
# #             # if next tile is in high danger, attempt to replanning
# #             self.step_along_path()
# #         # if at target enemy and has ammo, fire
# #         visible_enemies = gm.get_visible_enemies(self.team_from(self),only_positions=False)
# #         if visible_enemies and self.ammo > 0:
# #             # find an enemy in range (melee range 1 or 2)
# #             for enemy in visible_enemies:
# #                 if self.distance_to(enemy) <= 2:
# #                     self.shoot(enemy)
# #                     break

# #     def shoot(self, enemy_pos:Point):
# #         if self.ammo <= 0: return
# #         self.ammo -= 1
# #         hit_chance = 0.6
# #         if random.random() < hit_chance:
# #             # caller will resolve damage via GameManager (we store target)
# #             self.last_shot_target = enemy_pos

# #     def team_from(self, _):
# #         return self.team

# # class Medic(Character):
# #     def __init__(self, name,pos,team):
# #         super().__init__(name,pos,team,'M')
# #         self.heal_amount = 40

# #     def act(self, gm:'GameManager'):
# #         # if has command to heal, follow path
# #         if self.path:
# #             self.step_along_path()
# #             # if reached someone injured
# #             for ally in gm.get_team(self.team):
# #                 if ally.alive and ally.health < ally.max_health and self.distance_to(ally) <= 1:
# #                     ally.health = min(ally.max_health, ally.health + self.heal_amount)

# # class SupplySoldier(Character):
# #     def __init__(self, name,pos,team):
# #         super().__init__(name,pos,team,'S')
# #         self.carry = 20

# #     def act(self, gm:'GameManager'):
# #         if self.path:
# #             self.step_along_path()
# #         # if adjacent to ally with low ammo, refill
# #         for ally in gm.get_team(self.team):
# #             if ally.alive and ally.ammo < 5 and self.distance_to(ally) <= 1:
# #                 needed = min(self.carry, 10 - ally.ammo)
# #                 ally.ammo += needed
# #                 self.carry -= needed

# # # -------------------- Game Manager --------------------
# # class GameManager:
# #     def __init__(self, w=30, h=18, teams=2):
# #         self.grid = MapGrid(w,h)
# #         self.teams = teams
# #         self.characters: List[Character] = []
# #         self.tick_count = 0
# #         self.init_teams()

# #     def init_teams(self):
# #         # spawn teams near opposite sides
# #         for t in range(self.teams):
# #             side_x = 2 if t == 0 else self.grid.w - 3
# #             # commander
# #             cpos = self.find_free_near((side_x, self.grid.h//2))
# #             cmd = Commander(f'Cmd{t}', cpos, t)
# #             self.characters.append(cmd)
# #             # warriors
# #             for i in range(3):
# #                 p = self.find_free_near((side_x, self.grid.h//2 + i + (t* -1)))
# #                 w = Warrior(f'W{t}_{i}', p, t)
# #                 self.characters.append(w)
# #             # medic
# #             mpos = self.find_free_near((side_x, self.grid.h//2 + 4))
# #             med = Medic(f'M{t}', mpos, t)
# #             self.characters.append(med)
# #             # supply
# #             spos = self.find_free_near((side_x, self.grid.h//2 - 4))
# #             sup = SupplySoldier(f'S{t}', spos, t)
# #             self.characters.append(sup)

# #     def find_free_near(self, center:Point, radius=4) -> Point:
# #         cx,cy = center
# #         for _ in range(2000):
# #             rx = max(0,min(self.grid.w-1, cx + random.randint(-radius, radius)))
# #             ry = max(0,min(self.grid.h-1, cy + random.randint(-radius, radius)))
# #             if self.grid.tile_at((rx,ry)).passable and not any(ch.pos == (rx,ry) for ch in self.characters):
# #                 return (rx,ry)
# #         # fallback
# #         for y in range(self.grid.h):
# #             for x in range(self.grid.w):
# #                 if self.grid.tile_at((x,y)).passable and not any(ch.pos == (x,y) for ch in self.characters):
# #                     return (x,y)
# #         return (0,0)

# #     def get_team(self, team:int) -> List[Character]:
# #         return [c for c in self.characters if c.team == team]

# #     def get_visible_enemies(self, team:int) -> List[Point]:
# #         # return a list of enemy positions visible by any of team's members (merge vis)
# #         vis = set()
# #         for c in self.get_team(team):
# #             if not c.alive: continue
# #             vis.update(visibility_from(self.grid, c.pos, c.vision))
# #         enemies = [e.pos for e in self.characters if e.team != team and e.alive and e.pos in vis]
# #         return enemies

# #     def has_supply(self, team:int) -> bool:
# #         return any(isinstance(c,SupplySoldier) and c.alive for c in self.get_team(team))

# #     def get_avoid_set(self) -> Set[Point]:
# #         # avoid water and rocks
# #         s = set()
# #         for y in range(self.grid.h):
# #             for x in range(self.grid.w):
# #                 t = self.grid.tile_at((x,y))
# #                 if not t.passable:
# #                     s.add((x,y))
# #         return s

# #     def tick(self):
# #         self.tick_count += 1
# #         # update commanders decisions
# #         for cmd in [c for c in self.characters if isinstance(c,Commander) and c.alive]:
# #             cmd.decide(self)
# #         # each character acts
# #         for ch in [c for c in self.characters if c.alive]:
# #             if isinstance(ch,Warrior):
# #                 ch.act(self)
# #             elif isinstance(ch,Medic):
# #                 ch.act(self)
# #             elif isinstance(ch,SupplySoldier):
# #                 ch.act(self)
# #         # resolve shots (simple: warriors who recorded last_shot_target)
# #         shots = []
# #         for w in [c for c in self.characters if isinstance(c,Warrior) and c.alive]:
# #             tgt = getattr(w, 'last_shot_target', None)
# #             if tgt:
# #                 shots.append((w,tgt))
# #                 delattr(w, 'last_shot_target')
# #         for shooter, tgt in shots:
# #             # find a character at target
# #             for victim in [c for c in self.characters if c.pos == tgt and c.team != shooter.team and c.alive]:
# #                 # apply damage
# #                 dmg = random.randint(20,40)
# #                 victim.take_damage(dmg)
# #         # simple auto-depot refill when on depot
# #         for ch in [c for c in self.characters if c.alive]:
# #             if self.grid.tile_at(ch.pos).type == TileType.DEPOT:
# #                 if isinstance(ch,SupplySoldier):
# #                     ch.carry = 20
# #                 else:
# #                     ch.ammo = min(10, ch.ammo + 3)
# #                     ch.health = min(ch.max_health, ch.health + 5)
# #         # remove dead: keep them but mark dead (symbol 'X')
# #         for ch in [c for c in self.characters if not c.alive]:
# #             ch.symbol = 'x'

# #     def get_all_visible(self, team:int) -> Set[Point]:
# #         vis = set()
# #         for c in self.get_team(team):
# #             if c.alive:
# #                 vis.update(visibility_from(self.grid, c.pos, c.vision))
# #         return vis

# #     def enemy_positions(self, team:int) -> List[Point]:
# #         return [c.pos for c in self.characters if c.team]
    







# import random
# from collections import deque

# # ----------------------------
# # Environment Module
# # ----------------------------
# TERRAINS = ['.', '#', 'T', '~', 'M', 'A']  # Empty, Rock, Tree, Water, Med Depot, Ammo Depot

# class Environment:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.map = [[random.choice(TERRAINS) for _ in range(width)] for _ in range(height)]

#     def display(self):
#         for row in self.map:
#             print(' '.join(row))
#         print()

# # ----------------------------
# # Pathfinding Module
# # ----------------------------
# class Pathfinding:
#     def __init__(self, env):
#         self.env = env

#     def is_valid(self, x, y):
#         return 0 <= x < self.env.height and 0 <= y < self.env.width and self.env.map[x][y] != '#'

#     def bfs(self, start, goal):
#         """Simple BFS pathfinding"""
#         queue = deque([start])
#         visited = {start: None}
#         while queue:
#             x, y = queue.popleft()
#             if (x, y) == goal:
#                 break
#             for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
#                 nx, ny = x + dx, y + dy
#                 if self.is_valid(nx, ny) and (nx, ny) not in visited:
#                     visited[(nx, ny)] = (x, y)
#                     queue.append((nx, ny))
#         return self.reconstruct_path(visited, goal)

#     def reconstruct_path(self, visited, goal):
#         path = []
#         node = goal
#         while node and node in visited:
#             path.append(node)
#             node = visited[node]
#         return path[::-1]

# # ----------------------------
# # Character Modules
# # ----------------------------
# class Character:
#     def __init__(self, role, x, y):
#         self.role = role
#         self.x = x
#         self.y = y
#         self.health = 100
#         self.ammo = 10

#     def move(self, new_x, new_y):
#         self.x, self.y = new_x, new_y
#         print(f"{self.role} moved to ({self.x}, {self.y})")

# class Commander(Character):
#     def plan_action(self):
#         print("Commander planning strategy...")

# class Warrior(Character):
#     def attack(self):
#         print("Warrior attacking the enemy!")

# class Medic(Character):
#     def heal(self, teammate):
#         print(f"Medic healing {teammate.role}...")

# class SupplySoldier(Character):
#     def resupply(self, teammate):
#         print(f"Supplying ammo to {teammate.role}...")

# # ----------------------------
# # Game Engine
# # ----------------------------
# class GameEngine:
#     def __init__(self):
#         self.env = Environment(5, 5)
#         self.pathfinder = Pathfinding(self.env)
#         self.commander = Commander("Commander", 0, 0)
#         self.warrior = Warrior("Warrior", 1, 1)
#         self.medic = Medic("Medic", 2, 2)
#         self.supply = SupplySoldier("Supply", 3, 3)

#     # def play_turn(self):
#     #     self.env.display()
#     #     self.commander.plan_action()
#     #     path = self.pathfinder.bfs((0,0), (4,4))
#     #     print("Path (BFS):", path)
#     #     self.warrior.attack()
#     #     self.medic.heal(self.warrior)
#     #     self.supply.resupply(self.warrior)

# # ----------------------------
# # Main Execution
# # ----------------------------
# if __name__ == "__main__":
#     game = GameEngine()
#     # game.play_turn()





# simple_wargame.py
# Simple console-based team strategy simulation demonstrating:
# - Grid map with tile types
# - A* pathfinding and BFS
# - Visibility & safety maps
# - Simple Commander + Warrior/Medic/Supply AIs
# - Combat, health, ammo, depots, and win/loss

import heapq
import random
import math
import time
from collections import deque, defaultdict, namedtuple

# ---------- Map / Tile Definitions ----------
W, H = 16, 10  # grid size (width x height)

Tile = namedtuple("Tile", ["char", "passable", "visible_through", "name"])
TILES = {
    "empty": Tile(".", True, True, "Empty"),
    "rock":  Tile("#", False, False, "Rock"),
    "tree":  Tile("T", True, False, "Tree"),
    "water": Tile("~", False, True, "Water"),
    "med":   Tile("M", True, True, "MedDepot"),
    "ammo":  Tile("A", True, True, "AmmoDepot"),
}

def make_default_map():
    grid = [["empty" for _ in range(W)] for _ in range(H)]
    # place random obstacles
    for _ in range(int(W*H*0.12)):
        x,y = random.randrange(W), random.randrange(H)
        grid[y][x] = random.choice(["rock","tree","water"])
    # place depots
    grid[1][1] = "med"
    grid[H-2][W-2] = "ammo"
    return grid

# ---------- Utilities ----------
def neighbors(pos):
    x,y = pos
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx,ny = x+dx, y+dy
        if 0 <= nx < W and 0 <= ny < H:
            yield (nx,ny)

def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# ---------- Pathfinding (A*) ----------
def astar(grid, start, goal, avoid=set(), cost_fn=None):
    # avoid: set of positions to penalize heavily or treat as blocked
    if start == goal:
        return [start]
    frontier = []
    heapq.heappush(frontier, (0+manhattan(start,goal), 0, start, None))
    came_from = {start: None}
    cost_so_far = {start: 0}
    while frontier:
        _, cost, current, _ = heapq.heappop(frontier)
        if current == goal:
            break
        for nb in neighbors(current):
            tx,ty = nb
            tile_name = grid[ty][tx]
            tile = TILES[tile_name]
            if not tile.passable:
                continue
            # high penalty for avoided squares
            step_cost = 1 + (100 if nb in avoid else 0)
            if cost_fn:
                step_cost += cost_fn(nb)
            new_cost = cost_so_far[current] + step_cost
            if nb not in cost_so_far or new_cost < cost_so_far[nb]:
                cost_so_far[nb] = new_cost
                priority = new_cost + manhattan(nb, goal)
                heapq.heappush(frontier, (priority, new_cost, nb, current))
                came_from[nb] = current
    if goal not in came_from:
        return None
    # reconstruct
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = came_from[cur]
    path.reverse()
    return path

# ---------- BFS for nearest safe zone ----------
def bfs_nearest(grid, start, condition_fn, avoid=set()):
    q = deque([start])
    prev = {start: None}
    while q:
        cur = q.popleft()
        if condition_fn(cur):
            # reconstruct
            path = []
            c = cur
            while c is not None:
                path.append(c)
                c = prev[c]
            return list(reversed(path))
        for nb in neighbors(cur):
            if nb in prev:
                continue
            tx,ty = nb
            tile_name = grid[ty][tx]
            if not TILES[tile_name].passable:
                continue
            if nb in avoid:
                continue
            prev[nb] = cur
            q.append(nb)
    return None

# ---------- Visibility & Safety ----------
def visibility_from(pos, grid, radius=4):
    visible = set()
    x0,y0 = pos
    for y in range(max(0, y0-radius), min(H, y0+radius+1)):
        for x in range(max(0, x0-radius), min(W, x0+radius+1)):
            # simple radius + line-of-sight blocking by non-visible-through tiles
            if manhattan(pos, (x,y)) <= radius:
                # raycast from pos to (x,y)
                blocked = False
                steps = max(abs(x-x0), abs(y-y0))
                if steps == 0:
                    visible.add((x,y))
                    continue
                for s in range(1, steps+1):
                    rx = round(x0 + (x-x0)*s/steps)
                    ry = round(y0 + (y-y0)*s/steps)
                    tile = TILES[grid[ry][rx]]
                    if s < steps and not tile.visible_through:
                        blocked = True
                        break
                if not blocked:
                    visible.add((x,y))
    return visible

def build_team_visibility(team_members, grid, radius=4):
    merged = set()
    for c in team_members:
        merged |= visibility_from(c.pos, grid, radius=radius)
    return merged

def build_safety_map(enemies, grid, danger_radius=3):
    danger = defaultdict(int)
    for e in enemies:
        for y in range(H):
            for x in range(W):
                d = manhattan((x,y), e.pos)
                if d <= danger_radius:
                    danger[(x,y)] += max(0, (danger_radius - d + 1))
    return danger  # higher value = more dangerous

# ---------- Characters ----------
class Character:
    def __init__(self, name, pos, team):
        self.name = name
        self.pos = pos
        self.team = team
        self.hp = 100
        self.max_hp = 100
        self.alive = True
        self.visible = set()
        self.role = "Character"
    def step(self, state): pass
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.alive = False
    def distance_to(self, other):
        return manhattan(self.pos, other.pos)
    def __repr__(self):
        return f"{self.name}({self.role})@{self.pos} HP:{self.hp}"

class Commander(Character):
    def __init__(self, name, pos, team):
        super().__init__(name,pos,team)
        self.role = "Commander"
        self.orders = {}  # target per unit
    def step(self, state):
        # process team visibility and safety, simple strategy:
        team = state['teams'][self.team]
        enemies = [e for e in state['units'] if e.team != self.team and e.alive]
        # merge visibility
        merged_vis = build_team_visibility([u for u in state['units'] if u.team==self.team and u.alive], state['grid'])
        self.visible = merged_vis
        safety = build_safety_map(enemies, state['grid'])
        # decide: if enemy visible and weak -> attack; if low hp -> call medic; if low ammo -> call supply
        for u in team:
            if not u.alive or u is self: 
                continue
            # simple status checks
            if isinstance(u, Warrior):
                # if sees enemy nearby -> attack that enemy
                visible_enemies = [e for e in enemies if e.pos in u.visible]
                if visible_enemies:
                    target = min(visible_enemies, key=lambda e:e.hp)
                    self.orders[u.name] = ("attack", target.pos)
                elif u.hp < 40:
                    self.orders[u.name] = ("defend", None)
                elif u.ammo < 2:
                    # order supply to refill
                    self.orders[u.name] = ("need_ammo", None)
                else:
                    # roam toward center
                    self.orders[u.name] = ("patrol", (W//2, H//2))
            elif isinstance(u, Medic):
                # find injured teammate
                injured = [m for m in team if m.alive and m.hp < m.max_hp and m is not u]
                if injured:
                    target = min(injured, key=lambda x: x.hp)
                    self.orders[u.name] = ("heal", target.pos)
                else:
                    self.orders[u.name] = ("idle", None)
            elif isinstance(u, SupplySoldier):
                lowammo = [m for m in team if isinstance(m,Warrior) and m.ammo < 3]
                if lowammo:
                    target = lowammo[0]
                    self.orders[u.name] = ("resupply", target.pos)
                else:
                    self.orders[u.name] = ("idle", None)

class Warrior(Character):
    def __init__(self,name,pos,team):
        super().__init__(name,pos,team)
        self.role = "Warrior"
        self.ammo = 6
        self.range = 3
        self.path = []
    def step(self, state):
        if not self.alive: return
        self.visible = visibility_from(self.pos, state['grid'], radius=4)
        enemies = [e for e in state['units'] if e.team != self.team and e.alive]
        # if enemy in range -> shoot
        for e in enemies:
            if manhattan(self.pos, e.pos) <= self.range and self.ammo>0:
                # fire
                dmg = random.randint(12,25)
                e.take_damage(dmg)
                self.ammo -= 1
                print(f"{self.name} fires at {e.name} for {dmg} dmg. Ammo left {self.ammo}")
                return
        # follow commander orders if alive commander exists
        commander = next((u for u in state['units'] if isinstance(u,Commander) and u.team==self.team and u.alive), None)
        if commander:
            order = commander.orders.get(self.name, ("patrol",(W//2,H//2)))
            otype, param = order
            if otype == "attack" and param:
                # path to target
                path = astar(state['grid'], self.pos, param, avoid=set([(p.pos) for p in state['units'] if p.team!=self.team and p.alive]))
                if path and len(path)>1:
                    self.pos = path[1]
                return
            elif otype == "defend":
                # BFS to nearest tile with low danger
                safety = build_safety_map(enemies, state['grid'])
                def safe_cond(p):
                    return safety.get(p,0) <= 1
                path = bfs_nearest(state['grid'], self.pos, safe_cond)
                if path and len(path)>1:
                    self.pos = path[1]
                return
            elif otype == "need_ammo":
                # move toward ammo depot
                ammo_pos = find_tile(state['grid'], "ammo")
                if ammo_pos:
                    path = astar(state['grid'], self.pos, ammo_pos)
                    if path and len(path)>1:
                        self.pos = path[1]
                return
            elif otype == "patrol" and param:
                path = astar(state['grid'], self.pos, param)
                if path and len(path)>1:
                    self.pos = path[1]
                return
        else:
            # autonomous roam
            self.pos = random.choice(list(self.visible)) if self.visible else self.pos

class Medic(Character):
    def __init__(self,name,pos,team):
        super().__init__(name,pos,team)
        self.role = "Medic"
        self.path = []
    def step(self, state):
        if not self.alive: return
        self.visible = visibility_from(self.pos, state['grid'], radius=4)
        commander = next((u for u in state['units'] if isinstance(u,Commander) and u.team==self.team and u.alive), None)
        if commander:
            order = commander.orders.get(self.name, ("idle",None))
            otype,param = order
            if otype == "heal" and param:
                # go to med depot first, then injured
                med_pos = find_tile(state['grid'], "med")
                path1 = astar(state['grid'], self.pos, med_pos) if med_pos else None
                if path1 and len(path1)>1:
                    self.pos = path1[1]; return
                # then to injured
                path2 = astar(state['grid'], self.pos, param)
                if path2 and len(path2)>1:
                    self.pos = path2[1]; return
                # if at injured, heal
                if manhattan(self.pos, param) == 0:
                    target = next((u for u in state['units'] if u.pos==param and u.team==self.team), None)
                    if target and target.alive:
                        healed = random.randint(18,30)
                        target.hp = min(target.max_hp, target.hp + healed)
                        print(f"{self.name} heals {target.name} for {healed} HP (now {target.hp}).")
                        return
            else:
                # idle: roam small
                choices = [p for p in neighbors(self.pos) if TILES[state['grid'][p[1]][p[0]]].passable]
                if choices:
                    self.pos = random.choice(choices)
                return

class SupplySoldier(Character):
    def __init__(self,name,pos,team):
        super().__init__(name,pos,team)
        self.role = "Supply"
    def step(self, state):
        if not self.alive: return
        self.visible = visibility_from(self.pos, state['grid'], radius=4)
        commander = next((u for u in state['units'] if isinstance(u,Commander) and u.team==self.team and u.alive), None)
        if commander:
            order = commander.orders.get(self.name, ("idle",None))
            otype,param = order
            if otype == "resupply" and param:
                ammo_pos = find_tile(state['grid'], "ammo")
                if ammo_pos and manhattan(self.pos, ammo_pos) > 0:
                    path = astar(state['grid'], self.pos, ammo_pos)
                    if path and len(path)>1:
                        self.pos = path[1]; return
                # otherwise move to target warrior
                path2 = astar(state['grid'], self.pos, param)
                if path2 and len(path2)>1:
                    self.pos = path2[1]; return
                # if at warrior, resupply
                t = next((u for u in state['units'] if u.pos==param and isinstance(u,Warrior) and u.team==self.team), None)
                if t and t.alive:
                    t.ammo = 6
                    print(f"{self.name} resupplies {t.name} to {t.ammo} ammo.")
                    return
            else:
                # idle roam
                choices = [p for p in neighbors(self.pos) if TILES[state['grid'][p[1]][p[0]]].passable]
                if choices:
                    self.pos = random.choice(choices)
                return

# ---------- Helper ----------
def find_tile(grid, tile_key):
    for y in range(H):
        for x in range(W):
            if grid[y][x] == tile_key:
                return (x,y)
    return None

# ---------- Simulation Setup ----------
def place_team(grid, team_id, x_off=0, y_off=0):
    units = []
    # commander
    units.append(Commander(f"C{team_id}", (1 + x_off, 1 + y_off), team_id))
    units.append(Warrior(f"W{team_id}a", (2 + x_off, 1 + y_off), team_id))
    units.append(Warrior(f"W{team_id}b", (1 + x_off, 2 + y_off), team_id))
    units.append(Medic(f"M{team_id}", (2 + x_off, 2 + y_off), team_id))
    units.append(SupplySoldier(f"S{team_id}", (3 + x_off, 2 + y_off), team_id))
    return units

def render(grid, units):
    # minimal textual render
    unit_pos = {u.pos: u for u in units if u.alive}
    lines = []
    for y in range(H):
        row = ""
        for x in range(W):
            if (x,y) in unit_pos:
                u = unit_pos[(x,y)]
                symbol = u.name[0]
                if isinstance(u,Commander): symbol = "K"
                if isinstance(u,Warrior): symbol = "W"
                if isinstance(u,Medic): symbol = "M"
                if isinstance(u,SupplySoldier): symbol = "S"
                row += symbol
            else:
                row += TILES[grid[y][x]].char
        lines.append(row)
    print("\n".join(lines))
    # status
    for u in units:
        status = "DEAD" if not u.alive else f"HP:{u.hp} "
        if isinstance(u,Warrior):
            status += f"Ammo:{u.ammo}"
        print(f"{u.name:6} {u.role:8} {u.team} Pos:{u.pos} {status}")
    print("-"*40)

# ---------- Create State ----------
random.seed(1)
grid = make_default_map()
# place teams on opposite corners
team0 = place_team(grid, 0, x_off=0, y_off=0)
team1 = place_team(grid, 1, x_off=W-5, y_off=H-4)
units = team0 + team1

state = {
    'grid': grid,
    'units': units,
    'teams': {0: team0, 1: team1}
}

# ---------- Simulation Loop ----------
def simulate_turn(state, max_turns=200):
    for turn in range(1, max_turns+1):
        print(f"\nTURN {turn}")
        render(state['grid'], state['units'])
        # check win
        teams_alive = {t: any(u.alive for u in members) for t,members in state['teams'].items()}
        alive_teams = [t for t,alive in teams_alive.items() if alive]
        if len(alive_teams) <= 1:
            print("Game Over. Winner:", alive_teams[0] if alive_teams else "None")
            break
        # each unit steps (simple initiative: team0 then team1)
        for u in list(state['units']):
            if u.alive:
                u.step(state)
        # simple enemy AI: enemy warriors will also try to engage visible enemies
        # done inside their step via commander orders or autonomously
        # small chance spawn random enemy action to keep things lively
        # cleanup dead units
        for u in state['units']:
            if u.alive and u.hp <= 0:
                u.alive = False
        time.sleep(0.08)
    else:
        print("Reached max turns.")

if __name__ == "__main__":
    simulate_turn(state)

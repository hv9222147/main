
# import random  # For random choices when multiple paths are available
# class VirtualCharacter:
#     def __init__(self, maze, start_pos, goal_pos):
#         self.maze = maze  # The maze grid (0 = open path, 1 = wall, 2 = goal)
#         self.position = start_pos  # Starting position (row, col)
#         self.goal = goal_pos  # Goal position (row, col)
#         self.visited = set()  # Memory: tracks visited positions to avoid loops
#         self.path = []  # Records the path taken for backtracking if needed
    
#     def is_valid_move(self, row, col):
#         # Check if a move is safe (within bounds, not a wall, not visited to avoid loops)
#         rows, cols = len(self.maze), len(self.maze[0])
#         return (0 <= row < rows and 0 <= col < cols and
#                 self.maze[row][col] != 1 and  # Not a wall
#                 (row, col) not in self.visited)  # Not visited before
    
#     def get_possible_moves(self):
#         # Intelligent decision: Find all valid next moves
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
#         moves = []
#         for dr, dc in directions:
#             new_row, new_col = self.position[0] + dr, self.position[1] + dc
#             if self.is_valid_move(new_row, new_col):
#                 # Prioritize moves closer to goal (simple distance check for "intelligence")
#                 distance_to_goal = abs(new_row - self.goal[0]) + abs(new_col - self.goal[1])
#                 moves.append((new_row, new_col, distance_to_goal))
#         # Sort by distance to goal (smallest first) for smarter choice
#         moves.sort(key=lambda x: x[2])
#         return moves
    
#     def move(self):
#         # Main intelligent behavior: Choose and make the best move
#         possible_moves = self.get_possible_moves()
#         if not possible_moves:
#             print("No valid moves! Stuck.")
#             return False
        
#         # Pick the smartest move (closest to goal)
#         best_move = possible_moves[0][:2]  # (row, col)
#         self.position = best_move
#         self.visited.add(best_move)
#         self.path.append(best_move)
#         print(f"Character moved to: {best_move}")
        
#         # Check if goal reached
#         if best_move == self.goal:
#             print("Goal reached! Intelligent navigation successful.")
#             return True
#         return False
    
   
# # Example maze (5x5 grid): 0=open, 1=wall, 2=goal
# maze = [
#     [0, 0, 1, 0, 0],
#     [1, 0, 1, 0, 1],
#     [0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 1, 2]  # 2 is the goal
# ]
# # Create and run the virtual character
# start = (0, 0)  # Start at top-left
# goal = (4, 4)   # Goal at bottom-right
# character = VirtualCharacter(maze, start, goal)
# print("Starting maze exploration...")
# print("Maze layout:")
# for row in maze:
#     print(row)
# steps = 0
# max_steps = 20  # Prevent infinite loops
# while steps < max_steps:
#     if character.move():
#         break
#     steps += 1
# print(f"Path taken: {character.path}")
# print("Exploration complete.")


#!/usr/bin/env python3
"""
battle_sim.py — corrected single-file tactical team simulation.

Features:
- Grid map with Rocks (impassable, block vision), Trees (passable, block vision),
  Water (impassable, does NOT block vision), Depots (ammo/med).
- Characters: Commander, Warrior, Medic, SupplySoldier
- A* pathfinding (considers safety map cost), BFS for nearest depot
- Visibility (bresenham), safety map (enemy proximity), simple AI
- ASCII UI printed each tick

This file fixes multiple issues in the original submission: misplaced/duplicated
functions, missing methods, inconsistent indentation, and other bugs.
"""

import random
import heapq
from collections import deque, defaultdict
from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional, Set

# -----------------------
# Constants / Tile types
# -----------------------
ROCK = '#'
TREE = 'T'
WATER = '~'
EMPTY = '.'
MED_DEPOT = 'M'
AMMO_DEPOT = 'A'
    
TILE_PASSABLE = {
    ROCK: False,
    WATER: False,
    TREE: True,
    EMPTY: True,
    MED_DEPOT: True,
    AMMO_DEPOT: True,
}

TILE_BLOCKS_VISION = {
    ROCK: True,
    TREE: True,
    WATER: False,
    EMPTY: False,
    MED_DEPOT: False,
    AMMO_DEPOT: False,
}

# -----------------------
# Utility functions
# -----------------------

def neighbors(pos, w, h):
    x, y = pos
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < w and 0 <= ny < h:
            yield (nx, ny)


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def bresenham_line(a, b):
    # returns list of integer points between a (inclusive) and b (inclusive)
    x0, y0 = a
    x1, y1 = b
    points = []
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy
    return points

# -----------------------
# MapGrid
# -----------------------
class MapGrid:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        # grid[x][y] layout (width-major) — this is consistent across code
        self.grid = [[EMPTY for _ in range(height)] for _ in range(width)]
        self._place_random_obstacles()

    def _place_random_obstacles(self):
        # For demo: scatter some rocks, trees, water, and depots
        for x in range(self.w):
            for y in range(self.h):
                r = random.random()
                if r < 0.06:
                    self.grid[x][y] = ROCK
                elif r < 0.14:
                    self.grid[x][y] = TREE
                elif r < 0.18:
                    self.grid[x][y] = WATER
                # else empty
        # place depots
        for _ in range(2):
            self._place_tile_random(MED_DEPOT)
            self._place_tile_random(AMMO_DEPOT)

    def _place_tile_random(self, tile):
        for _ in range(200):
            x = random.randrange(self.w)
            y = random.randrange(self.h)
            if self.grid[x][y] == EMPTY:
                self.grid[x][y] = tile
                return

    def in_bounds(self, pos):
        x, y = pos
        return 0 <= x < self.w and 0 <= y < self.h

    def passable(self, pos):
        x, y = pos
        return TILE_PASSABLE[self.grid[x][y]]

    def blocks_vision(self, pos):
        x, y = pos
        return TILE_BLOCKS_VISION[self.grid[x][y]]

    def tile(self, pos):
        x, y = pos
        return self.grid[x][y]

    def display_with_units(self, units: List['Character'], visibility: Optional[Set[Tuple[int, int]]] = None):
        # Build map of chars (positions to symbols)
        unit_map = {}
        for u in units:
            if u.alive:
                unit_map[u.pos] = u
        rows = []
        for y in range(self.h):
            row = ''
            for x in range(self.w):
                if visibility is not None and (x, y) not in visibility:
                    row += ' '
                    continue
                if (x, y) in unit_map:
                    row += unit_map[(x, y)].symbol
                else:
                    row += self.grid[x][y]
            rows.append(row)
        return '\n'.join(rows)

# -----------------------
# Pathfinding: A* and BFS
# -----------------------

def a_star(grid: MapGrid, start, goal, safety_map: Optional[Dict[Tuple[int, int], float]] = None):
    """A* that considers safety_map as an extra cost (higher is worse). Returns path list (start..goal) or []"""
    w, h = grid.w, grid.h

    def move_cost(a, b):
        base = 1
        extra = safety_map.get(b, 0) if safety_map else 0
        return base + extra * 2.0  # weight safety more

    frontier = []
    heapq.heappush(frontier, (manhattan(start, goal), 0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, cur_cost, current = heapq.heappop(frontier)
        if current == goal:
            break
        for n in neighbors(current, w, h):
            if not grid.passable(n):
                continue
            new_cost = cost_so_far[current] + move_cost(current, n)
            if n not in cost_so_far or new_cost < cost_so_far[n]:
                cost_so_far[n] = new_cost
                priority = new_cost + manhattan(n, goal)
                heapq.heappush(frontier, (priority, new_cost, n))
                came_from[n] = current

    if goal not in came_from:
        return []
    # reconstruct
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = came_from[cur]
    path.reverse()
    return path


def bfs_find_nearest(grid: MapGrid, start, predicate):
    """BFS to find nearest tile satisfying predicate; returns position or None"""
    w, h = grid.w, grid.h
    q = deque([start])
    seen = {start}
    while q:
        cur = q.popleft()
        if predicate(cur):
            return cur
        for n in neighbors(cur, w, h):
            if n not in seen and grid.passable(n):
                seen.add(n)
                q.append(n)
    return None

# -----------------------
# Characters
# -----------------------
@dataclass
class Character:
    id: int
    team: int
    name: str
    pos: Tuple[int, int]
    hp: int = 100
    ammo: int = 10
    alive: bool = True
    symbol: str = '?'
    sight_range: int = 5

    def is_enemy(self, other: 'Character'):
        return self.team != other.team

    def in_range(self, target: 'Character', rng: int):
        return manhattan(self.pos, target.pos) <= rng

    def receive_damage(self, dmg):
        if not self.alive:
            return
        self.hp -= dmg
        if self.hp <= 0:
            self.alive = False
            self.hp = 0

    def heal(self, amount):
        if not self.alive:
            return
        self.hp = min(100, self.hp + amount)

    def refill_ammo(self, amount):
        if not self.alive:
            return
        self.ammo += amount


class Commander(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = 'C'
        self.sight_range = 7
        self.orders = {}  # id -> order

    def issue_orders(self, gm: 'GameManager'):
        # Simple strategy:
        # - If any warrior low on ammo -> order resupply
        # - If any friendly wounded -> order medic
        # - If sees enemy close -> order attack
        # - else hold/advance toward center
        for unit in gm.units_by_team(self.team):
            if not unit.alive:
                continue
            if isinstance(unit, Warrior):
                if unit.ammo < 3:
                    depot = gm.find_nearest_depot(unit.pos, AMMO_DEPOT)
                    if depot:
                        self.orders[unit.id] = ('resupply', depot)
                        continue
                visible_enemies = gm.visible_enemies_for(self.team)
                if visible_enemies:
                    target = min(visible_enemies, key=lambda e: manhattan(unit.pos, e.pos))
                    self.orders[unit.id] = ('attack', target.pos)
                    continue
                center = (gm.map.w // 2, gm.map.h // 2)
                self.orders[unit.id] = ('advance', center)
            elif isinstance(unit, Medic):
                wounded = [u for u in gm.units_by_team(self.team) if u.alive and u.hp < 80]
                if wounded:
                    target = min(wounded, key=lambda u: u.hp)
                    self.orders[unit.id] = ('heal', target)
                else:
                    self.orders[unit.id] = ('guard', unit.pos)
            elif isinstance(unit, SupplySoldier):
                low_ammo = [u for u in gm.units_by_team(self.team) if isinstance(u, Warrior) and u.alive and u.ammo < 4]
                if low_ammo:
                    target = min(low_ammo, key=lambda u: u.ammo)
                    self.orders[unit.id] = ('resupply_warrior', target)
                else:
                    self.orders[unit.id] = ('guard', unit.pos)


class Warrior(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = 'W'
        self.sight_range = 5
        self.attack_range = 1
        self.damage = 35

    def step(self, gm: 'GameManager'):
        if not self.alive:
            return
        cmd = gm.commander_for(self.team)
        order = cmd.orders.get(self.id) if cmd else None
        if order:
            typ, target = order
            if typ == 'attack':
                if manhattan(self.pos, target) > self.attack_range:
                    path = a_star(gm.map, self.pos, target, gm.safety_map_for(self.team))
                    if len(path) >= 2:
                        self.pos = path[1]
                else:
                    enemies = [e for e in gm.units if e.alive and e.team != self.team and self.in_range(e, self.attack_range)]
                    if enemies and self.ammo > 0:
                        target_e = min(enemies, key=lambda e: e.hp)
                        target_e.receive_damage(self.damage)
                        self.ammo = max(0, self.ammo - 1)
            elif typ == 'resupply':
                depot = target
                if self.pos == depot:
                    pass
                else:
                    path = a_star(gm.map, self.pos, depot, gm.safety_map_for(self.team))
                    if len(path) >= 2:
                        self.pos = path[1]
            elif typ == 'advance':
                dest = target
                if self.pos != dest:
                    path = a_star(gm.map, self.pos, dest, gm.safety_map_for(self.team))
                    if len(path) >= 2:
                        self.pos = path[1]
            elif typ == 'guard':
                pass
        else:
            visible = gm.visibility_for(self.team)
            enemies = [e for e in gm.units if e.alive and e.team != self.team and e.pos in visible]
            if enemies:
                target_e = min(enemies, key=lambda e: manhattan(self.pos, e.pos))
                if manhattan(self.pos, target_e.pos) > self.attack_range:
                    path = a_star(gm.map, self.pos, target_e.pos, gm.safety_map_for(self.team))
                    if len(path) >= 2:
                        self.pos = path[1]
                else:
                    if self.ammo > 0:
                        target_e.receive_damage(self.damage)
                        self.ammo = max(0, self.ammo - 1)
            else:
                for n in neighbors(self.pos, gm.map.w, gm.map.h):
                    if gm.map.passable(n) and random.random() < 0.2 and not gm.unit_at(n):
                        self.pos = n
                        break


class Medic(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = 'H'
        self.heal_amount = 30
        self.sight_range = 5

    def step(self, gm: 'GameManager'):
        if not self.alive:
            return
        cmd = gm.commander_for(self.team)
        order = cmd.orders.get(self.id) if cmd else None
        if order and order[0] == 'heal':
            target: Character = order[1]
            if not target.alive:
                return
            path = a_star(gm.map, self.pos, target.pos, gm.safety_map_for(self.team))
            if len(path) >= 2:
                self.pos = path[1]
            else:
                if manhattan(self.pos, target.pos) <= 1:
                    target.heal(self.heal_amount)
        else:
            friends = [u for u in gm.units_by_team(self.team) if u.alive and u.hp < 80]
            if friends:
                target = min(friends, key=lambda u: u.hp)
                if manhattan(self.pos, target.pos) > 1:
                    path = a_star(gm.map, self.pos, target.pos, gm.safety_map_for(self.team))
                    if len(path) >= 2:
                        self.pos = path[1]
                else:
                    target.heal(self.heal_amount)
            else:
                pass


class SupplySoldier(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symbol = 'S'
        self.sight_range = 5

    def step(self, gm: 'GameManager'):
        if not self.alive:
            return
        cmd = gm.commander_for(self.team)
        order = cmd.orders.get(self.id) if cmd else None
        if order:
            typ = order[0]
            if typ == 'resupply_warrior':
                target: Character = order[1]
                if not target.alive:
                    return
                depot = gm.find_nearest_depot(self.pos, AMMO_DEPOT)
                if depot and self.pos != depot:
                    path = a_star(gm.map, self.pos, depot, gm.safety_map_for(self.team))
                    if len(path) >= 2:
                        self.pos = path[1]
                        return
                if target.alive:
                    path = a_star(gm.map, self.pos, target.pos, gm.safety_map_for(self.team))
                    if len(path) >= 2:
                        self.pos = path[1]
                    else:
                        if manhattan(self.pos, target.pos) <= 1:
                            target.refill_ammo(6)
            elif typ == 'guard':
                pass
        else:
            low_ammo = [u for u in gm.units_by_team(self.team) if isinstance(u, Warrior) and u.alive and u.ammo < 3]
            if low_ammo:
                target = min(low_ammo, key=lambda u: u.ammo)
                depot = gm.find_nearest_depot(self.pos, AMMO_DEPOT)
                if depot and self.pos != depot:
                    path = a_star(gm.map, self.pos, depot, gm.safety_map_for(self.team))
                    if len(path) >= 2:
                        self.pos = path[1]
                        return
                path = a_star(gm.map, self.pos, target.pos, gm.safety_map_for(self.team))
                if len(path) >= 2:
                    self.pos = path[1]
                else:
                    if manhattan(self.pos, target.pos) <= 1:
                        target.refill_ammo(5)


# -----------------------
# Game Manager
# -----------------------
class GameManager:
    def __init__(self, width=20, height=12):
        self.map = MapGrid(width, height)
        self.units: List[Character] = []
        self.next_id = 1
        self.turn = 0
        # caches
        self._visibility_cache: Dict[int, Set[Tuple[int, int]]] = {}
        self._safety_map_cache: Dict[int, Dict[Tuple[int, int], float]] = {}
        self._safety_map_cache_turn = -1

    def spawn_team(self, team: int, base_pos: Tuple[int, int]):
        c = Commander(self.next_id, team, f'Commander{team}', base_pos)
        self.next_id += 1
        w1 = Warrior(self.next_id, team, f'Warrior{team}_1', self._nearby_free(base_pos))
        self.next_id += 1
        w2 = Warrior(self.next_id, team, f'Warrior{team}_2', self._nearby_free(base_pos))
        self.next_id += 1
        m = Medic(self.next_id, team, f'Medic{team}', self._nearby_free(base_pos))
        self.next_id += 1
        s = SupplySoldier(self.next_id, team, f'Supply{team}', self._nearby_free(base_pos))
        self.next_id += 1
        for u in (c, w1, w2, m, s):
            self.units.append(u)

    def _nearby_free(self, pos):
        for n in neighbors(pos, self.map.w, self.map.h):
            if self.map.passable(n) and not self.unit_at(n):
                return n
        for _ in range(200):
            x = random.randrange(self.map.w)
            y = random.randrange(self.map.h)
            if self.map.passable((x, y)) and not self.unit_at((x, y)):
                return (x, y)
        return pos

    def unit_at(self, pos):
        for u in self.units:
            if u.alive and u.pos == pos:
                return u
        return None

    def units_by_team(self, team):
        return [u for u in self.units if u.team == team and u.alive]

    def commander_for(self, team) -> Optional[Commander]:
        for u in self.units:
            if isinstance(u, Commander) and u.team == team and u.alive:
                return u
        return None

    def find_nearest_depot(self, pos, tile_type):
        return bfs_find_nearest(self.map, pos, lambda p: self.map.tile(p) == tile_type)

    def visible_positions_for_unit(self, unit: Character) -> Set[Tuple[int, int]]:
        vis = set()
        r = unit.sight_range
        for dx in range(-r, r + 1):
            for dy in range(-r, r + 1):
                x, y = unit.pos[0] + dx, unit.pos[1] + dy
                if not self.map.in_bounds((x, y)):
                    continue
                if manhattan(unit.pos, (x, y)) > r:
                    continue
                line = bresenham_line(unit.pos, (x, y))
                blocked = False
                for p in line:
                    if p == unit.pos:
                        continue
                    if self.map.blocks_vision(p):
                        blocked = True
                        break
                if not blocked:
                    vis.add((x, y))
        return vis

    def visibility_for(self, team: int) -> Set[Tuple[int, int]]:
        vis = set()
        for u in self.units_by_team(team):
            vis |= self.visible_positions_for_unit(u)
        return vis

    def visible_enemies_for(self, team: int) -> List[Character]:
        vis = self.visibility_for(team)
        enemies = [u for u in self.units if u.alive and u.team != team and u.pos in vis]
        return enemies

    def safety_map_for(self, team: int) -> Dict[Tuple[int, int], float]:
        # safety map: higher value = more dangerous. Cache per turn.
        key = team
        if key in self._safety_map_cache and self._safety_map_cache_turn == self.turn:
            return self._safety_map_cache[key]
        danger = defaultdict(float)
        enemies = [u for u in self.units if u.alive and u.team != team]
        for x in range(self.map.w):
            for y in range(self.map.h):
                pos = (x, y)
                if not self.map.passable(pos):
                    danger[pos] = 999.0
                    continue
                nearest = min((manhattan(pos, e.pos) for e in enemies), default=999)
                if nearest == 0:
                    danger[pos] = 10.0
                else:
                    danger[pos] = max(0.0, 3.0 - (1.0 * nearest / 3.0))
        self._safety_map_cache[key] = danger
        self._safety_map_cache_turn = self.turn
        return danger

    def step(self):
        self.turn += 1
        # commanders issue orders first
        for cmd in [u for u in self.units if isinstance(u, Commander) and u.alive]:
            cmd.issue_orders(self)

        # each unit acts
        for u in list(self.units):
            if isinstance(u, Warrior):
                u.step(self)
            elif isinstance(u, Medic):
                u.step(self)
            elif isinstance(u, SupplySoldier):
                u.step(self)
            elif isinstance(u, Commander):
                if random.random() < 0.05:
                    for n in neighbors(u.pos, self.map.w, self.map.h):
                        if self.map.passable(n) and not self.unit_at(n):
                            u.pos = n
                            break

    def is_game_over(self) -> bool:
        teams_alive = set(u.team for u in self.units if u.alive)
        return len(teams_alive) <= 1

    def winner(self) -> Optional[int]:
        teams_alive = set(u.team for u in self.units if u.alive)
        return next(iter(teams_alive)) if len(teams_alive) == 1 else None

    def print_state(self):
        team = 1
        cmd = self.commander_for(team)
        vis = self.visibility_for(team) if cmd else None
        print(f"Turn {self.turn} | Units alive: {sum(1 for u in self.units if u.alive)}")
        print(self.map.display_with_units(self.units, visibility=vis))
        for u in self.units:
            status = f"{u.name:12s} team{u.team} pos={u.pos} hp={u.hp:3d} ammo={u.ammo:2d} {'ALIVE' if u.alive else 'DEAD'}"
            if isinstance(u, Commander):
                status += f" orders={list(u.orders.values())[:3]}"
            print(status)
        print('-' * 60)


# -----------------------
# Run a small simulation
# -----------------------

def run_demo(seed=1, max_turns=200):
    random.seed(seed)
    gm = GameManager(20, 12)
    gm.spawn_team(1, (1, 1))
    gm.spawn_team(2, (gm.map.w - 2, gm.map.h - 2))
    for _ in range(max_turns):
        gm.print_state()
        if gm.is_game_over():
            break
        gm.step()
    print("Final state:")
    gm.print_state()
    w = gm.winner()
    if w:
        print(f"Team {w} wins!")
    else:
        print("The team status is incomplete.")


if __name__ == '__main__':
    run_demo(seed=42, max_turns=200)
                                                                                                                                                                    
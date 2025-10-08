import random
import heapq
from collections import deque
from dataclasses import dataclass
from typing import List, Dict


class constraint:
    max_ammo = 30
    max_health = 100
    revive_threshold = 20
    map_size = (20,12)


class requirements:
    objective : list[str]
    roles: dict[str,str]
    functional_requirement: list[str]
    constraint: constraint


class gridmap:
    def __init__(self,width,height,obstacle_prob=0.15):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

        for y in range(height): 
            for x in range(width):
                if random.random()< obstacle_prob:
                    self.grid[y][x] = 1
    
    def display(self):
        for row in self.grid:
            print("".join("#"if cell else "." for cell in row))



def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def a_star_search(grid, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal:
            break
        neighbors = [(current[0]+dx, current[1]+dy) for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]]
        for nxt in neighbors:
            x,y = nxt
            if 0 <= x < grid.width and 0 <= y < grid.height and grid.grid[y][x] == 0:
                new_cost = cost_so_far[current]+1
                if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                    cost_so_far[nxt] = new_cost
                    priority = new_cost + manhattan(nxt, goal)
                    heapq.heappush(frontier, (priority, nxt))
                    came_from[nxt] = current
    if goal not in came_from:
        return None
    # Reconstruct path
    path=[]
    cur=goal
    while cur:
        path.append(cur)
        cur=came_from[cur]
    return path[::-1]

def bfs(grid, start, goal):
    q = deque([start])
    came_from = {start: None}
    while q:
        cur = q.popleft()
        if cur == goal: break
        neighbors = [(cur[0]+dx, cur[1]+dy) for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]]
        for nxt in neighbors:
            x,y = nxt
            if 0 <= x < grid.width and 0 <= y < grid.height and grid.grid[y][x]==0:
                if nxt not in came_from:
                    came_from[nxt] = cur
                    q.append(nxt)
    if goal not in came_from: return None
    path=[]
    cur=goal
    while cur:
        path.append(cur)
        cur=came_from[cur]
    return path[::-1]


class agent:
    def __init__(self,name,pos,health=100,ammo=10):
        self.name= name
        self.pos = pos
        self.health = health
        self.ammo = ammo


class warrior(agent):
    def attack(self,target_pos):
        if   self.ammo > 0:
            print(f"{self.ammo}attack at{target_pos}")
            self.ammo -= 1


class medic(agent):
    def heal(self,ally):
        if ally.health < 100:
            print(f"{self.name} heals {ally.name}")
            self.ally +=20



def compute_visibility(grid, source, radius=6):
    visible = set()
    sx,sy = source
    for y in range(max(0,sy-radius), min(grid.height, sy+radius+1)):
        for x in range(max(0,sx-radius), min(grid.width, sx+radius+1)):
            if grid.grid[y][x]==0:
                visible.add((x,y))
    return visible

def compute_safety(grid, enemy_positions, radius=4):
    danger=[[0]*grid.width for _ in range(grid.height)]
    for y in range(grid.height):
        for x in range(grid.width):
            for ex,ey in enemy_positions:
                d = ((x-ex)**2 + (y-ey)**2)**0.5
                if d<=radius:
                    danger[y][x]+=int((radius-d)*10)
    return danger


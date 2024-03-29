from heapq import *

file = "input.txt"

lines = [l.strip() for l in open(file).readlines()]

data = {}
goal = []
for y, l in enumerate(lines):
    for x, risk in enumerate(l):
        data[(x, y)] = int(risk)
        goal.append((x, y))
goal.sort()
goal = goal[-1]


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

#A*
front = []
start = (0, 0)
heappush(front, (0, start))
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[start] = 0

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while front:
    curr = heappop(front)
    if curr == goal:
        break
    ns = [
        (curr[1][0] + x, curr[1][1] + y)
        for x, y in dirs
        if (curr[1][0] + x, curr[1][1] + y) in data
    ]
    for next in ns:
        new_cost = cost_so_far[curr[1]] + data[next]
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
            priority = new_cost + heuristic(goal, next)
            heappush(front, (priority, next))
            came_from[next] = curr
print(cost_so_far[goal])

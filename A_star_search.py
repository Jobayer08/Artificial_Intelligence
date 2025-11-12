from queue import PriorityQueue
def a_star_search(graph, start, goal, h):
    open_set= PriorityQueue()
    open_set.put((0+h[start], start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while not open_set.empty():
        f_current,current= open_set.get()

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + h[neighbor]
                open_set.put((f_score, neighbor))
    return None            

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 4, 'E': 2},
    'C': {'F': 5},
    'D': {'F': 3},
    'E': {'F': 1},
    'F': {}
}

# Heuristic
h = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 0
}

start = 'A'
goal = 'F'

path = a_star_search(graph, start, goal, h)
print("A* path:", path)
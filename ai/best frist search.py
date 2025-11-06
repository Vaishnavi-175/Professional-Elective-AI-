from queue import PriorityQueue

# Best First Search Algorithm

def best_first_search(graph, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start))   # (cost, node)

    while not pq.empty():
        cost, node = pq.get()
        if node == goal:
            print(f"Goal {goal} found!")
            return
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    pq.put((weight, neighbor))

# Example graph represented as adjacency list
graph = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('E', 5)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 5)],
    'G': []
}

print("Best First Search path:")
best_first_search(graph, 'A', 'G')
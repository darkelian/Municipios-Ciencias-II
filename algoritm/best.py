import heapq

def greedyBestFirstSearch(graph,initial, goal,position):
    #Estructura
    openSet = [(0, initial)]  # (fCost, nodo)
    cameFrom = {}
    
    def heuristic(node,position):
        return ((position[node]))
    
    while openSet:
        current=heapq.heappop(openSet)[1]#menor costo del openSet
        
        if current ==goal:#hacer el camino
            path=[current]
            while current != initial:
                current = cameFrom[current]
                path.append(current)
            return path[::-1]
        #Ver vecinos
        for neighbor, cost in graph[current].items():
            if neighbor not in cameFrom:
                cameFrom[neighbor] = current
                heapq.heappush(openSet, (heuristic(neighbor, position), neighbor))

    return None#Sin camino
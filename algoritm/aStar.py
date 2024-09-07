import heapq
def aStar(graph,initial, goal,position):
    #Estructura
    openSet = [(0, initial)]  # (fCost, nodo)
    cameFrom = {}
    gCost = {node: float('inf') for node in graph}
    gCost[initial] = 0
    
    def heuristic(node,position):
        return ((position[node]))
    
    while openSet:
        current=heapq.heappop(openSet)[1]#menor costo del openSet
        
        if current ==goal:#hacer el camino
            path=[current]
            
            while current in cameFrom:
                current =cameFrom[current]
                path.append(current)
            
            return path[::-1]
        #Ver vecinos
        for neighbor, cost in graph[current].items():
            tentativeGCost=gCost[current]+cost
            if tentativeGCost<gCost[neighbor]:
                #actualizar costos
                cameFrom[neighbor]=current
                gCost[neighbor] = tentativeGCost
                fCost=tentativeGCost+heuristic(neighbor,position) #f(n)=g(n)+h(n)
                heapq.heappush(openSet,(fCost,neighbor))
    return None#Sin camino
                
                

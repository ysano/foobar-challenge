#!/usr/bin/env python
def solution(entrances, exits, path):
    # Your code here

    # add virtual start and end point
    for p in path:
        p.insert(0,0)
        p.append(0)
    new_length = len(path[0])
    path.insert(0, [0] * new_length)
    path.append([0] * new_length)
    for e in entrances:
        path[0][e+1] = float("INF")
    for e in exits:
        path[e+1][new_length-1] = float("INF")

    ROOM = len(path)
    source = 0
    sink = new_length-1

    def bfs(s,t,parent):
        visited = [False] * ROOM
        queue=[]
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(path[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False

    def edmonds_karp(source, sink):
        parent = [-1] * ROOM
        max_flow = 0            # overall flow
        while bfs(source, sink, parent):
            path_flow = float("INF")
            s = sink
            while s != source:
                path_flow = min(path_flow, path[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                path[u][v] -= path_flow
                path[v][u] += path_flow
                v = parent[v]
        return max_flow

    return edmonds_karp(source,sink)
                
if __name__ == "__main__":
    entrances = [0, 1]
    exits = [4, 5]
    path = [
        [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
        [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
        [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
        [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
        [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
        [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
    ]
    print solution(entrances,exits,path) # 16

    print solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]) # 6

    print solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) # 16

#!/usr/bin/env python
def solution(map):
    # Your code here
    """
    map: 0s:passable space, 1s:impassable walls
    (0,0): door out of the prison top left
    (w-1,h-1): into an escape pod bottom right
    height,widht: 2-20
    """
    import copy
    
    SPACE = 0
    WALL = 1
    FP = 2                      # footprint
    COMB = 3                    # short path

    MAX_PATH = 20 * 20
    ROWS = len(map)
    COLS = len(map[0])
    GOAL_I = ROWS-1
    GOAL_J = COLS-1
    
    # DEBUG = True
    DEBUG = False
    if DEBUG:
        print("RAWs,COLs",COLS,ROWS)
    
    def print_map(mp):
        for i in range(len(mp[0])+2):
            print("-"),
        print("")
        for row in mp:
            print("|"),
            for cell in row:
                if(cell==SPACE):
                    print(" "),
                elif(cell==COMB):
                    print("*"),
                elif(cell==WALL):
                    print("#"),
                elif(cell==FP):
                    print("&"),
                else:
                    print("error")
                    return
            print("|")
        for i in range(len(mp[0])+2):
            print("-"),
        print("")
    
    def start(i,j):
        return i == 0 and j == 0

    def goal(i,j):
        return i == GOAL_I and j == GOAL_J

    def wall_maria(i,j):
        res = bool(i < 0 or len(map)-1 < i or j < 0 or len(map[0])-1 < j)
        return res


    def find_path(map):
        if DEBUG:
            print_map(map)

        # start queue
        passable_queue = [[0,0]]
        # mark 0,0
        map[0][0] = FP
        # where come from
        from_map = [[-1 for i in range(COLS)] for i in range(ROWS)]

        while len(passable_queue) > 0:
            if DEBUG:
                print("passable_queue", passable_queue)
            i,j = passable_queue.pop(0)

            # find passable direction
            for m,n in [[-1,0],[1,0],[0,-1],[0,1]]:
                if not wall_maria(i+m,j+n) and map[i+m][j+n] == SPACE:
                    if goal(i,j):
                        break
                    # mark here
                    map[i+m][j+n] = FP
                    # queuing
                    passable_queue.append([i+m,j+n])
                    # where from by next pos
                    from_map[i+m][j+n] = [i,j]

        if from_map[ROWS-1][COLS-1] == -1: # cant goal
            return MAX_PATH

        if DEBUG:
            print("from_map", from_map)
            print("goal?", from_map[ROWS-1][COLS-1] != -1)

        # find shortest path from goal to start
        i=GOAL_I
        j=GOAL_J
        count=0
        while True:
            count+=1
            map[i][j] = COMB
            if start(i,j):
                break
            next_rev = from_map[i][j]
            i, j = next_rev
            
        if DEBUG:
            print("path",count)
            print_map(map)
        return count

    # find short path with wall erasing
    best = MAX_PATH

    # at first not erase
    tmp_map = copy.deepcopy(map)
    count = find_path(tmp_map)
    best = min(best,count)

    # search without one wall
    for i in range(ROWS):
        for j in range(COLS):
            if map[i][j] == WALL:
                tmp_map = copy.deepcopy(map)
                tmp_map[i][j] = SPACE
                count = find_path(tmp_map)
                best = min(best,count)
    if DEBUG:
        print("BEST:",best)
    return best
    
if __name__ == "__main__":

    # sol = print_map
    sol = solution
    
    # sol([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) # 7

    # sol([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) # 11

    # original
    # sol([[0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 0]]) # 8
    
    # sol([[0, 0, 0], [0, 1, 0], [1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 0, 0]]) # 8

    # sol([[0, 0], [0, 1], [0, 0], [0, 1], [0, 1], [0, 0]]) # 7

    # sol([[0, 0], [0, 0]]) # 3

    sol([[0, 1], [1, 0]]) # 3

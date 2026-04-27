class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        dic = [(0,1),(0,-1),(-1,0),(1,0)]
        visited = set()
        res = 0
        que = deque()

        def bfs(r,c):
            que.append([r,c])
            visited.add((r, c))

            while que:
                ro , co  = que.popleft()
                for i,j in dic:
                    row , col = ro+i , co+j
                    if (row in range(len(grid))) and (col in range(len(grid[0]))) and (grid[row][col] == "1") and ((row,col) not in visited):
                        que.append((row,col))
                        visited.add((row,col))
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    res += 1
                    bfs(r,c)
        return res
        

            

"""# 200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

```

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

```
"""

# Method 1 : DFS  Time: O(n^2) , Space 0 (1)
import numpy as np
class Solution(object):
    def numIslands(self, grid):
        islands = 0
        for i in range(len(grid)):  
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += self.dfs(i,j,grid)                                # search all the connected points until none
        return islands

    def dfs(self, i, j,grid):
        # depth first search 
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':            
            return 0        
        grid[i][j] = "0"                                                        # find all the points connect with the inital one and flipped to visted
        
        dirs = [ [0,1], [0,-1],[1,0],[-1,0]   ]        
        for dir in dirs:
            self.dfs(i+dir[0],j+dir[1],grid)
        return 1

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
a = Solution()
print ( a.numIslands(grid))
 
# Method 2 : BFS     Time: O(n^2) , Space 0 (n)
'''
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]

 q = [[0,0]] 
  ["0",*1","0","0","0"],   
  [*1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
  q=[[0,0],[0,1],[1,0]]
  ["0","0","0","0","0"],   
  ["0","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]

'''
class Solution(object):
    def numIslands(self, grid):
        islands = 0
        for i in range(len(grid)):  
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(i,j,grid)
                    islands+=1
                    print (grid)
        return islands

    def bfs(self, i, j,grid):
        # breast first search 
        dirs = [ [0,1], [0,-1],[1,0],[-1,0]   ]        
        q = [[i,j]]                                                              # storage the raw col ids for connected components
        grid[i][j] = "0"
        while len(q)>0  :       
            i,j = q.pop(0)                                                      # pop the first element of th remaining connected compoent coords
            for dir in dirs:
                ii,jj = i+dir[0],j+dir[1]                                        # next index ii,jj
                if ii < 0 or jj < 0 or ii >= len(grid) or jj >= len(grid[0]) or grid[ii][jj] == '0':   
                    pass
                else:                                                           grid[ii][jj] == '1' :
                    grid[ii][jj] = "0"                                          # visited in dex
                    q.append([ii,jj])                                           # add the connected coords index

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
a = Solution()
print ( a.numIslands(grid))

"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

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
"""
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        def add_hm(i,j):
            hm[str(i)+":"+str(j)] = 1
            if i < rows-1 and grid[i+1][j] == 1 and hm.get(str(i+1)+":"+str(j)) is None:
                add_hm(i+1, j)
            if j < column -1 and grid[i][j+1] == 1 and hm.get(str(i)+":"+str(j+1)) is None:
                add_hm(i, j+1)
            if i > 0 and grid[i-1][j] == 1 and hm.get(str(i-1)+":"+str(j)) is None:
                add_hm(i-1, j)
            if j > 0 and grid[i][j-1] == 1 and hm.get(str(i)+":"+str(j-1)) is None:
                add_hm(i, j-1)
        hm = {}
        rows = len(grid)
        column = len(grid[0])
        ret = 0
        for i,arr in enumerate(grid):
            for j,item in enumerate(arr):
                if item == 1 and hm.get(str(i)+":"+str(j)) is None:
                    add_hm(i,j)
                    ret += 1
        return ret
        
s = Solution()
print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))

# coding=utf-8
# coding=utf-8
'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1:
输入:
11110
11010
11000
00000
输出: 1
示例 2:

输入:
11000
11000
00100
00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
'''
from typing import List


class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        # data = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        if row == 0:
            return 0

        col = len(grid[0])
        lands_num = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    lands_num += 1
                    self.dfs(grid, i, j)
        return lands_num


if __name__ == '__main__':
    list_data = [["1", "1", "1", "1", "0"],
                 ["1", "1", "0", "1", "0"],
                 ["1", "1", "0", "0", "0"],
                 ["0", "0", "0", "0", "0"]]
    print(Solution().numIslands(list_data))

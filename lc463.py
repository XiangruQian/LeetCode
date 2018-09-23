class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        p = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if (i - 1 >= 0 and grid[i - 1][j] == 0) or (i == 0):
                        p += 1
                    if (i + 1 < n and grid[i + 1][j] == 0) or (i == n - 1):
                        p += 1
                    if (j - 1 >= 0 and grid[i][j - 1] == 0) or (j == 0):
                        p += 1
                    if (j + 1 < m and grid[i][j + 1] == 0) or (j == m - 1):
                        p += 1
        return p


a = Solution()
print(a.islandPerimeter([[1]]))
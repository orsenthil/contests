
# Reference: http://blog.csdn.net/thesnowboy_2/article/details/78173867

class Solution:

    def find(self, grid, row, col, visited):
        if grid[row][col] == 0 or visited[row][col] == 1:
            return 0

        result = 1

        visited[row][col] = 1

        if row + 1 < len(grid):
            result += self.find(grid, row + 1, col, visited)

        if row - 1 >= 0:
            result += self.find(grid, row - 1, col, visited)

        if col + 1 < len(grid[0]):
            result += self.find(grid, row, col + 1, visited)

        if col - 1 >= 0:
            result += self.find(grid, row, col - 1, visited)

        return result

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = []
        _max = 0

        for row in range(rows):
            _row = []
            for col in range(cols):
                _row.append(0)
            visited.append(_row)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue

                result = self.find(grid, row, col, visited)

                if _max < result:
                    _max = result

        return _max


if __name__ == '__main__':
    s = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(s.maxAreaOfIsland(grid))

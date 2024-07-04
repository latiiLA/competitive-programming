class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque()
        m, n = len(isWater), len(isWater[0])

        # find where water exists
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((0, i, j))

        # implement bfs on all elements
        ans = [[-1] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            val, x, y = queue.popleft() 
            if ans[x][y] != -1: continue
            ans[x][y] = val
            for dx, dy in directions:
                xx, yy = x+dx, y+dy
                if 0 <= xx < m and 0 <= yy < n and ans[xx][yy] == -1:
                    queue.append((val+1, xx, yy))
        return ans
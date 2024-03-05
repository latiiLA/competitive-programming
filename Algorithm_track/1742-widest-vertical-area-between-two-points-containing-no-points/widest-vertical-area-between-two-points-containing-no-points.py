class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        points.sort()

        maximumWidth = 0

        # find the maximum width difference of adjecent points
        for i in range(len(points) - 1):
            maximumWidth = max((points[i + 1][0] - points[i][0]), maximumWidth)

        return maximumWidth
        
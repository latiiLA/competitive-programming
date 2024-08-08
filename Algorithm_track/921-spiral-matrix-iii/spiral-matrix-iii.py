class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = [[rStart, cStart]]
        total = rows * cols
        steps = 0
        index = 0

        isValid = lambda x, y: 0 <= rStart < rows and 0 <= cStart < cols
        
        while len(result) < total:
            if index % 2 == 0:
                steps += 1
            
            for _ in range(steps):
                rStart += directions[index][0]
                cStart += directions[index][1]
                
                if isValid(rStart, cStart):
                    result.append([rStart, cStart])
                    if len(result) == total:
                        return result
            
            index = (index + 1) % 4
        
        return result
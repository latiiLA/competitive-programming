class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        # base case
        if rowIndex < 2:
            return [1] * (rowIndex + 1)

        # recursive call
        previous_row = self.getRow(rowIndex - 1)

        current_row = [1]
        for i in range(len(previous_row) - 1):
            current_row.append(previous_row[i] + previous_row[i + 1])
        current_row.append(1)

        return current_row
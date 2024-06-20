class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        Simon
        10:55 PM
        positve diagonal row + column is same for all numbers
        from(n,0) to (0,n)
        Simon
        10:56 PM
        negative diagonal row - column will be the same for all numbers
        '''

        # this to track the movement of the queuens for each qeuen
        column = set()
        positiveDiagonal = set()
        negativeDiagonal = set()

        result = []
        board = [["."] * n for _ in range(n)] # initialize empty board

        # define backtracking function
        # if row == n that is our base case
        # else check your set if it is valid row and column else continue to the next column
        def dfs(row):
            if row == n:
                res = ["".join(r) for r in board]
                result.append(res)
                return

            for col in range(n):
                if col in column or row + col in positiveDiagonal or row - col in negativeDiagonal:
                    continue
                
                column.add(col)
                negativeDiagonal.add(row - col)
                positiveDiagonal.add(row + col)
                board[row][col] = "Q"

                dfs(row + 1) 

                # remove previous moves to check with other combinations --> part of backtracking behaviors
                column.remove(col)
                negativeDiagonal.remove(row - col)
                positiveDiagonal.remove(row + col)
                board[row][col] = "."
        
        dfs(0)
        return result
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        length = len(board)

        def position(cell):
            r = (cell - 1) // length
            c = (cell - 1) % length
            if r%2 != 0: #if odd rows
                c = length-1-c
            return [r,c] 


        q = deque()
        q.append([1, 0])
        visited = set()

        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                cell = square + i

                r, c = position(cell)
                if board[r][c] != -1:
                    cell = board[r][c]
                if cell == length * length:
                    return moves + 1
                if cell not in visited:
                    visited.add(cell)
                    q.append([cell, moves + 1])

        return -1
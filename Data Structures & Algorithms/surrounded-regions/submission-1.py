class Solution:
    def solve(self, board):
        ROWS, COLS = len(board), len(board[0])   # board size

        def capture(r, c):                       # paint safe land as "T"
            if (r < 0 or c < 0 or r == ROWS or c == COLS or  # off board
                board[r][c] != "O"):             # not land (X or already T)
                return
            board[r][c] = "T"                    # mark safe
            capture(r + 1, c)                    # down
            capture(r - 1, c)                    # up
            capture(r, c + 1)                    # right
            capture(r, c - 1)                    # left

        # 1. paint everything connected to the edge as safe (O → T)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and
                    (r in [0, ROWS - 1] or c in [0, COLS - 1])):  # on the edge
                    capture(r, c)

        # 2. leftover O's are trapped (O → X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. restore the safe land (T → O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
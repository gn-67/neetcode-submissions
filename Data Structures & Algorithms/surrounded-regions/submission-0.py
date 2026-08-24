class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #maybe we check if a node is a 0 and on the border
        #if it is, then we mark all nodes accessible by it with a symbol "#", meaning we cannot capture it
        #then we finally iterate across the entire matrix, subbing out O for X and # for O

        rows = len(board)
        cols = len(board[0])


        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return 

            board[r][c] = "#"

            dfs(r,c - 1)
            dfs(r,c + 1)
            dfs(r - 1,c)
            dfs(r + 1,c)
            return 
        
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][cols - 1] == "O":
                dfs(r,cols - 1)
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
            




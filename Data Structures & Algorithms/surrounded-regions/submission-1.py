class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #ok so a region is surrounded if is NOT accessible by an O on the border
        #so we could run dfs from our border nodes, and mark all nodes on the path as a symbol, other than x or o, such as #, to denote that this node cannot be transformed into an x
        #then, once we have marked all unsurrounded nodes with an #, we can iterate across the entire board again one more time, and replace all # with os, and all os with xs


        rows = len(board)
        cols = len(board[0])
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            
            board[r][c] = "#"
            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)
            return 
        

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)
            
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c)
            
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)
        
        #now in theory, we should have marked all nodes that were Os to # if they are accessible by border Os, so we can go in and make necessary swaps

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

        
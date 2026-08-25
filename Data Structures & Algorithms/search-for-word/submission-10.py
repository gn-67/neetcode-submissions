class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #right away my mind is drawn to a BFS solution to traverse the board
        #and I think we will also have to incorporate backtracking here,

        visited = set()
        rows = len(board)
        cols = len(board[0])

        def bfs(r,c,i):
            #not entirely sure if we need to track anythign else within our function, if so I'll add it in retroactively

            if i >= len(word):
                return True


            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or board[r][c] != word[i]:
                return False

            visited.add((r,c))

            result = bfs(r + 1, c, i + 1) or bfs(r, c + 1, i + 1) or bfs(r - 1, c, i + 1) or bfs(r, c - 1, i + 1)
            visited.remove((r,c))
            return result
            
        
        for r in range(rows):
            for c in range(cols):
                if bfs(r,c,0):
                    return True
        
        return False

            

        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #we visit neightbors first -> BFS??
        
        row = len(board)
        column = len(board[0])
        path = set()


        def dfs(r, c, i):
            if i == len(word):
                return True #how does this verify we are done??? where are we even incrementing i?
            
            if r >= row or c >= column or r < 0 or c < 0:
                return False
            
            if (r,c) in path:
                return False

            if board[r][c] != word[i]:
                return False
            
            path.add((r,c))

            result = dfs(r + 1, c, i+1) or dfs(r - 1, c, i+1) or dfs(r, c + 1, i+1) or dfs(r, c - 1, i+1)

            #clean up our last addition
            path.remove((r,c))

            return result

        for r in range(row):
            for c in range(column):
                if dfs (r, c, 0):
                    return True
        
        return False


            
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        #we need to search every cell until we find our word
        #we can use a backtracking approach while checking all neighbors using DFS
        #we need to use a set to track out path, to make sure we don't visit nodes we'eve already visited

        rows = len(board)
        cols = len(board[0])
        seen = set()


        def dfs(r,c,i):
            #since we are traversing the board, we can start by laying out our basecases

            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in seen or board[r][c] != word[i]:
                return False
            if board[r][c] == word[i] and i == len(word) - 1:
                return True #we completed our word
            
            seen.add((r,c))

            result = dfs(r+1, c, i+1) or dfs(r, c+1, i+1) or dfs(r-1, c, i+1) or dfs(r, c-1, i+1)
            #if any of these come up true, result will be true
            seen.remove((r,c))
            return result

        
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        
        return False

        
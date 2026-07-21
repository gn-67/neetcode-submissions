class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        #we have to  check every cell
        # we can use dfs to check neighbors
        rows = len(board)
        columns = len(board[0])
        seen = set()
        # we can't visit the same cell twice

        def dfs (r, c, i):
            if i == len(word):
                return True
            
            if r >= rows or r < 0 or c >= columns or c < 0 or (r,c) in seen or board[r][c] != word[i]:
                return False

            seen.add((r,c))
            result = dfs(r+1, c, i + 1) or dfs(r-1, c, i + 1) or dfs(r, c+1, i + 1) or dfs(r, c-1, i + 1)
            seen.remove((r,c))
            return result

        

        for r in range(rows):
            for c in range(columns):
                if dfs(r,c,0):
                    return True
        
        return False

        
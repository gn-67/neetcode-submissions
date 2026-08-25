class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pac = set()
        atl = set()

        rows = len(heights)
        cols = len(heights[0])

        def dfs(r,c,ocean,prevHeight):
            if r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prevHeight or (r,c) in ocean:
                return
            
            ocean.add((r,c))

            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])
            return
        

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        return list(pac.intersection(atl))



        
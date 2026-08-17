class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        #we want to make sure each node is reachable by both pacific and atlantic ocean
        #we know that the edges for all of them are already accessible by respective ocean
        #we can reverse our thinking to be that water can flow from the ocean to a node if the node is greater than the node before it


        pac = set()
        atl = set()


        def dfs(r,c,ocean, prevHeight):
            if r < 0 or r >= rows or c < 0 or c >= cols or ((r,c)) in ocean or heights[r][c] < prevHeight:
                return 
            
            ocean.add((r,c))
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r - 1 ,c, ocean, heights[r][c])
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])


            
            


        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows-1][c])

        return list(pac.intersection(atl))
                

        
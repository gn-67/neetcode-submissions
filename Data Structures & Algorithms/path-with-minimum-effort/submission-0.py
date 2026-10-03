class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #minimum effort = minimum absoluter difference between two consectuive 

        minHeap = [[0,0,0]]
        directions = [[0,1],[1,0],[-1,0], [0,-1]]
        visited = set()

        while minHeap:
            diff, row, col = heapq.heappop(minHeap)

            if (row,col) in visited:
                continue
            visited.add((row,col))

            if row == len(heights) - 1 and col == len(heights[0]) - 1:
                return diff

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r >= 0 and c >= 0 and c < len(heights[0]) and r < len(heights) and (r,c) not in visited:
                    heapq.heappush(minHeap, [max(diff, abs(heights[row][col] - heights[r][c])),r,c,])
            
        
        
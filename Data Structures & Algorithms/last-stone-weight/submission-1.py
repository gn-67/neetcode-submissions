class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #we want to use a maxheap in order to keep track of the current heaviest stones
        #takes O(n) to make and O(logn) for each operation, which we do at most o(n) times so overall time complexity is O(nlogn)

        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)
            
        if not stones:
            return 0
        
        return abs(stones[0])
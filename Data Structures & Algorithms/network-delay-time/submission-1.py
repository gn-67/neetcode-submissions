class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        #first lets list out our edges into an adj map
        #we can also create an empty result set for O(1) lookup
        #from there, we can use a minheap to give us the nearest nodes as we traverse using BFS, and we will process them by checking if they already exist in our result, or adding them in if they aren't, since each insertion will always be the closest node thanks to the min heap


        adjMap = {i : [] for i in range(1, n + 1)}

        for node, destination, weight in times:
            adjMap[node].append([weight, destination])

        shortest = {}
        #the minimum time it takes to reach all nodes is simply the longest time from our source to the last node, so we can return that

        #our bfs heap contains the distance from source, and the node
        minHeap = [[0, k]]

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in shortest:
                continue
            
            shortest[node] = weight

            for weights, neighbors in adjMap[node]:
                if neighbors not in shortest:
                    heapq.heappush(minHeap, [weights + weight, neighbors])
        if len(shortest) != n:
            return -1
        return max(list(shortest.values()))

        
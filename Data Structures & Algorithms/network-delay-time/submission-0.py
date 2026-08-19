class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #first I will create an adjacency map with our edges and weights


        adjMap = {i : [] for i in range(n + 1)}
        for node, destination, weight in times:
            adjMap[node].append([destination, weight])
        
        
        #what I could do is grab the ordering in a hashmap then add up all the values
        minHeap = [[0,k]]
        result = {}

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in result:
                continue #we have already found the minimum time
            
            result[node] = weight

            for neighbors, weights in adjMap[node]:
                if neighbors not in result:
                    heapq.heappush(minHeap, [weights + weight, neighbors])
        
        if len(result) != n:
            return -1

        return max(result.values())
            
            

        
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        #first we want to start by making our adjacency list
        adjMap = {i : [] for i in range(n)}

        for source, destination, weight in edges:
            adjMap[source].append([destination, weight])
        

        result = {}
        minHeap = [[0,src]]
        #a minheap compares values in front first, so we should have weights first
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in result:
                continue #this is because our result contians the minimums
            result[node] = weight

            #now we explore our neighbors, adding the current weight to their weight
            for nodes, weights in adjMap[node]:
                heapq.heappush(minHeap,[weights + weight, nodes])
        
        for node in range(n):
            if node not in result:
                result[node] = -1
        
        return result
            





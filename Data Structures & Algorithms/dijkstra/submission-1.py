class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:


        #I think we can implement dykstras algorithm using a minheap + greedy bfs
        #implementing this algorithm allows us to find the shortest path on a weighted directed graph

        #and we can also use an adjMap to represent our nodes and edges

        adjMap = {i : [] for i in range(n)}

        for nodes, destinations, weights in edges:
            adjMap[nodes].append([destinations, weights])

        
        minHeap = [[0, src]]
        result = {}

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in result:
                #we've already captured the minimum distance, so we don't need to recalculate
                continue

            result[node] = weight
            
            for nodes, weights in adjMap[node]:
                heapq.heappush(minHeap, [weight + weights, nodes])

            
        
        #we can fill in empty nodes (unreachable) with -1
        for node in range(n):
            if node not in result:
                result[node] = -1
        
        return result



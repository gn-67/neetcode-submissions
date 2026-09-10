class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        #we want to track our tasks by count, and complete the highest frequency tasks frist, that way we can fill the stall cycles with the next most frequent task
        #we can easily access the most frequent tasks using a max heap
        #we can also utilize a queue in order to retrieve a task when it is ready to be processed again after waiting n cycles, and push it back onto our maxheap which we process from

        counts = collections.Counter(tasks)

        maxHeap = [-s for s in counts.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = collections.deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time

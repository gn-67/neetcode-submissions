#binary search, but maybe we return the upper bound of the tree and we just adjust it
# the lower bound of time would be 4, lower bound of rate would be 
# 25 + 10 + 23 + 4 = 62
# ceil(x/k)= h when pile x is eaten at k hours/banana

#find the max value in piles
# from range 1 - max
# do a binary search where k = the middle and we test k to see if it works
# we have to see if the time it takes to complete the list is less than or equal to 9

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        result = 1

        while start <= end:
            time = 0
            k = start + (end - start) // 2
            
            for i in range(len(piles)):
                time += math.ceil( piles[i] / k)

            if time > h:
                start = k + 1

            elif time <= h:
                end = k - 1
                result = k
        
        return result
            


        



        
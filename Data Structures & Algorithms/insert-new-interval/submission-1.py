class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #our intervals are given in sorted order
        #which means we can iterate across
        #if the end time of our new interval is before the start time of our current interval
        #we know we have to insert here, and the rest of our intervals remain the same
        #if the start time of our interval is after the current interval ends, then we have to add our current interval to the result and move on
        #otherwise, this means our newInterval is overlapping with another interval
        #so we update our new interval to be the min start of hte two intervals and the max end of the two intervals
        #and at the end if we never inserted our newInterval, we place it at the end

        result = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]

            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
        
        result.append(newInterval)

        return result
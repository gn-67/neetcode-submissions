"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #we can use sort of a two pointer approach here,
        #where we sort by start times in one list
        #and end times in another list
        #then we greedily compare while we have start times available
            #if any start time is before an end time, we increment our count variable
            #if any start time is after an end time, we decrement our count variable
            #we take the max after each iteration
        

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        result = 0
        count = 0
        i = 0
        j = 0

        while i < len(start):
            if start[i] < end[j]:
                count += 1
                i += 1
            
            else:
                count -= 1
                j += 1
            
            result = max(result, count)
        
        return result

        
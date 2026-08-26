"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        #we need our sorted start and end times
        #whenever theres a conflict, we increment our count by one
        #once there isn't a conflict, we decrement
        #we return the highest value count was at

        result = 0
        count = 0


        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])



        i = 0
        j = 0

        while i < len(starts):
            if ends[j] > starts[i]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            
            result = max(result,count)

        return result
        
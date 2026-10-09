"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #first we sort by start times
        #then we check if the start time of our second interval is before the end of the time before:
        #return false, otherwise return true at the end


        if len(intervals) <= 1:
            return True

        intervals = sorted(intervals, key = lambda x : x.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        
        return True


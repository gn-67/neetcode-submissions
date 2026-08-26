"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        sortTimes = sorted(intervals, key = lambda x : x.start) #sort based on start times

        for i in range(1,len(intervals)):
            if sortTimes[i-1].end > sortTimes[i].start:
                return False
        
        return True

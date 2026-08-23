"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        count = 0
        result = 0

        i = 0
        j = 0

        while i < len(intervals):
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                j += 1
                count -= 1
            result = max(result, count)
        
        return result
        
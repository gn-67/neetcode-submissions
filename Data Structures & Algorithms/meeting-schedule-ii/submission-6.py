"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        starts = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals])
        rooms = 0
        result = 0
        i = 0
        j = 0
        #we increment when rooms overlap
        #decrement when rooms don't
        while i < len(intervals):
            if starts[i] < end[j]:
                rooms += 1
                i += 1
            else:
                rooms -= 1
                j += 1
            result = max(rooms, result)
        
        return result

        
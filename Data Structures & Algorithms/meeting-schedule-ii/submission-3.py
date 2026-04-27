"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ans = 0
        count = 0

        start = intervals.copy()
        end = intervals.copy()

        start.sort(key=lambda i: i.start)
        end.sort(key=lambda i: i.end)

        s = e = 0
    
        while s < len(start):
            if start[s].start < end[e].end:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            ans = max(ans, count)

        
        return ans
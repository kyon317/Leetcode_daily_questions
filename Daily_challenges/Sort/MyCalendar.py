'''
Leetcode 729 My Calendar I
https://leetcode.com/problems/my-calendar-i/description/
Finish date: 2024-09-25
Algorithm: Sorted dictionary
'''

from sortedcontainers import SortedDict


class MyCalendar:

    def __init__(self):
        self.timeslot = SortedDict()

    def book(self, start: int, end: int) -> bool:
        first_idx = self.timeslot.bisect_right(start) - 1
        nxt_idx = self.timeslot.bisect_left(start)
        if first_idx >= 0 and self.timeslot.values()[first_idx] > start:
            # 上个日程还没结束，本次日程就开始了
            return False

        if nxt_idx < len(self.timeslot) and self.timeslot.keys()[nxt_idx] < end:
            # 本次日程还没结束，下个日程就开始了
            return False
        self.timeslot[start] = end
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
'''
Leetcode 731. My Calendar II
https://leetcode.com/problems/my-calendar-ii/description/
Finish date: 2024-09-26
Algorithm: Array, sorting, segment tree
'''


class MyCalendarTwo:

    def __init__(self):
        self.t1 = []  # non-overlapping books
        self.t2 = []  # overlapping books

    def book(self, start: int, end: int) -> bool:
        for s, e in self.t2:
            # overlap second time
            if s < end and e > start:
                return False
        for s, e in self.t1:
            # overlap first time
            if s < end and e > start:
                self.t2.append((max(s, start), min(e, end)))
        self.t1.append((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

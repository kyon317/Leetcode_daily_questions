'''
Leetcode 1381. Design a Stack With Increment Operation
https://leetcode.com/problems/design-a-stack-with-increment-operation/description/
Finish date: 2024-09-29
Algorithm: Array, Datastructure
'''

class CustomStack:

    def __init__(self, maxSize: int):
        self._size = maxSize
        self._stk = []

    def push(self, x: int) -> None:
        if len(self._stk) < self._size:
            self._stk.append(x)

    def pop(self) -> int:
        if self._stk == []:
            return -1
        return self._stk.pop()

    def increment(self, k: int, val: int) -> None:
        if k > len(self._stk):
            k = len(self._stk)
        for i in range(k):
            self._stk[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
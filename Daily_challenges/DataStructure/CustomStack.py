'''
Leetcode 1381. Design a Stack With Increment Operation
https://leetcode.com/problems/design-a-stack-with-increment-operation/description/
Finish date: 2024-09-29
Algorithm: Array, Datastructure
'''

class CustomStack:

    def __init__(self, maxSize: int):
        self._size = maxSize
        self._stk = [-1] * maxSize
        self._front = -1

    def push(self, x: int) -> None:
        if self._front == self._size - 1:
            return
        self._front += 1
        self._stk[self._front] = x

    def pop(self) -> int:
        if self._front == -1:
            return -1
        res = self._stk[self._front]
        self._stk[self._front] = -1
        self._front -= 1
        return res

    def increment(self, k: int, val: int) -> None:
        if k > self._front + 1:
            k = self._front + 1
        for i in range(k):
            self._stk[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
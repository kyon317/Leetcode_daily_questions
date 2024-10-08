'''
Leetcode 641. Design Circular Deque
https://leetcode.com/problems/design-circular-deque/description/
Finish date: 2024-09-27
Algorithm: Datastructure, double pointers
'''

class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [-1] * k
        self.k = k
        self._front, self._rear = 0,0
        self._size = 0


    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.isEmpty():
            self._front = (self._front - 1) % self.k
        self.q[self._front] = value
        self._size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.isEmpty():
            self._rear = (self._rear + 1) % self.k
        self.q[self._rear] = value
        self._size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self._front] = -1
        self._front = (self._front + 1) % self.k
        self._size -= 1
        if self.isEmpty():
            self._rear = self._front
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self._rear] = -1
        self._rear = (self._rear - 1) % self.k
        self._size -= 1
        if self.isEmpty():
            self._front = self._rear
        return True

    def getFront(self) -> int:
        return self.q[self._front]

    def getRear(self) -> int:
        return self.q[self._rear]

    def isEmpty(self) -> bool:
        return self._size == 0

    def isFull(self) -> bool:
        return self._size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
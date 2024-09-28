class DoubleLinkedListNode:                                    #Double linked list node class.
    def __init__(self, value: int):
        self.prev = None
        self.next = None
        self.value = value

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k                                          #Initialize sive, count, head and tail.
        self.count = 0
        self.head = DoubleLinkedListNode(-1)
        self.tail = DoubleLinkedListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        if self.isFull():                                      #Insert after head if not full.
            return False
        self.count += 1
        node = DoubleLinkedListNode(value)
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():                                      #Insert before tail if not full.
            return False
        self.count += 1
        node = DoubleLinkedListNode(value)
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():                                     #Delete after head if not empty.
            return False
        self.count -= 1
        node = self.head.next
        node.next.prev = self.head
        self.head.next = node.next
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():                                     #Delete before tail if not empty.
            return False
        self.count -= 1
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        return True

    def getFront(self) -> int:
        if self.isEmpty():                                     #Return value after head if not empty; otherwise -1.
            return -1
        return self.head.next.value

    def getRear(self) -> int:
        if self.isEmpty():                                     #Return value before tail if not empty; otherwise -1.
            return -1
        return self.tail.prev.value

    def isEmpty(self) -> bool:
        return self.count == 0                                 #Return if count is 0.

    def isFull(self) -> bool:
        return self.count == self.size                         #Return if count is size limit.


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

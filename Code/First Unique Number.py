class DoubleLinkedListNode:                           #Double linked list node.
    def __init__(self, x):
        self.value = x
        self.prev = None
        self.next = None
        
class FirstUnique:

    def __init__(self, nums: List[int]):              #Use a double linked list to store all unique numbers.
        self.map = {}                                 #Use a dict to store the location of unique number in double linked list.
        self.head = DoubleLinkedListNode(-1)          #Double linked list head, value -1.
        self.tail = DoubleLinkedListNode(-1)          #Double linked list tail, value -1.
        self.head.next = self.tail
        self.tail.prev = self.head
        for x in nums:                                #Initially, add all elements in order.
            self.add(x)

    def showFirstUnique(self) -> int:
        return self.head.next.value                   #Always return the value of next node of head.

    def add(self, value: int) -> None:
        if value not in self.map:                     #If value is a new number, append it to before the double linked lisk tail and add the location to dict.
            node = DoubleLinkedListNode(value)
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node
            self.map[value] = node
        elif self.map[value] is not None:             #If value is not new but only appears once, remove the previous appearance from double linked list and set the location of it to none.
            node = self.map[value]
            node.next.prev = node.prev
            node.prev.next = node.next
            node.prev = None
            node.next = None
            self.map[value] = None

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

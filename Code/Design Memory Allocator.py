class DoubleLinkedListNode:                                                                                                                                                   #Double linked list node class.
    def __init__(self, start: int, end: int, allocated: bool, prev: 'ListNode', next: 'ListNode'):
        self.start = start
        self.end = end
        self.allocated = allocated
        self.prev = prev
        self.next = next

class Allocator:

    def __init__(self, n: int):
        self.doubleLinkedListHead, self.doubleLinkedListTail = DoubleLinkedListNode(-1, -1, True, None, None), DoubleLinkedListNode(-1, -1, True, None, None)                 #Instantiate dummy head and dummy tail for double linked list.
        node = DoubleLinkedListNode(0, n - 1, False, self.doubleLinkedListHead, self.doubleLinkedListTail)                                                                    #Insert a node between head and tail representing the unallocated memory block, from 0 to n - 1.
        self.doubleLinkedListHead.next = node
        self.doubleLinkedListTail.prev = node
        self.allocated = defaultdict(list)                                                                                                                                    #Store the allocated memory block nodes by mID.

    def allocate(self, size: int, mID: int) -> int:
        curr = self.doubleLinkedListHead.next
        while curr != self.doubleLinkedListTail:                                                                                                                              #Traverse double linked list.
            if not curr.allocated and curr.end - curr.start + 1 >= size:                                                                                                      #If current memory block is not allocated and have enough memory to allocate, allocate memory.
                curr.allocated = True                                                                                                                                         #Mark current memory block as allocated.
                self.allocated[mID].append(curr)                                                                                                                              #Add it to allocated of mID.
                if curr.end - curr.start + 1 > size:                                                                                                                          #If there are memory remain after allocation, instantiate a new node for it and insert it after current block.
                    newNode = DoubleLinkedListNode(curr.start + size, curr.end, False, curr, curr.next)
                    curr.next.prev, curr.next = newNode, newNode
                    curr.end = curr.start + size - 1                                                                                                                          #Update the end of current block.
                return curr.start                                                                                                                                             #Return start of current block.
            curr = curr.next
        return -1

    def free(self, mID: int) -> int:
        count = 0                                                                                                                                                             #Initialize count.
        for node in self.allocated[mID]:                                                                                                                                      #Travrese nodes of all allocated memory block for current mID.
            count += node.end - node.start + 1                                                                                                                                #Add the block size to count.
            if not node.prev.allocated:                                                                                                                                       #If node.prev is not allocated, merge it with node.
                node.start, node.prev = node.prev.start, node.prev.prev
                node.prev.next = node
            if not node.next.allocated:                                                                                                                                       #If node.next is not allocated, merge it with node.
                node.end, node.next = node.next.end, node.next.next
                node.next.prev = node
            node.allocated = False                                                                                                                                            #Set node to be not allocated.
        self.allocated[mID].clear()                                                                                                                                           #Clear all allocation for mID.
        return count                                                                                                                                                          #Return count.

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)

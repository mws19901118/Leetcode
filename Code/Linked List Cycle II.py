# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head                                                 #Initialize fast & slow pointers.
        count = 0                                                               #Count the length from head to where fast catches slow.
        while fast and fast.next:                                               #Move forward fast and slow in different pace.
            fast = fast.next.next
            slow = slow.next
            count += 1
            if fast == slow:                                                    #If fast catches slow, stop.
                break
        if slow != fast or not count:                                           #If fast does not catch slow or they didn't move at all, there is no cycle.
            return None
        length = 0                                                              #Count the length of cycle.
        while True:
            fast = fast.next
            length += 1
            if fast == slow:
                break
        if count >= length:                                                     #Imagine the loop is cut at the meet point. The linked list then becomes Y shape. One start is head, the other is the next of catching point and end at catching point.
            for i in range(count - length):                                     #Next, it becomes how to find the intersection of Y shape linked list with the lengths of 2 linked list are known.
                head = head.next
        else:
            for i in range(length - count):
                fast = fast.next
        while fast != head:
            fast = fast.next
            head = head.next
        return head

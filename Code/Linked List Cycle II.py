# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:                                                            #If head is none, return none.
            return head
        fast, slow = head, head
        hasCycle = False
        count = 0
        while fast.next is not None and fast.next.next is not None:             #Use fast and slow pointers to determine if there is cycle. Also count the steps from head to where fast and slow pointers meet.
            fast = fast.next.next
            slow = slow.next
            count += 1
            if fast == slow:
                hasCycle = True
                break
        if not hasCycle:                                                        #If no cycle, return none.
            return None
        length = 0                                                              #Count the length of cycle.
        while True:
            fast = fast.next
            length += 1
            if fast == slow:
                break
        if count >= length:                                                     #Imagine the loop is cut at the meet point. The linked list then becomes Y shape. One start is head, the other is the next of meeting point and end at meeting point.
            for i in range(count - length):                                     #Next, it becomes how to find the intersection of Y shape linked list with the lengths of 2 linked list are known.
                head = head.next
        else:
            for i in range(length - count):
                fast = fast.next
        while fast != head:
            fast = fast.next
            head = head.next
        return head

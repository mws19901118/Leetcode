# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0, head)                                           #Because head may be deleted, add a dummy head before the head node.
        tail = dummyHead
        while tail.next:                                                        #Traverse list until the next of tail is none.
            count = 0                                                           #Count current value.
            curr = tail.next
            while curr and curr.val == tail.next.val:
                count += 1
                curr = curr.next
            if count > 1:                                                       #If current value has multiple appereances, delete them.
                tail.next = curr
            else:                                                               #Otherwise, move tail to next node.
                tail = tail.next
        return dummyHead.next                                                   #Return the next of dummy head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(-5001, head)                               #Create a dummy head.
        tail = dummyHead.next                                           #Initialize tail to be the actual head.
        while tail.next:                                                #Traverse list while tail.next is not none.
            if tail.next.val > tail.val:                                #If the tail.next.val is greater than tail.val, traversed list is sorted so far; so move tail to next and continue. 
                tail = tail.next
                continue
            curr = dummyHead                                            #Find the place to insert tail.next in the traversed list.
            while curr != tail and curr.next.val < tail.next.val:
                curr = curr.next
            temp = tail.next                                            #Detach tail.next from tail and insert it after curr.
            tail.next = temp.next
            temp.next = curr.next
            curr.next = temp
        return dummyHead.next                                           #Return dummyHead.next.

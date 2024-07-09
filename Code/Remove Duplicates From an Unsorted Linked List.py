# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        count = Counter()                          #Instantiate a counter.
        curr = head
        while curr:                                #Count the values in list.
            count[curr.val] += 1
            curr = curr.next
        dummyHead = ListNode()                     #Create a dummy head and a tail.
        tail = dummyHead
        curr = head
        while curr:                                #Traverse original list.
            if count[curr.val] == 1:               #If its value has no duplicate, append a such node to tail and move forward tail.
                tail.next = ListNode(curr.val)
                tail = tail.next
            curr = curr.next
        return dummyHead.next                      #Return the next of dummy head.

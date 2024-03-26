# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = Counter()                  #Count each element in linked list.
        curr = head
        while curr:
            count[curr.val] += 1
            curr = curr.next
        dummyHead = ListNode()             #Create a dummy head.
        tail = dummyHead
        for k, v in count.items():         #Append the frequency to the tail of new list.
            tail.next = ListNode(v)
            tail = tail.next
        return dummyHead.next              #Return the next of dummy head.

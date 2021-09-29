# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0                                         #Count length.
        curr = head
        while curr:
            count += 1
            curr = curr.next
        quotient, remainder = divmod(count, k)            #Get the quotient and remainder of count / k.
        parts = []
        for i in range(k):                                #Traverse k.
            length = quotient + int(i < remainder)
            if length == 0:
                parts.append(None)
                continue
            curr = head
            for _ in range(length - 1):
                curr = curr.next
            parts.append(head)
            head = curr.next
            curr.next = None
        return parts

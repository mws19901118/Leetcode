# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0                                           #Count length.
        curr = head
        while curr:
            count += 1
            curr = curr.next
        quotient, remainder = divmod(count, k)              #Get the quotient and remainder of count / k.
        parts = []
        for i in range(k):                                  #Traverse k.
            length = quotient + int(i < remainder)          #Calculate length of current part. If i < remainder, it's quotient + 1; otherwise, it's quotient.
            if length == 0:                                 #If length is 0, append none to parts and continue.
                parts.append(None)
                continue
            curr = head                                     #Set curr to head.
            for _ in range(length - 1):                     #Move curr to curr.next for length - 1 times.
                curr = curr.next
            parts.append(head)                              #Append head to parts.
            head = curr.next                                #Set head to curr.next.
            curr.next = None                                #Unlink curr.next with curr.
        return parts

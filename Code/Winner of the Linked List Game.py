# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        diff = 0                                                              #Store the diff between Odd team vs Even team.
        while head:                                                           #Traverse while head is not none.
            diff += 1 if head.val > head.next.val else -1                     #Increase diff old-index node is higher in current pair; decrease otherwise.
            head = head.next.next                                             #Move head twice to next pair.
        return "Tie" if not diff else ("Odd" if diff < 0 else "Even")         #Return result based on the value of diff.

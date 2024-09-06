# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)                        #Store nums in a set.
        dummyHead = ListNode(-1, head)       #Create a dummy head.
        curr = dummyHead
        while curr.next:                     #Traverse the linked list.
            if curr.next.val not in s:       #If the value of next of curr is not in s, move curr forward.
                curr = curr.next
                continue
            t = curr.next.next               #Otherwise, delete the next of curr.
            curr.next.next = None
            curr.next = t
        return dummyHead.next                #Return the next of dummy head.

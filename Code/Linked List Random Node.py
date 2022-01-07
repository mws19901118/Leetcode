# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head                                #Store linked list.
        self.length = 0                                 #Count length.
        curr = head
        while curr:
            self.length += 1
            curr = curr.next

    def getRandom(self) -> int:
        n, curr = self.length, self.head                #Sampling without replacement.
        while curr:
            if random.random() < 1 / n:
                return curr.val
            curr = curr.next
            n -= 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

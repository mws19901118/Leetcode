# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head                                                    #Initialize head node.
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        n, result = 1, 0                                                  #n stands for how many nodes have been traversed.
        curr = self.head

        while curr:                                                       #Traverse the linked list.
            if random.random() < 1 / n:                                   #Decide whether to include the element in reservoir
                result = curr.val
            curr = curr.next                                              #Move on to the next node
            n += 1
        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

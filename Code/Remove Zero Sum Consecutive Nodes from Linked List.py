# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefixSum = 0                                                #Initialize prefix sum.
        prefixSumSet = set([0])                                      #Initialize the seen prefix sums.
        stack = []                                                   #Use stack to store all remain values.
        curr = head
        while curr:                                                  #Traverse linked list.
            prefixSum += curr.val                                    #Update prefix sum.
            if prefixSum in prefixSumSet:                            #If current prefix sum is seen, we have to remove all values since first seen current prefix sum.
                prefixSumToBeDeleted = prefixSum - curr.val          #Initialize prefixSumToBeDeleted with prefixSum - curr.val, as current node is already deleted.
                while stack and prefixSumToBeDeleted != prefixSum:   #Iterate while stack is not empty and the prefixSumToBeDeleted is not current prefix sum, i.e. we haven't finished deleting all values since first seen current prefix sum.
                    prefixSumSet.remove(prefixSumToBeDeleted)        #Delete prefixSumToBeDeleted from prefixSumSet.
                    prefixSumToBeDeleted -= stack.pop()              #Pop stack and distract the value from prefixSumToBeDeleted.
            else:                                                    #If current prefix sum is not seen, add current value to stack and add current prefix sum to prefixSumSet.
                stack.append(curr.val)
                prefixSumSet.add(prefixSum)
            curr = curr.next
        dummyHead = ListNode()                                       #Create a dummy head for a new linked list.
        tail = dummyHead
        for x in stack:                                              #Traverse stack in FIFO fashion and create a list node for each value and append it to the tail of new linked list.
            tail.next = ListNode(x, None)
            tail = tail.next
        return dummyHead.next                                        #Return the next of dummyHead.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = [inf, -1]                                                                                                                                        #Initialize result.
        curr, index = head, 0                                                                                                                                     #Initialize pointer to traverse the linked list and the index of pointer in linked list.
        firstCritical, prevCritical = -1, -1                                                                                                                      #Store the index of first critical and previous critical.                                       
        while curr.next and curr.next.next:                                                                                                                       #Traverse while curr has next and next of next.
            if (curr.next.val < curr.val and curr.next.val < curr.next.next.val) or (curr.next.val > curr.val and curr.next.val > curr.next.next.val):            #Process if curr.next is a critical.
                if firstCritical == -1:                                                                                                                           #If it is the first critical, update the index of first critical.
                    firstCritical = index + 1
                else:                                                                                                                                             #Otherwise, update result.
                    result[0] = min(result[0], index + 1 - prevCritical)                                                                                          #Min distance could be the distance from previous critical to current critical.
                    result[1] = index + 1 - firstCritical                                                                                                         #Max distance is from first critical to current critical.
                prevCritical = index + 1
            index += 1                                                                                                                                            #Increase index,
            curr = curr.next                                                                                                                                      #Move curr to next.
        return result if result[0] != inf else [-1, -1]                                                                                                           #Return [-1, -1] if min distance is inf; otherwise, return result.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummyHead = ListNode()                      #Create a dummy head.
        tail = dummyHead                            #Store the tail pointer of new linked list.
        while head:                                 #Traverse linked list.
            count, curr = 0, head                   #Initialize count and curr for the traverse of next group.
            while count < k and curr:               #Traverse next group and count nodes.
                count += 1
                curr = curr.next
            if count < k:                           #If count < k, we reach the last group, so no need to revrese.
                tail.next = head                    #Directly point the next of tail to head and move head to curr, which is none.
                head = curr
            else:                                   #Otherwise, we have to reverse current group.
                for _ in range(k):                  #Traverse nodes in current group.
                    temp = head                     #Point a temp pointer to current node.
                    head = head.next                #Move head to next.
                    temp.next = tail.next           #Insert temp to the next of tail.
                    tail.next = temp
                for _ in range(k):                  #Move tail to the actual tail after insert the reversed group.
                    tail = tail.next
        return dummyHead.next                       #Return the next of dummy head.

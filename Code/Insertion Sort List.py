# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head==None:
            return head
        result=ListNode(head.val)
        tail=result                           #result is the head of new list
        current=head.next
        while current!=None:
            temp1=ListNode(current.val)
            if temp1.val<=result.val:         #current value is smaller than or equal to head value, temp1 becomes the new head.
                temp1.next=result
                result=temp1
            else:
                if tail.val<temp1.val:        #current value is larger than tail value, temp1 becomes the new tail.
                    tail.next=temp1
                    temp1.next=None
                    tail=temp1
                else:                 
                    temp2=result
                    while temp2.next!=None:   #find the correct place of current value
                        temp3=temp2.next
                        if temp3.val<temp1.val:
                            temp2=temp3
                        else:                 #insert
                            temp2.next=temp1
                            temp1.next=temp3
                            break
            current=current.next
        return result

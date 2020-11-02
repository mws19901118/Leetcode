# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        result = ListNode(head.val)
        tail = result                                                   #Result is the head of new list
        head = head.next
        while head:
            node = ListNode(head.val)
            if node.val <= result.val:                                  #If current value is smaller than or equal to result value, node becomes the new head.
                node.next = result
                result = node
            elif tail.val < node.val:                                   #If current value is larger than tail value, node becomes the new tail.
                tail.next = node
                node.next = None
                tail = node
            else:
                curr = result
                while curr.next and curr.next.val < node.val:           #Find the correct place of current value
                    curr = curr.next
                node.next = curr.next                                   #Insert.
                curr.next = node
            head = head.next
        return result

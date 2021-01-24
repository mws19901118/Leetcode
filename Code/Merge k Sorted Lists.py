# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2Lists(self, l1: ListNode, l2: ListNode) -> ListNode:                                              #Merge 2 sorted lists.
        dummyHead = ListNode()
        tail = dummyHead
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummyHead.next
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2                                                                                  #Divide and conquer.
        list1, list2 = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge2Lists(list1, list2)

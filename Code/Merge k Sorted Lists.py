# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):                               #Use divide and conquer
        l=len(lists)
        if l==0:                                                #If there is no linked lists, return none.
            return None
        elif l==1:                                              #If there are only one linked list, return itself.
            return lists[0]
        elif l==2:                                              #If there are exactly 2 linked lists, merge them.
            newlist=ListNode(-1)
            tail=newlist
            l1=lists[0]
            l2=lists[1]
            while l1!=None and l2!=None:
                if l1.val<l2.val:
                    tail.next=l1
                    tail=tail.next
                    l1=l1.next
                else:
                    tail.next=l2
                    tail=tail.next
                    l2=l2.next
            if l1==None:
                tail.next=l2
            else:
                tail.next=l1
            newlist=newlist.next
            return newlist
        else:                                                   #If there are more than 2 link lists, equally divide them into half, merge the two halves respectively, and then merge the results.
            newlists=[]
            newlists.append(self.mergeKLists(lists[:l/2]))
            newlists.append(self.mergeKLists(lists[l/2:]))
            return self.mergeKLists(newlists)

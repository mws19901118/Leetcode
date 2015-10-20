# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head==None:
            return None
        p=head
        while p!=None:                                      #duplicate every node and insert them after the old ones
            t=RandomListNode(p.label)
            t.next=p.next
            p.next=t
            t.random=p.random
            p=t.next
        p=head.next
        while True:                                         #process 'random' pointer
            if p.random!=None:
                p.random=p.random.next
            if p!=None and p.next!=None:
                p=p.next.next
            else:
                break
        newhead=head.next
        q=head
        p=newhead
        while q.next!=None and q.next.next!=None and p.next!=None and p.next.next!=None:              #delete old ones
            q.next=q.next.next
            q=q.next
            p.next=p.next.next
            p=p.next
        #if p!=None:
        p.next=None
        #if q!=None:
        q.next=None
        return newhead

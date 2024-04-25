class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:                                                                             #If head is none, creat a new single circular linked list and return.
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode
 
        prev, curr = head, head.next                                                             #Initialize prev and curr to be head and head.next.
        while True:                                                                              #Traverse the circular linked list.
            if prev.val <= insertVal <= curr.val or \                                            #Scenario 1: insertVal is between prev.val and curr.val, then just insert it after prev.
            (prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val)):          #Scenario 2: prev.val > curr.val, which means prev.val is the largest and curr.val is the smallest. If insertVal is not smaller to prev.val or not larger than curr.val, insertVal should also be inserted after prev.
                prev.next = Node(insertVal, curr)
                return head                                                                      #Directly return after insertion.
            prev, curr = prev.next, curr.next
            if prev == head:                                                                     #If prev == head, we have traversed the whole circular linked list and not insert the insertVal yet, so break. And it means all nodes have same value.
                break
        prev.next = Node(insertVal, curr)                                                        #Then we can insert the insertVal at any place, could be just after prev.
        return head                                                                              #Return head.

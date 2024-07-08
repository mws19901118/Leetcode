class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:                                                                                       #If head is none, creat a new single circular linked list and return.
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode
 
        curr = head                                                                                        #Initialize and curr to be head.
        while True:                                                                                        #Traverse the circular linked list.
            if curr.val <= insertVal <= curr.next.val or \                                                 #Scenario 1: insertVal is between curr.val and curr.next.val, then just insert it after curr.
            (curr.val > curr.next.val and (insertVal >= curr.val or insertVal <= curr.next.val)):          #Scenario 2: curr.val > curr.next.val, which means curr.val is the largest and curr.next.val is the smallest. If insertVal is not smaller to curr.val or not larger than curr.next.val, insertVal should also be inserted after curr.
                curr.next = Node(insertVal, curr.next)
                return head                                                                                #Directly return after insertion.
            curr = curr.next
            if curr == head:                                                                               #If curr == head, we have traversed the whole circular linked list and not insert the insertVal yet, so break. And it means all nodes have same value.
                break
        curr.next = Node(insertVal, curr.next)                                                             #Then we can insert the insertVal at any place, could be just after curr.
        return head                                                                                        #Return head.

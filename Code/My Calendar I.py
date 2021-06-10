class Node:                                             #Binary search tree node for interval.
    def __init__(self, start, end):
        self.start, self.end = start, end               #Initialize node with interval start and end.
        self.left, self.right = None, None              #Initially, left child and right child is none.

    def insert(self, node) -> bool:                     #Insert node to binary search tree.
        if node.start >= self.end:                      #If node's start is not smaller than current end, set node to be the right child of current node and return true if right child is none.
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)              #If right child is not none, insert it to right subtree recursively.
        elif node.end <= self.start:                    #If node's end is not smaller than current start, set node to be the left child of current node and return true if left child is none.
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)               #If left child is not none, insert it to left subtree recursively.
        else:                                           #Else, there is overlap, so return false.
            return False

class MyCalendar:

    def __init__(self):
        self.root = Node(-1, -1)                        #Initialize binary search tree with a dummyhead.

    def book(self, start: int, end: int) -> bool:
        return self.root.insert(Node(start, end))       #Return the result of insert new interval node.


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(",")                       #Split preorder string by ",".
        stack = []                                        #Use stack to store node.
        for i, x in enumerate(nodes):                     #Traverse nodes.
            if x != '#':                                  #If x is number, append false to stack, meaning that hasn't visited the right child of current node.
                stack.append(False)
            else:                                         #Otherwise, while stack top is true, pop stack.
                while stack and stack[-1]:
                    stack.pop()
                if not stack:                             #If stack is empty, x must be the last element in nodes to make it a valid preorder serialization of binary tree.
                    return i == len(nodes) - 1
                stack[-1] = True                          #Set top of stack to true, meaning that has visited the right child of current node.
        return not stack                                  #Return if the stack is empty.

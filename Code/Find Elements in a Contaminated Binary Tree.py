# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.elements = set()                                  #Store elements in a set.
        root.val = 0                                           #Set root.val to 0.
        dq = deque([root])                                     #Initialize dq with root.
        while dq:                                              #BFS.
            node = dq.popleft()
            self.elements.add(node.val)                        #Add node.val to self.elements.
            if node.left:
                node.left.val = 2 * node.val + 1               #Update node.left.val if node.left is valid.
                dq.append(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2              #Update node.right.val if node.right is valid.
                dq.append(node.right)

    def find(self, target: int) -> bool:
        return target in self.elements                         #Return if target is in self.elements.


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder_index = {x: i for i, x in enumerate(postorder)}                                                            #Store the index of each node in postorder.
        def construct(preorder_start: int, preorder_end: int, postorder_start: int, postorder_end) -> Optional[TreeNode]:    #Construct binary tree with preorder[preorder_start:preorder_end + 1] and postorder[postorder_start:postorder_end + 1].
            if preorder_start > preorder_end or postorder_start > postorder_end:                                             #If either preorder[preorder_start:preorder_end + 1] or postorder[postorder_start:postorder_end + 1] is invalid, return none.
                return None
            node = TreeNode(preorder[preorder_start])                                                                        #Create a node with preorder[preorder_start].
            if preorder_start + 1 <= preorder_end:                                                                           #If preorder_start + 1 <= preorder_end, current node has child.
                index = postorder_index[preorder[preorder_start + 1]]                                                        #Find the index of preorder[preorder_start + 1] in postorder.
                left_length = index - postorder_start + 1                                                                    #Calculate the node count of left child in postorder(same in preorder).
                node.left = construct(preorder_start + 1, preorder_start + left_length, postorder_start, index)              #Recurisively construct left child.
                node.right = construct(preorder_start + left_length + 1, preorder_end, index + 1, postorder_end - 1)         #Recurisively construct right child.
            return node
        
        return construct(0, len(preorder) - 1, 0, len(postorder) - 1)                                                        #Construct tree from root and return.

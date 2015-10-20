# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        result=[]
        if root==None:
            return result
        end=TreeNode(-1)
        stack=[]                                      #The same as Binary Tree Preorder Traversal, as long as come to a leaf node, calculate the root number and add it to sum
        stack.append(end)
        
        flag=[]
        isleaf={}                                     #dictionary to indicate whether a treenode is a leaf node
        write=False
        flag.append(True)
        while root!=end:
            if write==False:
                write=True
            if root.left!=None:
                isleaf[root]=False                    #have left child, not leaf, add to dictionary
                temp=root.left
                root.left=None
                stack.append(root)
                flag.append(write)
                root=temp
                write=False
            else:
                if root.right!=None:
                    isleaf[root]=False                #have right child, not leaf, add to dictionary
                    temp=root.right
                    root.right=None
                    stack.append(root)
                    flag.append(write)
                    root=temp
                    write=False
                else:
                    if root not in isleaf:            #not exist in dictionary, must be leaf
                        length=len(stack)
                        temp=root.val
                        for i in range(0,length-1):   #calculate path sum
                            temp+=stack[length-1-i].val
                        if temp==sum:
                            current=[]                #generate list of path
                            for i in range(0,length-1):
                                current.append(stack[i+1].val)
                            current.append(root.val)
                            result.append(current)    #add to result
                    root=stack.pop()
                    write=flag.pop()
        return result

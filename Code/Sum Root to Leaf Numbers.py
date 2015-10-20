# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root==None:
            return 0
            
        sum=0

        end=TreeNode(-1)
        stack=[]                                              #The same as Binary Tree Preorder Traversal, as long as come to a leaf node, calculate the root number and add it to sum
        stack.append(end)
        
        flag=[]
        isleaf={}                                             #dictionary to indicate whether a treenode is a leaf node
        write=False
        flag.append(True)
        while root!=end:
            if write==False:
                write=True
            if root.left!=None:
                isleaf[root]=False                            #have left child, not leaf, add to dictionary
                temp=root.left
                root.left=None
                stack.append(root)
                flag.append(write)
                root=temp
                write=False
            else:
                if root.right!=None:
                    isleaf[root]=False                        #have right child, not leaf, add to dictionary
                    temp=root.right
                    root.right=None
                    stack.append(root)
                    flag.append(write)
                    root=temp
                    write=False
                else:
                    if root not in isleaf:                    #not exist in dictionary, must be leaf
                        length=len(stack)                     
                        temp=0                                
                        for i in range(0,length-1):           #calculate root number, note:stack[0] is end node(TreeNode(-1)), also the stack does not contain current leaf node
                            temp+=pow(10,i)*stack[length-1-i].val
                        sum+=temp*10+root.val                 #add to sum
                    root=stack.pop()
                    write=flag.pop()
        return sum

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        dict={}
        def maxSum(node):                         #return the larger one of max possible sum of left branch and max possible sum of right branch
            if node==None:
                return 0
            if node not in dict:
                numl=maxSum(node.left)            #numl is the max path sum of the tree whose root is node.left
                numr=maxSum(node.right)           #numr is the max path sum of the tree whose root is node.right
                numw=check(node.val,numl+numr,msum)     #check whether numl+numr>0
                sumLeft=check(node.val,numl,msum)       #the max possible sum of left branch 
                sumRight=check(node.val,numr,msum)      #the max possible sum of right branch
                dict[node]=max(sumLeft,sumRight)        
            return dict[node]
        def check(value,sum,msum):                #check whether current sum is larger than max sum
            if sum>0:
                sum+=value
            else:
                sum=value
            if sum>msum[-1]:
                msum.append(sum)
            return sum
                    
        msum=[root.val]                           #'msum' is used to store the max path sum, initialed with 'root.val'
        maxSum(root)                                    
        return msum[-1]

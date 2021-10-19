class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []                                    #Initialize a stack to store all elements currently do not have next greater element.
        greaterElement = {}                           #Store next greater element of each element.
        for i, x in enumerate(nums2):                 #Traverse nums2.
            while stack and stack[-1] < x:            #While stack is not empty and stack top is smaller than x.
                top = stack.pop()                     #Pop stack.
                greaterElement[top] = x               #Its next greater element is x.
            stack.append(x)                           #Append x to stack.
        for x in stack:                               #For each element remain in stack, they have no next greater element.
            greaterElement[x] = -1
        return [greaterElement[x] for x in nums1]     #For each element in nums1, return its next greater element in a list.

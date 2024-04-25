class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []                                          #Initialize stack.
        for i, x in enumerate(heights):                     #Traverse heights.
            while stack and heights[stack[-1]] <= x:        #Keep stack mono desending for the height of each index.
                stack.pop()
            stack.append(i)
        return stack                                        #Return stack.

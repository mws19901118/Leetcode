class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        result = [0] * len(heights)                        #Initialize result for each person.
        stack = []                                         #Use a mono stack to store the indexes of people who can still see more in descending order by its height.
        for i, x in enumerate(heights):                    #Traverse heights.
            while stack and heights[stack[-1]] < x:        #While stack is not empty and the height at top of stack smaller than x, pop stack and increase the result of that index because person on that index can see current person.
                result[stack.pop()] += 1
            if stack:                                      #If stack is not empty, increase the result of top of stack because that person can see current person.
                result[stack[-1]] += 1
            stack.append(i)                                #Append i to stack.
        return result

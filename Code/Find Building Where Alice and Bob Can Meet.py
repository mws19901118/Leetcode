class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        sq = sorted([(max(x, y), min(x, y), i) for i, (x, y) in enumerate(queries)], reverse = True)      #For each query x, y, swap x and y if x > y; then sort them along with original index in desending order. 
        result = [-1] * len(queries)                                                                      #Initialize result for each query,
        stack = []                                                                                        #Use a stack to store the heights from behind in desending order(because for any buiding, if there is a higher building in front of it but after the 2 buildings in query, then Alice and Bob will always meet at the taller building); to make bisect_left work, convert it to negative height in asending order,
        index = 0                                                                                         #Use index to traverse sorted queries.
        for i in reversed(range(len(heights))):                                                           #Traverse heights from behind.
            while stack and stack[-1][0] >= -heights[i]:                                                  #While stack is not empty and negative height at top of stack is greater than current negative height, pop stack.
                stack.pop()
            stack.append((-heights[i], i))                                                                #Append current negative height and index to stack.
            while index < len(sq) and sq[index][0] == i:                                                  #While index hasn't reached the end and the y of current query is i, process the query.
                if sq[index][0] == sq[index][1] or heights[sq[index][0]] > heights[sq[index][1]]:         #If x == y or heights[x] < heights[y] in query, Alice and Bob will meet at y, so update corresponding result to y.
                    result[sq[index][2]] = sq[index][0]
                else:                                                                                     #Otherwise, binary search the leftmost index to insert (-heights[x], -1) in stack.
                    j = bisect_left(stack, (-heights[sq[index][1]], -1))
                    if j:                                                                                 #If the insert index is not 0, then height in stack[j - 1] is greater than heights[x](also greater than heights[y)), so Alice and Bob will meet at the index in stack[j - 1].
                        result[sq[index][2]] = stack[j - 1][1]
                index += 1                                                                                #Move forward index.
            if index == len(sq):                                                                          #If index reaches the end, stop loop.
                break
        return result

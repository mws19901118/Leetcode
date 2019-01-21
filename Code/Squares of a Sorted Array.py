class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        minAbs = max(abs(A[0]), abs(A[-1])) + 1
        index = -1
        for i, a in enumerate(A):                                 #Find the element in A with min abs value and its index.
            if abs(a) < minAbs:
                minAbs = abs(a)
                index = i
        squares = [minAbs ** 2]                                   #Add the square of minAbs to the squares list.
        left = index - 1                                          #Left pointer, traverse to the left of index.
        right = index + 1                                         #Right pointer, traverse to the right of index.
        while len(squares) < len(A):
            if right >= len(A) or abs(A[left]) <= abs(A[right]):  #If right pointer reaches the right end or the abs value of right pointer is not smaller than that of left pointer, add the square of value of left pointer to the squares list. 
                squares.append(A[left] ** 2)
                left -= 1
            else:                                                 #Otherwise, add the square of value of right pointer to the squares list. 
                squares.append(A[right] ** 2)
                right += 1
        return squares

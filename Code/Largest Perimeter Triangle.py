class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()                                    #Sort A.
        for i in xrange(len(A) - 3, -1, -1):        #Find the largest consecutive elements which can form a triangle, then return the sum of those 3.
            if A[i] + A[i+1] > A[i+2]:              #Let's say they are a < b < c. If a + b <= c, then any a' and b' before a and b will have a' + b' <= c. Thus no valid triangle existed given the longest edge is c.
                return A[i] + A[i+1] + A[i+2]       #Otherwise a + b > c, it's a valid triangle and any a' abd b' before a and b will have a' + b' <= a + b. Thus, a + b + c has the longest perimeter for the triagnle whose longest edge is c.
        return 0                                    #If no valid triangle found, return 0.

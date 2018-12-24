class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        l = len(A)
        if l < 3:                                               #If length is smaller than 3, A is not mountain array.
            return False
        front = 0                                               #Find the index of peak element from the front.
        while front + 1 < l and A[front + 1] > A[front]:
            front += 1
        back = l - 1                                            #Find the index of peak element from the back.
        while back - 1 >= 0 and A[back - 1] > A[back]:
            back -= 1
        return front == back and front != l - 1 and back != 0   #Front and back should be equal and also can't be on the boundary of either side of A.

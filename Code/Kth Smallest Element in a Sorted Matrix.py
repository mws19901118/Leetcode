class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minV, maxV = matrix[0][0], matrix[-1][-1]       #Get the min value and max value in matrix.
        while minV < maxV:                              #Bianry search kth smallest element from minV to maxV.
            mid = (minV + maxV) // 2                    #Get mid of minV and maxV.
            count, x, y = 0, 0, len(matrix) - 1         #Count how many elements are no larger than mid. And initialize a pointer to the upper right corner.   
            while x < len(matrix) and y >= 0:           #While the pointer is valid.
                if matrix[x][y] <= mid:                 #If current value is no larger than mid, all elements before current element and in the same row are no larger than mid.
                    count += y + 1                      #Update count.
                    x += 1                              #Move to next row.
                else:                                   #Otherwise, move to previous column.
                    y -= 1
            if count < k:                               #If count is smaller than k, update minV to continue binary search in the 2nd half.
                minV = mid + 1
            else:                                       #Otherwise, update maxV to continue binary search in 1st half.
                maxV = mid
        return maxV                                     #Return maxV after binary search.

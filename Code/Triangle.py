class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        n=len(triangle)
        minimum=[triangle[0][0]]                                      #list which stores the minimum path sums from top to every bottom element(update every row)
        for i in range(1,n):
            start=minimum[0]+triangle[i][0]                           #the leftmost sum
            end=minimum[i-1]+triangle[i][i]                           #the rightmost sum
            for j in range(1,i):
                temp=min(minimum[j-1],minimum[j])+triangle[i][j]      #use the sum of current number and the minimum of the two adjacent numbers in the last raw to update the list
                minimum[j-1]=temp
            minimum.insert(0, start)                                  #insert the leftmost sum to the list
            minimum[i]=end                                            #change the last element of list to the rightmost sum
        return min(minimum)                                           #return the minimum element of the list

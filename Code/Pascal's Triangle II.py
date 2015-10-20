class Solution:
    # @return a list of integers
    def getRow(self, ):
        def f(n):  
            if n==0 or n==1:
                return 1
            else:
                return n*f(n-1)

        row=[]
        for i in range(rowIndex+1):
            row.append(f(rowIndex)/(f(i)*f(rowIndex-i)))
        return row

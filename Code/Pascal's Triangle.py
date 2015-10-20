class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        triangle=[]
        for i in range(numRows):
            temp=[1]
            if i>0:
                for j in range(len(triangle[i-1])-1):
                    temp.append(triangle[i-1][j]+triangle[i-1][j+1])
                temp.append(1)
            triangle.append(temp)
        return triangle

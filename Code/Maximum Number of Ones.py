class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        count = []                                                                            #Store the number of equivalent cell in matrix for each cell in the top left sub-matrix which is sideLength by sideLength.
        for i, j in product(range(sideLength), range(sideLength)):                            #Traverse the top left sub-matrix and assume it's filled with ones optimally.
            num = ceil((width - i) / sideLength) * ceil((height - j) / sideLength)            #For each columns or rows, we can shift them to new positions while moving the sun-matrix rightward or downward; and the new cell is equivalent with original cell. Now just calculate how mach equivalent cell the current cell has(include self).
            count.append(num)                                                                 #Append num to count.
        count.sort(reverse = True)                                                            #Sort count in desending order.
        return sum(count[:maxOnes])                                                           #Return the largest maxOnes number in count.

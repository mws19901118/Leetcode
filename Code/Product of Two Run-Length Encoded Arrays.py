class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        result = []
        i, j = 0, 0                                              #Use 2 pointers to traverse encoded1 and encoded2.
        while i < len(encoded1) and j < len(encoded2):
            count = min(encoded1[i][1], encoded2[j][1])          #The count of current product is min value of encoded1[i][1] and encoded2[j][1].
            product = encoded1[i][0] * encoded2[j][0]            #Calculate product.
            if result and result[-1][0] == product:              #If result is not empty and the product of latest result is same as product. just increase its count.
                result[-1][1] += count
            else:                                                #Otherwise append [product, count] to result.
                result.append([product, count])
            encoded1[i][1] -= count                              #Decrease count from encoded1[i][1].
            if not encoded1[i][1]:                               #If encoded1[i][1] is 0, move forward i.
                i += 1
            encoded2[j][1] -= count                              #Decrease count from encoded2[j][1].
            if not encoded2[j][1]:                               #If encoded2[j][1] is 0, move forward j.
                j += 1
        return result

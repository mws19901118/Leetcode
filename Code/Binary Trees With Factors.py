class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        division = 10 ** 9 + 7
        count = Counter(arr)                                            #Store the count of binary trees we can make by its root value, initially 1 for every root value in arr.
        arr.sort()                                                      #Sort arr in asending order.
        for i, x in enumerate(arr):                                     #Traverse arr.
            for j, y in enumerate(arr[:i + 1]):                         #Traverse arr[:i + 1]
                p = x * y                                               #Calculate product.
                if p not in count:                                      #If product not in count, no valid binary tree we can make, so continue.
                    continue
                count[p] += (count[x] * count[y]) << int(x != y)        #If x == y, we can make count[x] * count[y] more binary trees; otherwise we can make count[x] * count[y] * 2 binary trees.
                count[p] %= division                                    #Calculate modulo.
        return sum(count.values()) % division                           #Return modulo of sum of values in count.

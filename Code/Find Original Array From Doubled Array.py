class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)                                        #Count each number.
        if count[0] % 2:                                                #If count of 0 is odd, doubled array cannot be formed, so return empty array.
            return []
        for x in sorted(count):                                         #Traverse sorted key in count.
            if count[x] > count[2 * x]:                                 #If count[x] > count[2 * x], not enough number to double x, so return empty array.
                return []
            count[2 * x] -= count[x] if x else count[x] // 2            #Substract count[x] from count[2 * x] if x is not 0; otherwise, substract count[0] // 2 from count[0].
        return list(count.elements())                                   #Return count.elements().

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)                                                #Count each number in arr.
        pairs = sorted((value, key) for key, value in count.items())        #Sort unique number and its count by the count in asending order.
        for i, (value, key) in enumerate(pairs):                            #Traverse number and count pair.
            k -= value                                                      #Remove all current number.
            if k < 0:                                                       #If k < 0, we cannot remove more, then return the length of remaining unique number.
                return len(pairs) - i
        return 0                                                            #Return 0 is all removed.

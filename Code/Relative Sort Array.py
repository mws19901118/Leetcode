class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)                                      #Count each element in arr1.
        remain = sorted(list(set(count.keys()) - set(arr2)))       #Sort the elements in arr1 but not in arr2 in asending order.
        result = []
        for x in arr2 + remain:                                    #Traverse arr2 then remain.
            result.extend([x] * count[x])                          #Append x for count[x] times to result.
        return result

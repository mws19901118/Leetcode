class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)                                            #Count each element.
        numberByCount = defaultdict(list)                                #Map each number by its count.
        for x, v in count.items():
            numberByCount[v].append(x)
        minV, maxV = min(count.values()), max(count.values())            #Find the min count and max count.
        result = []
        for x in reversed(range(minV, maxV + 1)):                        #Traverse from max count backward to min count.
            result.extend(numberByCount[x])                              #Append all numbers with current count to result and since result is guaranteed to be unique so we don't need to add one by one and check after adding each.
            k -= len(numberByCount[x])                                   #Reduce k by the number of numbers just added to result.
            if k <= 0:                                                   #If k <= 0, we have already find the top J frequent elements, so return result.
                return result

class Solution:
    def find(self, nums: List[int], k: int, x: int) -> List[int]:          #Same as Find X-Sum of All K-Long Subarrays I.py
        count = Counter(nums[:k])
        sortedCount = SortedList((-j, -i) for i, j in count.items())
        xSum = sum(i * j for i, j in sortedCount[:x])
        result = [xSum]

        def add(index: int) -> None:
            nonlocal xSum
            pair = (-count[nums[index]], -nums[index])
            pair_index = sortedCount.bisect_left(pair)
            if pair_index < x:
                if len(sortedCount) >= x:
                    xSum -= sortedCount[x - 1][0] * sortedCount[x - 1][1]
                xSum += pair[0] * pair[1]
            sortedCount.add(pair)
        
        def remove(index: int) -> None:
            nonlocal xSum
            pair = (-count[nums[index]], -nums[index])
            pair_index = sortedCount.bisect_left(pair)
            if pair_index < x:
                if len(sortedCount) >= x + 1:
                    xSum += sortedCount[x][0] * sortedCount[x][1]
                xSum -= pair[0] * pair[1]
            sortedCount.remove(pair)

        for i in range(len(nums) - k):
            remove(i)
            count[nums[i]] -= 1
            if count[nums[i]] != 0:
                add(i)          
            if count[nums[i + k]] != 0:
                remove(i + k)
            count[nums[i + k]] += 1
            add(i + k)
            result.append(xSum)
        return result

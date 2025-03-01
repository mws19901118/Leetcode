class Solution:
    def minSwaps(self, data: List[int]) -> int:
        count = sum(data)                                        #Count total 1 in data.
        running_count = sum(data[:count])                        #Initialize running count by count 1 in data[:count].
        result = count - running_count                           #Initialize result to be swaps to move all 1 to data[:count], which is count - running_count.
        for i in range(count, len(data)):                        #Traverse data[count:].
            running_count += data[i] - data[i - count]           #Update running count by moving data[i] in to sliding window and moving data[i - count] out of sliding window.
            result = min(result, count - running_count)          #Calculate swaps to move all 1 to data[i - count + 1:i + 1] and update result if necessary.
        return result

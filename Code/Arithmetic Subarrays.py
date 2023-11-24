class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i, j in zip(l, r):                                                #Traverse each pair of query.
            s = set(nums[i:j + 1])                                            #Put the numbers in query range into a set.
            minV, maxV = min(s), max(s)                                       #Get the min value and max value in query range.
            if (maxV - minV) % (j - i):                                       #If the number span cannot be divided by length - 1, it cannot form arutgnetuc subarray as all numbers are integers.
                result.append(False)                                          #Append false to result and continue.
                continue
            diff = (maxV - minV) // (j - i)                                   #Calculate the diff of arithmetic subarray.
            result.append(all(minV + k * diff in s for k in range(j - i)))    #Append if all numbers in arithmetic subarray are in the set.
        return result

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        total1 = sum(arr)                                                                                     #Count 1 in arr.
        if total1 % 3:                                                                                        #If total1 cannot be divided by 3, arr cannot be divide into 3 parts.
            return [-1, -1]
        elif total1 == 0:                                                                                     #If no 1 exists in arr, return [0, 2] as a valid result for all 0 array.
            return [0, 2]
        first1, trailing0 = [len(arr)] * 3, [-1] * 3                                                          #Initialize the index of first 1 and number of trailing 0 of each part.
        share, count, part = total1 // 3, 0, 0                                                                #Calculate the share of 1 in each part; also initialize the count of 1 and which part current number belongs to for the traverse below.
        for i, x in enumerate(arr):                                                                           #Traverse arr.
            count += x                                                                                        #Add x to count to get current count of 1 in current part.
            if count > share:                                                                                 #If current part have more 1 than share, we enter the next part.
                count -= share
                part += 1
            if count == 1:                                                                                    #If current count is 1, update the idnex of first 1 in current part, if necessary.
                first1[part] = min(first1[part], i)
            if count == share:                                                                                #If current count eqauls share, we reach the trailing 0 section of current part, update the number of trailing 0.
                trailing0[part] += 1
        if trailing0[2] > trailing0[0] or trailing0[2] > trailing0[1]:                                        #If the last part has more trailing 0 than previous 2 parts, arr cannot be divide into 3 parts. Because trailing 0 of last part is fixed and previous 2 parts cannot have enough trailing 0.
            return [-1, -1]
        part1Kernel = arr[first1[0]:first1[1] - trailing0[0]]                                                 #Get the kernal of part1(without leading or trailing 0).
        part2Kernel = arr[first1[1]:first1[2] - trailing0[1]]                                                 #Get the kernal of part2(without leading or trailing 0).
        part3Kernel = arr[first1[2]:len(arr) - trailing0[2]]                                                  #Get the kernal of part3(without leading or trailing 0).
        if all(a == b == c for a, b, c in zip(part1Kernel, part2Kernel, part3Kernel)):                        #If part1Kernel, part2Kernel, part3Kernel are exactly same, return the i, j pair which makes part1 and part2 has same length of trailing 0 with part3. 
            return [first1[1] - trailing0[0] - 1 + trailing0[2], first1[2] - trailing0[1] + trailing0[2]]
        else:                                                                                                 #Otherwise, arr cannot be divide into 3 parts.
            return [-1, -1]

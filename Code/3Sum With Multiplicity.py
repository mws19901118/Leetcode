class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        division = 10 ** 9 + 7                                                                                      #Division is 10 ** 9 + 7.
        counter = Counter(arr)                                                                                      #Count each number.
        distinct = sorted(counter.keys())                                                                           #Sort the keys to get sorted distinct numbers list.
        result = 0
        for i, x in enumerate(distinct):                                                                            #Traverse distinct.
            for y in distinct[i:]:                                                                                  #Traverse distinct[i:] so x <= y.
                z = target - x - y                                                                                  #Calculate z.
                if z in counter and z >= y:                                                                         #If z in counter and z >= y, we may find a combination of 3 sum.
                    if x == z:                                                                                      #If x == z, x, y and z are same so add max(counter[x] * (counter[x] - 1) * (counter[x] - 2) // 6, 0) % division to result.
                        result += max(counter[x] * (counter[x] - 1) * (counter[x] - 2) // 6, 0) % division
                    elif x == y:                                                                                    #If x == y, add counter[x] * (counter[x] - 1) // 2 * counter[z] % division to result.
                        result += counter[x] * (counter[x] - 1) // 2 * counter[z] % division
                    elif y == z:                                                                                    #If y == z, add counter[y] * (counter[y] - 1) // 2 * counter[x] % division to result.
                        result += counter[y] * (counter[y] - 1) // 2 * counter[x] % division
                    else:                                                                                           #Otherwise, add counter[x] * counter[y] * counter[z] % division to result.
                        result += counter[x] * counter[y] * counter[z] % division
        return result

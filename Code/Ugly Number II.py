class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]                                                                               #1 is the 1st ugly number.
        i2, i3, i5 = 0, 0, 0                                                                     #i2, i3, i5 indicates the index of previous ugly number to generate new ugly number by multiplying 2, 3 and 5 respectively/
        while len(ugly) < n:
            n2, n3, n5, next_ugly = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5, 0                  #Calculate the 3 new possible ugly number and initialize next ugly number.
            n3 = ugly[i3] * 3
            n5 = ugly[i5] * 5
            if n2 <= n3 and n2 <= n5:                                                            #Find the smallest one among n2, n3 and n5 to be the candidate of next ugly number and move forward the correspoding index by 1.
                next_ugly = n2
                i2 += 1
            elif n3 <= n2 and n3 <= n5:
                next_ugly = n3
                i3 += 1
            else:
                next_ugly = n5
                i5 += 1
            if next_ugly != ugly[-1]:                                                            #If the new ugly number is not equals to the largest ugly number, append it to the array.
                ugly.append(next_ugly)
        return ugly[-1]                                                                          #Return the ugly number we want.

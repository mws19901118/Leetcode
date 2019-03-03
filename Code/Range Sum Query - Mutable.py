class NumArray:
    def __init__(self, nums):
        self.nums = [0] * len(nums)                                     #Store the original nums.
        self.bit = [0] * (len(nums) + 1)                                #Binary Indexed Tree, the index starts with 0 here for convenience. Thus self.bit[i + 1] is corresponding to self.nums[i].
        for i, n in enumerate(nums):                                    #Because both nums and bit are intialed with all 0s, update them for each number. 
            self.update(i, n)
        self.sumRange = lambda i, j: self.Sum(j + 1) - self.Sum(i)      #The range sum from i to j is the sum from 0 to j minus the sum from 0 to i - 1, so use a lambda function to return the result.

    def update(self, i, val):                                           #Update new value index i.
        diff, self.nums[i] = val - self.nums[i], val                    #Calculate diff and update self.nums[i].
        i += 1                                                          #Now update self.bit, so increase the index by 1.
        while i < len(self.bit):                                        #Update from start to end.
            self.bit[i] += diff                                         #Update the value in self.bit for current index.
            i += (i & -i)                                               #Go to next. "i & -i" calculates the max power of 2 which is a divider of i. "i + (i & -i)" is the higher level sum to update.
                                                                        #For example, i = 10. Then, i in binary is 1010; -i in binary is 0110. i & -i is 2 and i + (i & -i) is 12, the next sum in bit to update(if bit's length is enough).
    def Sum(self, k):                                                   #Calculate the range sum from 0 to k - 1.
        result = 0                                                      #Initailize result.
        while k:
            result += self.bit[k]                                       #Add the value in self.bit for current index.
            k -= (k & -k)                                               #Here is the revert process of "i += (i & -i)" in update.
        return result                                                   #For example, k = 10. Then, k in binary is 1010; -k in binary is 0110. k & -k is 2 and k - (k & -k) is 8.
                                                                        #Range sum from 0 to 9 is self.bit[8](sum from 0 to 7) + self.bit[10](sum from 8 to 9).

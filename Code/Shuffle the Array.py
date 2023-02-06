class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n, 2 * n):                                                         #Traverse second half of nums.
            nums[i - n] |= (nums[i] << 10)                                                #Since the value of element is smaller than 1000, it can be put in a 10 bits long int. So, left shift each y 10 bits then or with its corresponding x. Now, each element in the first half has fitst 10 bits as y and last 10 bits as x.

        allOnesMask = int(pow(2, 10)) - 1                                                 #Create a bit mask for 1111111111.
        for i in reversed(range(n)):                                                      #Traverse first half reversely.
            nums[2 * i], nums[2 * i + 1] = nums[i] & allOnesMask, nums[i] >> 10           #Update nums[2 * i] and nums[2 * i + 1] to be the last 10 bits and first 10 bits of current value respectively.
        return nums                                                                       #Return nums.

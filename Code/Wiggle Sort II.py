class Solution(object):
    def swap(self, nums, i, j):                                                                                                                               #Swap 2 numbers in the array.
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t

    def replace(self, nums, current, substitution):                                                                                                           #If current number equals the next number, replace one of them with substitution.
        if current % 2 == 0:                                                                                                                                  #If current is even, replace current if substitution is smaller or replace the next number if substitution is larger.
            if nums[substitution] > nums[current]:
                self.swap(nums, current + 1, substitution)
            else:
                self.swap(nums, current, substitution)
        else:                                                                                                                                                 #If current is odd, replace current if substitution is larger or replace the next number if substitution is smaller.
            if nums[substitution] < nums[current]:
                self.swap(nums, current + 1, substitution)
            else:
                self.swap(nums, current, substitution)
                
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        current = 0                                                                                                                                           #Record the index of current number.
        before = 0                                                                                                                                            #Record the index of number(before current index) to swap with current number.
        after = 2                                                                                                                                             #Record the index of number(after current index) to swap with current number.
        while current < len(nums) - 1:                                                                                                                        #Traverse until current number is the last one.
            if after == current + 1:                                                                                                                          #"after" should be at least 2 numbers ahead "current".
                after += 1
            if nums[current] != nums[current + 1]:                                                                                                            #If current number does not equal the number after current number, simply wiggle sort the 2 number.
                if (current % 2 == 0 and nums[current] > nums[current + 1]) or (current % 2 == 1 and nums[current] < nums[current + 1]):                      #If current is even, current number should be the smaller one; otherwise, it should be the larger one.
                    self.swap(nums, current, current + 1)
            else:                                                                                                                                             #If current number equals the number after current number, we have to find a different number to replace one of the 2 numbers.
                while after < len(nums) and nums[after] == nums[current]:                                                                                     #First, find such number behind the number after current number.
                    after += 1
                if after != len(nums):                                                                                                                        #If found such number, replace one of the 2 numbers.
                    self.replace(nums, current, after)
                else:                                                                                                                                         #If can't find, find such number before current number.
                    while before < current:
                        if nums[before] != nums[current]:                                                                                                     #It shouldn't equal current number.
                            if before % 2 == 0:                                                                                                               #If the before is even, current number should be smaller than the min value of the neighbors of before(or nums[1] if before is 0).
                                if (before == 0 and nums[current] < nums[1]) or (before > 0 and nums[current] < min(nums[before - 1], nums[before + 1])):
                                    break
                            else:                                                                                                                             #Otherwise, current number should be laeger than the max value of the neighbors of before.
                                if nums[current] > max(nums[before - 1], nums[before + 1]):
                                    break
                        before += 1
                    self.replace(nums, current, before)                                                                                                       #If found such number, replace one of the 2 numbers.
            current += 1
        print nums

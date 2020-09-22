class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:      #Implement Boyer-Moore Majority Vote algorithm(http://gregable.com/2013/10/majority-vote-algorithm-find-majority.html).
        candidate1, candidate2 = None, None                       #To find all elements that appear more than ⌊ n/3 ⌋ times, there are at most 2 elements fit the requirement(note as candidate1 and candidate2).
        count1, count2 = 0, 0                                     #Record the times of qppearance of corresponding candidate.
        for i in nums:
            if i == candidate1:                                   #If current element equals candidate1, increase count1 by 1.
                count1 += 1
            elif i == candidate2:                                 #Else if current element equals candidate2, increase count2 by 1.
                count2 += 1
            elif count1 == 0:                                     #Else if current element doesn't equal any candidates and count1 equals 0, let current element be the new candidate1 and update count1.
                candidate1, count1 = i, 1
            elif count2 == 0:                                     #Else if current element doesn't equal any candidates and count2 equals 0, let current element be the new candidate2 and update count2.
                candidate2, count2 = i, 1
            else:                                                 #Otherwise, decrease count1 and count2 by 1. When encountering a new element, we don't know if it will be the majority and we also don't know the following situation. So, we offset the 1 appearence of candidates.
                count1 -= 1
                count2 -= 1
        majority = []
        if nums.count(candidate1) > len(nums) // 3:               #We don't know if the appearance of the majority we get with the above method is more than ⌊ n/3 ⌋ times, we have to double-check it.
            majority.append(candidate1)
        if nums.count(candidate2) > len(nums) // 3:
            majority.append(candidate2)
        return majority

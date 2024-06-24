class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flipStarts = deque()                                      #Use deque to store the start index of each flip in sliding window.
        count = 0                                                 #Initialize flip count.
        for i, x in enumerate(nums):                              #Since the order of flip doesn't matter, we traverse nums from front and assume we make necessary flips in same order.
            while flipStarts and flipStarts[0] + k - 1 < i:       #While deque is not empty and the first index in deque is at least k elements away from current index, pop left deque as the flip on popped index has no more effect on current number.
                flipStarts.popleft()
            if not (x + len(flipStarts)) & 1:                     #Now, current number is flipped len(flipStarts) times, so determine if it is 0 after all the flips; if it is, continue the processing logic.
                if i < len(nums) - k + 1:                         #If there are at least k - 1 numbers after current number, i.e. it is valid to do a flip starting at current number, flip k numbers starting at current number and increase count also append current index to deque.
                    flipStarts.append(i)
                    count += 1
                else:                                            #Otherwuse, this is a 0 cannot be flipped, return -1.
                    return -1
        return count

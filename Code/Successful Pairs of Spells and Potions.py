class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()                                                                              #Sort potions in asending order.
        return [len(potions) - bisect_left(potions, ceil(success / x)) for x in spells]             #For each spell x, binary search the index to insert ceil(success / x) in potions, and all the potions at index or to the right can form a success pair with x. Let's say it's y and y >= ceil(success / x), then x * y >= x * ceil(success / x) >= x * success / x = success. 

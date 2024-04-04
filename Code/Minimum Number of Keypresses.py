class Solution:
    def minimumKeypresses(self, s: str) -> int:
        sortedCount = sorted(Counter(s).values(), reverse = True)                                        #Count each character in s and sort the count in desending order.
        return sum(sortedCount[:9]) * 1 + sum(sortedCount[9:18]) * 2 + sum(sortedCount[18:]) * 3         #For the first 9 characters, map them at first of each digit so it only needs one press to type them.
                                                                                                         #For the next 9 characters, map them at second of each digit so it only needs two press to type them.
                                                                                                         #For the rest, map them at third of each digit so it needs three press to type them.
                                                                                                         #Sum up and return.

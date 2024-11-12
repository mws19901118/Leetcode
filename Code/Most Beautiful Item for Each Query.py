class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        max_beauty = [(0, 0)]                                                                 #Initialize max beauty at each price with price 0 and beauty 0.
        for p, b in sorted(items):                                                            #Traverse sorted items by price in ascending order.
            max_beauty.append((p, max(b, max_beauty[-1][1])))                                 #For each price, append the price and the max beauty so far to max beauty.
        return [max_beauty[bisect_right(max_beauty, (x, inf)) - 1][1] for x in queries]       #For each query x, binary search for the rightmost index to insert (x, inf) in max beauty, then the result is the beauty on index - 1.

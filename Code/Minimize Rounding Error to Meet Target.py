class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        numbers = sorted([float(x) for x in prices], key = lambda x: ceil(x) - x)                                                          #Convert price to float and sort by its error of rouding to ceil in asending order.
        lowerBound, upperBound = sum(floor(x) for x in numbers), sum(ceil(x) for x in numbers)                                             #Calculate the lower bound and upper bound after rounding.
        if target < lowerBound or target > upperBound:                                                                                     #If target is not within bound, return "-1".
            return "-1"
        numbers = [x for x in numbers if floor(float(x)) != ceil(float(x))]                                                                #Remove the numbers that are at integer, because round them to ceil won't make any difference.
        result = sum(ceil(x) - x for x in numbers[:target - lowerBound]) + sum(x - floor(x) for x in numbers[target - lowerBound:])        #We have to round target - lowerBound numbers to ceil, while round the rest to floor. So, we round the first target - lowerBound numbers to ceil because they are already sorted.
        return "{:.3f}".format(result)                                                                                                     #Sum up the overall error and convert to string with 3 precisions then return.

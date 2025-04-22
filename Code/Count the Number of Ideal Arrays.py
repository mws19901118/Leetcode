class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        division = 10 ** 9 + 7                                                      #Initialize division.
        count = {x: 1 for x in range(1, maxValue + 1)}                              #Count the number of unique ideal array(the unique combination of digits) ending at each value for current length; initially it is 1 for each number from 1 to max value(ideal array formed by only one number).
        result = maxValue                                                           #Initialize result to be max value.
        for x in range(1, n):                                                       #Iterate array length before appending from 1 to n - 1.
            new_count = Counter()                                                   #Initialize new count.
            for y in count:                                                         #Traverse current count.
                for multiplier in range(2, maxValue // y + 1):                      #Multiplier of y should be from 2 to maxValue // y to not exceed max value.
                    result = (result + comb(n - 1, x) * count[y]) % division        #For each of unique ideal array ending at y, we can append y * multiplier to make a new ideal array. Because we only need to keep the relative increasing order so there is comb(n - 1, x) ways to arrange the array to keep relative increasing order from unique ideal array. Take modulo at the end.
                    new_count[multiplier * y] += count[y]                           #Add count[y] to new_count[multiplier * y].
            count = new_count                                                       #Replace count with new_count.
        return result

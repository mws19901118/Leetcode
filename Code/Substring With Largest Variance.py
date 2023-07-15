class Solution:
    def largestVariance(self, s: str) -> int:
        distinct = set([x for x in s])                                            #Get the distinct characters in s.
        pairs = [(x, y) for x in distinct for y in distinct if x != y]            #Generate all possible characters pairs in s that the 2 characters are not equal.
        variance = 0                                                              #Initialize max variance.
        for x, y in pairs:                                                        #Traverse paris and find the max variance of each pair in all substrings.
            diff, count, startWithY = 0, 0, False                                 #Initialize the max diff of occurance(assuming the occurance of x is larger), count of x and if the substring has to start with y.
            for z in s:                                                           #Traverse s.
                if z == x:                                                        #If z == x, increase both diff and count by 1.
                    diff += 1
                    count += 1
                elif z == y:                                                      #If z == y, decrease diff by 1.
                    if startWithY and diff >= 0:                                  #But before decreasing diff, check if substring starts with y and diff is not smaller than 0.
                        diff += 1                                                 #If so, it means the current substring starts with y and follows by a number of x.
                        startWithY = False                                        #Since we encounter another y now, we can ditch the first y, so increase diff by 1 and set startWithY to false.
                    diff -= 1
                    if diff <= -1:                                                #If diff is not greater than -1, any x before current y is not worth for further calculation, just start a new substring starting with y.
                        diff = -1
                        startWithY = True
                if diff < count:                                                  #If diff < count, substring is not all x, so diff is valid variance and then update max variance if necessary.
                    variance = max(variance, diff)
        return variance                                                           #Return variance.

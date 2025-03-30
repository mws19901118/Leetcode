class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        max_num = max(nums)                                                          #Find the max number in nums.
        isPrime, primes = [True] * (max_num + 1), []                                 #Find all primes up to the max number.
        for i in range(2, max_num + 1):                                              #Traverse from 2 to max number.
            if isPrime[i]:                                                           #If i is prime, append i to primes.
                primes.append(i)
                j = i * i                                                            #Start from i * i to max number, set all numbers that are times of i to non prime.
                while j <= max_num:
                    isPrime[j] = False
                    j += i

        @cache                                                                       #Cache result.
        def calculateScore(x: int) -> int:                                           #Calculate the prime score of given number.
            result, i = 0, 0                                                         #Initialize result and i to traverse primes.
            while x > 1 and i < len(primes) and primes[i] * primes[i] <= x:          #Iterate while x is greater than 1 and i hasn't reached the end and square of primes[i] is not greater than x.
                if not x % primes[i]:                                                #If x can be divided by currrent prime, increase result.
                    result += 1
                    while not x % primes[i]:                                         #Divide x by current prime until not dividable.
                        x //= primes[i]
                i += 1
            return result + (x > 1)                                                  #Return result and plus 1 if x is still greater than 1(a large prime that is a factor of x).

        @cache                                                                       #Cachce result.
        def fastPower(base: int, exponent: int) -> int:                              #Fast Calculate base ** exponent % division.
            result = 1                                                               #Initialize result.
            while exponent > 0:                                                      #Iterate while exponent is greater than 0.
                if exponent % 2 == 1:                                                #If current exponent is odd, multiple result by base and calculate the remain.
                    result = (result * base) % division
                base = (base * base) % division                                      #Update base to the square of current base then calculate the remain.
                exponent >>= 1                                                       #Divide exponent by 2.
            return result

        score = [calculateScore(x) for x in nums]                                    #Calculate the prime score of each number.
        score.append(10000)                                                          #Append a large score, 10000 to the end of score to simulate the end.
        stack = [(10001, -1)]                                                        #Initialize stack to a large score, 10001 which has to be greater than 10000 so it won't be popped, and index -1 to simulate the start.
        operations = []                                                              #Initialize operations to be the number and times it can be used.
        for i in range(len(nums) + 1):                                               #Traverse nums and the end.
            while stack and stack[-1][0] < score[i]:                                 #While stack is not empty and top of the stack has a smaller score than current score, pop stack to get the index of top of the stack.
                _, j = stack.pop()
                operations.append((nums[j], (i - j) * (j - stack[-1][1])))           #Append nums[j] and (i - j) * (j - stack[-1][1]) to operations, because for nums[j], nums[stack[-1][1]] on the left and nums[i] on the right have higher prime score then nums[j] can be used (i - j) * (j - stack[-1][1]) times at most.
            stack.append((score[i], i))                                              #Append score and index of current number to stack,
        
        operations.sort(reverse = True)                                              #Sort operations in reverse order.
        division = 10 ** 9 + 7                                                       #Initialize division.
        result, index = 1, 0                                                         #Initialize result and index to traverse operations.
        while k and index < len(operations):                                         #Iterate while k is greater than 0 and index hasn't reached the end.
            count = min(k, operations[index][1])                                     #For current number, it can be used at most min(k, operations[index][1]) times.
            result *= fastPower(operations[index][0], count)                         #Multiply the fast power(after taking the remain) of current number as base and count as exponent to result.
            result %= division                                                       #Calculate the remain and update result.
            k -= count                                                               #Decrease k by count.
            index += 1                                                               #Move index to next.
        return result

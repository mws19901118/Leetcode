class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        visited = set()                                                                                        #Store visited k-palindromic numbers.
        half = (n + 1) // 2                                                                                    #Calculate the half of n.
        result = 0                                                                                             #Initialize result.
        for i in range(1, 10 ** half):                                                                         #Enumerate number from 1 to 10 ** half - 1.
            s = str(i).zfill(half)                                                                             #Convert number to string and fill leading zeros to make it 
            full = (s[::-1] + s) if not n & 1 else (s[1:][::-1] + s)                                           #Mirror the half to full palindrome string.
            if full[0] == '0' or int(full) % k:                                                                #If the full string has leading 0 or cannot be divided by k, skip.
                continue
            sorted_full = "".join(sorted([x for x in full]))                                                   #Sort digits in full string then join them to dedupe.
            if sorted_full in visited:                                                                         #If it is already seen, continue.
                continue
            visited.add(sorted_full)                                                                           #Add the sorted full string to visited.
            count = Counter(full)                                                                              #Count each digit in full string.
            result += (n - count['0']) * factorial(n - 1) // prod(factorial(x) for x in count.values())        #There are (n - count['0']) * (n - 1)! permutations, because there cannot be leading 0; then divide it be product of factorial of each digit count; next add it to final result.
        return result

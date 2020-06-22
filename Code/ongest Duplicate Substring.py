class Solution:
    def findDuplicate(self, S: str, length: int) -> int:        #Rabin-Karp algorithm, find duplicate substrings with given length.
        bigPrime = 2305843009213693951                          #Use a big prime(2^61 - 1) as modulo.
        A = [ord(c) - ord('a') for c in S]                      #Calculate the distance between each character in S to 'a'(only lowercase characters in S).
        h = 0                                                   #Store the hash value of each substring.
        p = pow(26, length, bigPrime)                           #Calculate 26 ^ length % bigPrime.
        for i in range(length):
            h = (h * 26 + A[i]) % bigPrime                      #Calculate the hash of first substring.
        hashValues = set([h])                                   #Store it in a set.
        for i in range(length, len(S)):                         #For next substring, calculate the hash value using rolling hash.
            h = h * 26 + A[i] - A[i - length] * p               #Next hash = previous hash * 26 + A[ending character] - A[poping out character] * p.
            h %= bigPrime
            if h in hashValues:                                 #If found duplicate hash value, then found duplicate substring.
                 return i - length + 1                          #Return the starting index.
            hashValues.add(h)                                   #Otherwise, add current substring hash value to set.
        return None                                             #If not found, return None.
    
    def longestDupSubstring(self, S: str) -> str:
        result = (-1, -1)
        start, end = 1, len(S) - 1
        while start <= end:                                     #Binary search the anwser from 1 to len(S) - 1.
            mid = (start + end) // 2
            duplicate = self.findDuplicate(S, mid)              #Find duplicate substrings whose length is mid.
            if duplicate is not None:                           #If duplicate substring found.
                result = (duplicate, duplicate + mid)           #Update the start and end index of duplicate substring.
                start = mid + 1                                 #keep binary search from mid + 1 to len(S) - 1. 
            else:
                end = mid - 1                                   #If not found, binary search from 1 to mid - 1.
        return S[result[0]:result[1]]                           #Return the duplicate substring.

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return "" if str1 + str2 != str2 + str1 else str1[:gcd(len(str1), len(str2))]         #If 2 strings have gcd substring, the concatenation of 2 strings should be same no matter order; then the length of gcd string is the gcd of lengths of both strings.

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * 1 << (n - 1)                                            #Calculate the total possible happy strings of length n, which is 3 * 2 ** (n - 1) because the first letter has 3 choices and each of the following letter has 2 choices.
        if k > total:                                                       #If k is greater than total, return empty string.
            return ""
        mapping = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['a', 'b']}       #Map possible letter choices in lexicographical order by previous letter.
        total //= 3                                                         #Divide total by 3 to calculate the total happy strings per first letter.
        k -= 1                                                              #Decrease k so that it is 0-indexed.
        result = [chr(ord('a') + k // total)]                               #Calculate the first letter and intialize result.
        k %= total                                                          #Take the modulo to calculate the index of result happy string inside the rest happy strings after setting the first letter.
        for _ in range(n - 1):                                              #Iterate n - 1 times.
            total //= 2                                                     #Divide total by 3 to calculate the total happy strings after setting current letter.
            result.append(mapping[result[-1]][k // total])                  #Calculate current letter from the choices based on previous letter and append it to result.
            k %= total                                                      #Take the modulo to calculate the index of result happy string inside the rest happy strings after setting existing letters.
        return "".join(result)                                              #Join result and return.

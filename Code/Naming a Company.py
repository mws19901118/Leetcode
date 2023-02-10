class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        suffixByInitial = collections.defaultdict(set)                                                                      #Group suffix by initial converting to the offset to 'a'.
        for x in ideas:
            suffixByInitial[ord(x[0]) - ord('a')].add(x[1:])        
        result = 0
        for i in range(26):                                                                                                 #Traverse from a to z.
            for j in range(i + 1, 26):                                                                                      #Traverse from i + 1 to z.
                intersection = len(suffixByInitial[i] & suffixByInitial[j])                                                 #Get the intersection size of suffixes in i and suffixes in j.
                result +=  (len(suffixByInitial[i]) - intersection) * (len(suffixByInitial[j]) - intersection)              #For each pair from the suffixes of i but not in intersection and suffixes of j but not in the intersection, they can form a valid name. Since, there swapped name are not in ideas.
        return result * 2                                                                                                   #Also the order matters, so multuply the answer by 2.

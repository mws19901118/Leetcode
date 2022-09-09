class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (x[0], -x[1]))      #Sort by attack ascend and then by defense descend.
        maxD, count = 0, 0                                  #Initialize max defense and count of week characters.
        for x, y in reversed(properties):                   #Traverse properties backfard.
            if y < maxD:                                    #If current defense is smaller than maxD, current character is weak, because the character with maxD also has a greater attack value.
                count += 1
            else:                                           #Otherwise update maxD.
                maxD = max(maxD, y)
        return count

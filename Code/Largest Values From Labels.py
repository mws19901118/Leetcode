class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        sortedValues = sorted([(v, l) for v, l in zip(values, labels)], reverse = True)         #Sort value and label tuple by value in descending order.
        usedLabel = collections.defaultdict(int)                                                #Count the usage of each label.
        result, count = 0, 0                                                                    #Initialize result and count.
        for i, (v, l) in enumerate(sortedValues):                                               #Traverse sortedValues.
            if count == numWanted:                                                              #If we already take numWanted values, jump out of for loop.
                break
            if usedLabel[l] < useLimit:                                                         #If usage of label l not reaching limit, increase useLabel[l] and count by 1 and add v to result.
                usedLabel[l] += 1
                result += v
                count += 1
        return result

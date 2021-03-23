class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordSet = set(wordlist)                                               #Store words in a set.
        caseDict, vowelDict = {}, {}                                          #Intialize caseDict and vowelDict.
        for w in wordlist:                                                    #Traverse wordList.
            lower = w.lower()                                                 #Covert w to lowercase.
            if lower not in caseDict:                                         #If lower not in caseDict, store it in caseDict as key with w as value.
                caseDict[lower] = w
            replaceVowel = re.sub(r'[AEIOUaeiou]', '*', lower)                #Replace the vowels in lower with *.
            if replaceVowel not in vowelDict:                                 #If replaceVowel not in caseDict, store it in vowelDict as key with w as value.
                vowelDict[replaceVowel] = w
        result = []                                                           #Initialize the result list.
        for q in queries:                                                     #Traverse queries.
            if q in wordSet:                                                  #If q in wordSet, append it to result and continue.
                result.append(q)
                continue
            lower = q.lower()                                                 #Covert q to lowercase.
            if lower in caseDict:                                             #If lower in caseDict, append value to result and continue.
                result.append(caseDict[lower])
                continue
            replaceVowel = re.sub(r'[AEIOUaeiou]', '*', lower)                #Replace the vowels in lower with *.
            if replaceVowel in vowelDict:                                     #If replaceVowel not in caseDict, append value to result and continue.
                result.append(vowelDict[replaceVowel])
                continue
            result.append("")                                                 #If no scenarios apply, append "" to result.
        return result                                                         #Return result.

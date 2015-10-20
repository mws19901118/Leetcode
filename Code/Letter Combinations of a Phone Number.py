class Solution:
    def backtrack(self, result, current, digits, index, dict):
        if index==len(digits):                                                                        #If index equals the length of digits, the backtracking comes to an end.
            if index!=0:                                                                              #If digits is a empty string, we don't have to append anything.
                result.append("".join(current))                                                       #Otherwise, join the characters and append it to result.
        else:
            t=dict[digits[index]]                                                                     #Get the corresponding characters of current digit.
            for i in range(len(t)):
                current.append(t[i])                                                                  #Append a character to the temporary list of characters.
                self.backtrack(result, current, digits, index+1, dict)                                #Backtrack next digit.
                current.pop()                                                                         #Remove the character just appended.
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        dict={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}      #Map digits to characters.
        result=[]
        self.backtrack(result, [], digits, 0, dict)                                                   #Begin backtracking with index=h0.
        return result

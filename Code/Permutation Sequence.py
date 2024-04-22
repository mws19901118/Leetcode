class Solution:
    # @return a string
    def getPermutation(self, n, k):
        k -= 1                                                        #k minus 1, because the index of a list begins with 0.
        numbers = [i for i in range(1, n + 1)]                        #Store all available numbers in an array and keep them sorted in asending order.
        result = ""
        amount = factorial(n)                                         #Initialize the amount of permutations of n starting with a certain digit.
        while numbers:                                                #Iterate while numbers is not empty.
            fold //= len(numbers)                                     #Calculate the amount of permutations with a certain digit for current length of remaining numbers.
            index = k // fold                                         #Find the index of first digit in remaining numbers.
            result += str(numbers[index])                             #Append it to result.
            numbers = numbers[:index] + numbers[index + 1:]           #Remove it from remaining numbers and update numbers.
            k %= fold                                                 #Update k for next iteration.
        return result

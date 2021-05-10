class Solution(object):
    def strobogrammaticOfLength(self, n):                                                           #Calculate the count of strobogrammatic number of length n.
        if n == 1:
            return 3
        elif n == 2:
            return 4
        elif n == 3:
            return 12
        else:
            if n % 2 == 0:
                return 4 * 5 ** ((n - 2) / 2)
            else:
                return 12 * 5 ** ((n - 3) / 2)

    def findSmaller(self, num):
        firstDigit= {'0':0, '1':0, '2':1, '3':1, '4':1, '5':1, '6':1, '7':2, '8':2, '9':3}          #Use a dict to store how many strobogrammatic digits are below the first digit of num.
        middleDigit = {'0':0, '1':1, '2':2, '3':2, '4':2, '5':2, '6':2, '7':2, '8':2, '9':3}        #Use a dict to store how many strobogrammatic digits are below the middle digit of num.
        otherDigits = {'0':0, '1':1, '2':2, '3':2, '4':2, '5':2, '6':2, '7':3, '8':3, '9':4}        #Use a dict to store how many strobogrammatic digits are below the current digit of num(except for the first digit and middle digit).
        dict = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}                                        #Store valid strobogrammatic relations.
        secondHalf = ""                                                                             #Store the strobogrammatic mapped string of the first half of num.
        factor = [1, 3]                                                                             #Because there are 3 valid strobogrammatic digits if the length of num is odd, the factor is 3. Otherwise, the factor is 1.
        total = 0                                                                                   #Count strobogrammatic numbers which have the same length with low but are smaller than num.
        i = 0
        flag = True                                                                                 #Indicates that all the digits from the first to current are strobogrammatic. 
        while i < len(num) / 2:
            if i == 0:                                                                              #Check the first digit, add the count of strobogrammatic numbers which are below to num at the first digit.
                total += factor[len(num) % 2] * firstDigit[num[i]] * 5 ** (len(num) / 2 - i - 1)
                if num[i] not in ['1','6','8','9']:                                                 #If the first digit is not strobogrammatic, set flag to false and break.
                    flag = False
                    break
            else:                                                                                   #Check current digit, add the count of strobogrammatic numbers which are below to num at current digit.
                total += factor[len(num) % 2] * otherDigits[num[i]] * 5 ** (len(num) / 2 - i - 1)
                if num[i] not in ['0','1','6','8','9']:                                             #If current digit is not strobogrammatic, set flag to false and break.
                    flag = False
                    break
            secondHalf += dict[num[i]]                                                              #Append the stobogrammatic mapped digit to secondHalf.
            i += 1
        if len(num) % 2 == 1 and i == len(num) / 2:                                                 #If the length of num is odd, check the middle digit, add the count of strobogrammatic numbers which are below to num at current digit.
            total += middleDigit[num[i]]
            if num[i] not in ['0', '1', '8']:                                                       #If the middle digit is not strobogrammatic, set flag to false and break.
                flag = False
        secondHalf = secondHalf[::-1]                                                               #Reverse secondHalf.
        if len(num) > 1 and flag and int(num[- (len(num) / 2):]) > int(secondHalf):                 #If length is greater than 1 and all the digits checked are strobogrammatic digits, compare the value of second part of num and the value of secondHalf.
            total += 1                                                                              #If secondHalf is smaller, the strobogrammatic number whose first half is the same as that of num is smaller than num.
        return total
    
    def strobogrammaticCheck(self, num):                                                          #Check if num is strobogrammatic(The same with Strobogrammatic Number I).
        dict = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
        for i in range(len(num) / 2):
            if num[i] not in dict or num[-(i + 1)] not in dict or num[-(i + 1)] != dict[num[i]]:
                return False
        if len(num) % 2 == 1 and num[len(num) / 2] != '0' and num[len(num) / 2] != '1' and num[len(num) / 2] != '8':
            return False
        return True
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        if len(low) > len(high):
            return 0
        sum = 0
        for i in range(len(low), len(high)):                                                      #Find the sum of strobogrammatic number from length of low to length of high minus 1.
            sum += self.strobogrammaticOfLength(i)
        sum -= self.findSmaller(low)                                                              #Subtract the count of strobogrammatic numbers which have the same length with low but are smaller than low.
        sum += self.findSmaller(high)                                                             #Plus the count of strobogrammatic numbers which have the same length with high but are smaller than high.
        if self.strobogrammaticCheck(high) is True:                                               #If high is strobogrammatic, include it into sum.
            sum += 1
        return sum

class Solution(object):
    def check(self, first, second, num):                                    #Given the previous 2 number, determine if the following sequence is valid.
        l = len(num)
        if l == 0:                                                          #If reach the end, thus we find a valid additive number sequence, return true.
            return True
        sum = first + second                                                #Calculate the sum.
        if num[0] == '0':                                                   #If the first digit is '0', new number must be 0.
            if sum != 0:                                                    #If sum is not 0, return false.
                return False
            else:
                return self.check(second, sum, num[1:])                     #Otherwise, check the following sequence recursively.
        else:
            index = 1
            while index <= l:                                               #Enum every number beginning with the first digit until it's larger than or equal to sum.
                t = int(num[:index])
                if t < sum:
                    index += 1
                elif t == sum:                                              #If it's equal to sum, it's the next valid additive number, check the following sequence recursively.
                    return self.check(second, sum, num[index:])
                else:                                                       #If it's larger than sum, we can't find the next valid additive number, so return false.
                    return False
        return False                                                        #If all the number are smaller than sum, return false.
        
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        l = len(num)
        if l < 3:                                                           #If the length is smaller than 3, there can't be 3 valid number, so return false.
            return False
        flag = False
        if num[0] == '0':                                                   #If the first digit is '0', the first number is 0.
            first = 0
            if num[1] == '0':                                               #If the second digit is '0', the second number is 0.
                second = 0
                flag = flag or self.check(first, second, num[2:])           #Check the following sequence.
            else:
                for j in range(2, (l + 1) / 2):                             #Enum all the possible second number.
                    second = int(num[1:j])
                    flag = flag or self.check(first, second, num[j:])       #Check the following sequence.
                    if flag == True:
                        break
        else:
            for i in range(1, l / 2 + 1):                                   #Enum all the possible first number. 
                first = int(num[:i])
                if num[i] == '0':                                           #If next digit is '0', the second number is 0.
                    second = 0
                    flag = flag or self.check(first, second, num[i + 1:])   #Check the following sequence.
                else:
                    for j in range(i + 1, i + (l - i) / 2 + 1):             #Enum all the possible second number.
                        second = int(num[i:j])
                        flag = flag or self.check(first, second, num[j:])   #Check the following sequence.
                        if flag == True:
                            break
                if flag == True:
                    break
        return flag

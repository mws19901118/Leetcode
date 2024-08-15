class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5, count_10 = 0, 0                        #Count 5 dollar bill and 10 dollar bill.
        for x in bills:                                 #Traverse bills.
            if x == 5:                                  #Scenario x == 5: increase count_5.
                count_5 += 1
            elif x == 10:                               #Scenario x == 10: if count_5 is 0, return false; otherwise, decrease count_5 and increase count_10.
                if not count_5:
                    return False
                count_5 -= 1
                count_10 += 1
            elif x == 20:                               #Scenario x == 20:
                if count_10 and count_5:                #If both count_10 and count_5 is not 0, decrease count_10 and count_5.
                    count_10 -= 1
                    count_5 -= 1
                elif count_5 >= 3:                      #If count_5 is greater than or equal to 3, decrease count_5 by 3.
                    count_5 -= 3
                else:                                   #Otherwise, return false.
                    return False
        return True                                     #Return true at the end.

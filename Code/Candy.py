class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings)                                                  #Initially, give one candy to each child.
        for i in range(1, len(ratings)):                                            #Traverse forward.
            if ratings[i] > ratings[i - 1]:                                         #If current child has a higher rating than previous child, give current child one more candy than previous child.
                candy[i] = candy[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):                                   #Traverse backward.
            if ratings[i] > ratings[i + 1] and candy[i] <= candy[i + 1]:            #If current child has a higher rating than next child but does not have more candies, give current child one more candy than next child.
                candy[i] = candy[i + 1] + 1
        return sum(candy)                                                           #Return sum of candy.

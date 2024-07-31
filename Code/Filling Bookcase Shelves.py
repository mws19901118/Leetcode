class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache                                                                                      #Cache result.
        def dp(index: int) -> int:                                                                  #Calculate the min height of filling bookcase for books[index:].
            if index >= len(books):                                                                 #If index reaches the end, return 0.
                return 0
            totalHeight, currentHeight, remainWidth = inf, 0, shelfWidth                            #Initialize total height, current height and remain width.
            while index < len(books) and remainWidth - books[index][0] >= 0:                        #Move index forward while we can still fill book on current level.
                currentHeight = max(currentHeight, books[index][1])                                 #Update the max height of current level.
                totalHeight = min(totalHeight, currentHeight + dp(index + 1))                       #The total height is the currentHeight + dp(index + 1) and update totalHeight.
                remainWidth -= books[index][0]                                                      #Update remainWidth.
                index += 1
            return totalHeight                                                                      #Return totalHeight.

        return dp(0)                                                                                #Return dp(0).

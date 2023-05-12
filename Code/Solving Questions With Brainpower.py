class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache                                                                                                #Cache result.
        def dp(index: int) -> int:                                                                            #Return the max score of questions[index:].
            if index >= len(questions):                                                                       #If index >= len(questions), return 0.
                return 0
            return max(dp(index + 1), questions[index][0] + dp(index + 1 + questions[index][1]))              #Return the max of dp(index + 1)(skipping current question) and questions[index][0] + dp(index + 1 + questions[index][1])(solving current question).

        return dp(0)                                                                                          #Return dp(0).

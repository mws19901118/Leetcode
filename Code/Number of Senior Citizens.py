class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(int(x[11:13]) > 60) for x in details)    #Count passenger older than 60.

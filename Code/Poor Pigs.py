class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(math.log(buckets) / math.log(minutesToTest // minutesToDie + 1))  #Each pig can take T tests and have (T + 1) states. So, calculate minimum x such that (T+1) ^ x >= buckets. T = minutesToTest // minutesToDie

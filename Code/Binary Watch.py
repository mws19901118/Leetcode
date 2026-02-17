class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return [str(i) + ":" + str(j).zfill(2) for i, j in product(range(12), range(60)) if i.bit_count() + j.bit_count() == turnedOn]      #Return all minutes from 00:00 to 11:59 total 1 bits equals turnedOn.

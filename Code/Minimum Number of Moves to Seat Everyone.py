class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(x - y) for x, y in zip(sorted(seats), sorted(students)))        #Sort both seats and students and sum up the abs of corresponding sort and student.

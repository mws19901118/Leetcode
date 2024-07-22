class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = sorted((-h, n) for n, h in zip(names, heights))          #Sort by heigh in descending order then return the names.
        return [n for h, n in people]

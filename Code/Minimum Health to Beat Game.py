class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return sum(damage) - min(armor, max(damage)) + 1      #Sum up the damage and minus the min of armor and max damage then plus 1.

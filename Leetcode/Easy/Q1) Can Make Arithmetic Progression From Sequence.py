class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        seq = sorted(arr)
        diff = seq[1] - seq[0]
        for i in range(2, len(arr)):
            if seq[i] - seq[i-1] != diff:
                return False
        return True
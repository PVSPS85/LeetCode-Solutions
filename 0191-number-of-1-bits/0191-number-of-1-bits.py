class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for ch in bin(n):
            if ch == '1':
                count += 1
        return count     
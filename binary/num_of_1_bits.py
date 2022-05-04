# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        numOfBits = 0
        mask = 1
        for _ in range(32):
            if n & mask:
                numOfBits += 1
            mask = mask << 1
        return numOfBits

"""
num = 7

mask of 1
7 & 1 == 1
mask << 1 == 2
mask of 2
mask << 1 == 4
mask of 4
we do this 32 times :)
"""
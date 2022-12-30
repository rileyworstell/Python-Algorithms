# https://leetcode.com/problems/counting-bits/

class Solution:
    # O(n) time O(1) space
    """
    Last set bit is the rightmost set bit. setting that bit to zero with x &= x - 1
    dp ans[i] = ans[i & (i - 1)] + 1
    """
    def countBits(self, n: int):
        ans = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            ans[i] = ans[i & (i - 1)] + 1
        return ans


x = Solution()
print(x.countBits(10)) # [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
        
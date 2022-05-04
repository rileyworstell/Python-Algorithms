# https://leetcode.com/problems/unique-paths/
class Solution:
    # Time O(mn)
    # Space O(mn)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[0][1] = 1
        for r in range(1, m+1):
            for c in range(1, n+1):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]
                



x = Solution()
print(x.uniquePaths(3, 7))
# 28

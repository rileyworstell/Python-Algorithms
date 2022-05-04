# https://leetcode.com/problems/longest-common-subsequence/submissions/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [['' for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        for r in range(1, len(dp)):
            for c in range(1, len(dp[0])):
                helper = ""
                if text1[c-1] == text2[r-1] and len(dp[r-1][c]) <= len(dp[r][c-1]):
                    helper = text1[c-1]
                    dp[r][c] = dp[r-1][c-1] + helper
                elif len(dp[r-1][c]) > len(dp[r][c-1]):
                    dp[r][c] = dp[r-1][c] + helper
                else:
                    dp[r][c] = dp[r][c-1] + helper
        return len(dp[-1][-1])
                
        
x = Solution()
t1="abcba"
t2="abcbcba"
print(x.longestCommonSubsequence(t1, t2))
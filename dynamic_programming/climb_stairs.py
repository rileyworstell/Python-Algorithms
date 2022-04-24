# https://leetcode.com/problems/climbing-stairs/
class Solution:
    # top - down - memoization
    def climbStairs(self, n, memo={}):
        if n <= 1:
            return 1
        memo[n] =  self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
        return memo[n]


    # # bottom up - tabulation
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     first = 1
    #     second = 0
    #     cur = 0
    #     for i in range(0, n):
    #         if i + 1 <= n:
    #             second += first
    #         if i + 2 <= n:
    #             cur += first
    #         temp = cur
    #         cur = 0
    #         first = second
    #         second = temp
    #     return first



n = 3
x = Solution()
print(x.climbStairs(n))
"""
    2 
  1    0
"""
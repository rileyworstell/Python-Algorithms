# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums):
        # loop through and treat each number as the largest number
        # then go through all the numbers before it and if the right number is greater set the value to
        # the max of itself or the value at the number before it + 1
        # O(n^2) time
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

            


x = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(x.lengthOfLIS(nums))# [2, 3, 7, 101] 4

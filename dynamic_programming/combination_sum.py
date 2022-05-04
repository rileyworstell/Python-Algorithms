# https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        global count
        count = 0
        self.helper(nums, target, 0)
        return count

    
    def helper(self, nums, target, cur, memo={}, counter=0):
        global count
        if cur in memo:
            return memo[cur]
        if cur == target:
            return 1 + counter
        if cur > target:
            return counter
        
        
        for i in range(len(nums)):
            memo[cur] = max(self.helper(nums[i:], target, cur + nums[i], memo, counter), memo.get(cur, 0))
            counter = memo[cur]
            count += memo[cur]
        
        return counter




nums = [1, 2, 3]
target = 7
x = Solution()
print(x.combinationSum4(nums, target))

        
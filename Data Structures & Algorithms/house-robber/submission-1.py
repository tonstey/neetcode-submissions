class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * n

        if n >= 1:
            memo[0] = nums[0]
        if n >= 2:
            memo[1] = max(nums[0], nums[1])

        for i in range(2, n):
            memo[i] = max(memo[i-1], nums[i] + memo[i-2])

        print(memo)
        return memo[n - 1]
        
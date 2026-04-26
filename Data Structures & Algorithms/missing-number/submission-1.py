class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        comp = 0

        for i in range(0, len(nums) + 1):
            comp = comp ^ i
        for i in nums:
            comp = comp ^ i

        return comp
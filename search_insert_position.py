class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        total = 1
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
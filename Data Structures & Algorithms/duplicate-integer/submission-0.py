class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        index = 0

        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                return True
            else:
                index += 1

        return False
        
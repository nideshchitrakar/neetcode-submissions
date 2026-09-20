class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for index_i, i in enumerate(nums):
            j = target - i
            if j in index_map:
                return [index_map[j], index_i]
            if i not in index_map:
                index_map[i] = index_i

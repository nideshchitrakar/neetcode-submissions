class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products, suffix_products = [1] * len(nums), [0] * len(nums)
        res = [1] * len(nums)
        i, j = 0, len(nums) - 1

        while i < len(nums):
            if i == 0:
                prefix_products[i] = nums[i]
            else:
                prefix_products[i] = nums[i] * prefix_products[ i - 1 ]
            i += 1

        while j >= 0:
            if j == len(nums) - 1:
                suffix_products[j] = nums[j]
            else:
                suffix_products[j] = nums[j] * suffix_products[ j + 1 ]
            j -= 1

        for i in range(len(nums)):
            res[i] = (prefix_products[i - 1] if i > 0 else 1) * (suffix_products[i + 1] if i < len(nums) - 1 else 1)

        return res

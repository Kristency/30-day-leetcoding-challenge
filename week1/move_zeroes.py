# https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_start = None
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                if zero_start is None:
                    zero_start = i
            else:
                if zero_start is not None:
                    nums[i], nums[zero_start] = nums[zero_start], nums[i]
                    zero_start += 1

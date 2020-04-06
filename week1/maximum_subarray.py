# https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = global_max = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])
            if cur_max > global_max:
                global_max = cur_max

        return global_max

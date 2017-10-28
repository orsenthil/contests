"""
https://leetcode.com/problems/3sum/description/
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx - 1] == nums[idx]:  # same numbers, answer should have unique triplets
                continue

            second_idx, third_idx = idx + 1, len(nums) - 1
            while second_idx < third_idx:
                s = nums[idx] + nums[second_idx] + nums[third_idx]
                if s < 0:
                    second_idx += 1
                elif s > 0:
                    third_idx -= 1
                else:
                    results.append((nums[idx], nums[second_idx], nums[third_idx]))
                    while second_idx < third_idx and nums[second_idx + 1] == nums[second_idx]:
                        second_idx += 1
                    while second_idx < third_idx and nums[third_idx] == nums[third_idx - 1]:
                        third_idx -= 1

                    second_idx += 1
                    third_idx -= 1

        return results



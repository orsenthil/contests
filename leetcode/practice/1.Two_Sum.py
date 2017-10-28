"""
https://leetcode.com/problems/two-sum/description/
"""


class Solution:

    def find(self, arr, value):
        try:
            return arr.index(value)
        except ValueError:
            return None

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx in range(len(nums)):
            n1 = nums[idx]
            nums[idx] = 'x'
            s_idx = self.find(nums, target-n1)
            if s_idx is not None:
                return [idx, s_idx]


if __name__ == '__main__':
    s = Solution()
    assert [0, 1] == s.twoSum([2, 7, 11, 15], 9)
    print(s.twoSum([2, 7, 11, 15], 9))
    assert [1, 2] == s.twoSum([3,2,4], 6)
    print(s.twoSum([3,2,4], 6))


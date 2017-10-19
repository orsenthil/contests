import collections

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _counter = collections.Counter(nums)
        _max_frequency = max(_counter.values())
        _most_common = []
        for key, value in _counter.iteritems():
            if value == _max_frequency:
                _most_common.append(key)
        
        _smallest = len(nums) + 1

        for key in _most_common:
            left_index = nums.index(key)
            right_index = len(nums) - nums[::-1].index(key)
            _diff = (right_index - left_index)
            if _diff < _smallest:
                _smallest = _diff

        return _smallest


if __name__ == '__main__':
    s = Solution()
    assert s.findShortestSubArray([1,2,2,3,1,4,2]) == 6
    assert s.findShortestSubArray([1, 2, 2, 3, 1]) == 2
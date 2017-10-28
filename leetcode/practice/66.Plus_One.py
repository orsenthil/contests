"""
Plus One: https://leetcode.com/problems/plus-one/description/
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits:  List[int]
        :rtype List[int]
        """
        result = [0] + digits
        last_pos = len(result) - 1
        for last_digit in reversed(result):
            if last_pos == (len(result) - 1):
                result[last_pos] += 1
            result[last_pos-1] += result[last_pos] // 10
            result[last_pos] %= 10
            last_pos -= 1
        pt = 0
        for i in range(len(result)):
            if result[i] == 0:
                pt += 1
            else:
                break
        result = result[pt:]
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([9, 9]))

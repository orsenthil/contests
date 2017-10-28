"""
Description: https://leetcode.com/problems/add-binary/description/

"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # base case
        if len(a) == 0: return b
        if len(b) == 0: return a
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        if a[-1] == '1' and b[-1] == '1': # 1 1 = 10
            carry = '1'
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), carry) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'

if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("", "111")) # 111
    print(s.addBinary("101", "")) # 101
    print(s.addBinary("11", "1")) # 100



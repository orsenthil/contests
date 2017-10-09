class Solution:
    def toggle(self, expect):
        if expect == '1':
            return '0'
        return '1'

    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary_repr = bin(n)[2:]
        if len(binary_repr) == 1:
            return True
        first = binary_repr[0]
        expect = self.toggle(first)

        for c in binary_repr[1:]:
            if c != expect:
                return False
            expect = self.toggle(expect)
        return True


s = Solution()
print(s.hasAlternatingBits(5))
print(s.hasAlternatingBits(7))
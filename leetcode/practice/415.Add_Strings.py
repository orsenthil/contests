class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        added = [0] * (max(len(num1), len(num2)) + 1)
        pos = len(added) - 1
        num1_reversed = num1[::-1]
        num2_reversed = num2[::-1]
        index = 0
        result = 0

        while pos:
            if index < len(num1) and index < len(num2):
                n1 = num1_reversed[index]
                n2 = num2_reversed[index]
                result = int(n1) + int(n2)
            elif index < len(num1):
                n1 = num1_reversed[index]
                result = int(n1)
            elif index < len(num2):
                n2 = num2_reversed[index]
                result = int(n2)

            added[pos] += result
            added[pos-1] += added[pos] // 10
            added[pos] %= 10

            pos -= 1
            index += 1
            result = 0

        pt = 0
        while pt < len(added) - 1 and added[pt] == 0:
            pt += 1

        return ''.join(map(str, added[pt:]))

if __name__ == '__main__':
    s = Solution()
    assert s.addStrings("89", "99") == str(89 + 99)
    assert s.addStrings("9", "99") == str(9 + 99)
    assert s.addStrings("9", "999999") == str(9 + 999999)
    print(s.addStrings("89", "99"))

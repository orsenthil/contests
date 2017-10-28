"""
https://leetcode.com/problems/add-two-numbers/description/

"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list = []
        l2_list = []

        while l1.next is not None:
            l1_list.append(str(l1.val))
            l1 = l1.next
        else:
            l1_list.append(str(l1.val))

        while l2.next is not None:
            l2_list.append(str(l2.val))
            l2 = l2.next
        else:
            l2_list.append(str(l2.val))

        n1 = int("".join(reversed(l1_list)))
        n2 = int("".join(reversed(l2_list)))

        r = n1 + n2
        result = list(str(r))[::-1]
        list_of_nodes = []

        for r in result:
            list_of_nodes.append(ListNode(r))

        _len = len(list_of_nodes)

        for i in range(1, _len):
            list_of_nodes[i-1].next = list_of_nodes[i]

        return list_of_nodes[0]


if __name__ == '__main__':
    l1_2 = ListNode(2)
    l1_4 = ListNode(4)
    l1_3 = ListNode(3)
    l1_2.next = l1_4
    l1_4.next = l1_3

    l2_5 = ListNode(5)
    l2_6 = ListNode(6)
    l2_4 = ListNode(4)
    l2_5.next = l2_6
    l2_6.next = l2_4

    s = Solution()
    s.addTwoNumbers(l1_2, l2_5)


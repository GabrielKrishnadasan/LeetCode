#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = {"(": ")", "{": "}", "[": "]"}

        if len(s) % 2 == 1:
            return False

        stack = []

        for item in s:
            if item in m.keys():
                stack.append(item)
            else:
                if len(stack) == 0 or m[stack.pop()] != item:
                    return False

        if len(stack) == 0:
            return True
        return False
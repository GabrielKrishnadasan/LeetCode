#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []

        for item in s:
            if item.isalnum():
                lst.append(item.lower)


        f = 0
        b = len(lst) - 1

        while f < b:
            if lst[f] != lst[b]:
                return False
            f += 1
            b -= 1

        return True
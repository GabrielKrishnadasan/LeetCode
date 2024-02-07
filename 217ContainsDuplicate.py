#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums) -> bool:
        s = set()

        for item in nums:
            if item in s:
                return True
            else:
                s.add(item)

        return False
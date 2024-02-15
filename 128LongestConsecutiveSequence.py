#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

#You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = 1
        if len(nums) == 0:
            return 0

        s = set(nums)

        for item in nums:
            temp = item
            if temp - 1 not in s:
                ret = 1
                while temp + 1 in s:
                    ret += 1
                    temp += 1
                m = max(m, ret)
        return m
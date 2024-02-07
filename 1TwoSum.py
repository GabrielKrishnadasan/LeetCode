#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for item in nums:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
        
        for i in range(len(nums)):
            if target - nums[i] in dic:
                if target - nums[i] != nums[i]:
                    return [i, nums.index(target - nums[i])]
                else:
                    if dic[nums[i]] == 2:
                        for j in range(i + 1, len(nums)):
                            if nums[j] == nums[i]:
                                return [i, j]
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ret = []

        for i in range(len(nums)):
            target = -nums[i]

            if i > 0 and nums[i-1] == nums[i]:
                continue

            f = i + 1
            b = len(nums) - 1

            while f < b:
                if nums[f] + nums[b] < target:
                    f += 1
                elif nums[f] + nums[b] > target:
                    b -= 1
                else:
                    ret.append([nums[i], nums[f], nums[b]])
                    f += 1
                    b -= 1
                    while nums[f] == nums[f - 1] and f < b:
                        f += 1
        return ret
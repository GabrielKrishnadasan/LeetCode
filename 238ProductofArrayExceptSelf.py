#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCount = 0
        for item in nums:
            if item != 0:
                product *= item
            else:
                zeroCount += 1

        ret = []

        if zeroCount > 1:
            return [0] * len(nums)
        elif zeroCount == 1:
            for item in nums:
                if item == 0:
                    ret.append(product)
                else:
                    ret.append(0)
        else:
            for item in nums:
                ret.append(int(product/item))

        return ret
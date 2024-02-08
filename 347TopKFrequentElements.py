#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()

        index = 0
        countLst = []
        countLst.append([nums[0], 1])
        for i in range(1, len(nums)):
            if nums[i] == countLst[index][0]:
                countLst[index][1] += 1
            else:
                countLst.append([nums[i], 1])
                index += 1

        sorted_list = sorted(countLst, key=lambda x:x[1], reverse=True)

        ret = []
        for i in range(k):
            ret.append(sorted_list[i][0])

        return ret
#Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}

        anaDict[''.join(sorted(strs[0]))] = 0
        lst = [[strs[0]]]

        for i in range(1, len(strs)):
            temp = ''.join(sorted(strs[i]))
            if temp in anaDict:
                lst[anaDict[temp]].append(strs[i])
            else:
                anaDict[temp] = len(lst)
                lst.append([strs[i]])

        return lst
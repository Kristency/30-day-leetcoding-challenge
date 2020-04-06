# https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_ = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in map_:
                map_[sorted_word].append(word)
            else:
                map_[sorted_word] = [word]

        return map_.values()

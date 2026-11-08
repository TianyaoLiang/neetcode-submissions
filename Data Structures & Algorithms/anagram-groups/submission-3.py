class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted not in word_dict:
                word_dict[s_sorted] = []
            word_dict[s_sorted].append(s)
        return list(word_dict.values())
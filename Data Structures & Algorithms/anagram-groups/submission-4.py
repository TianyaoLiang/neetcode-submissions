class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {} # sorted word : word
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted not in dict:
                dict[s_sorted] = []
            dict[s_sorted].append(s)
        return list(dict.values())
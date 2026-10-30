class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in ana_dict:
                ana_dict[sorted_word] = []  # Initialize the list if it's not there
            ana_dict[sorted_word].append(word)
            
        return list(ana_dict.values())
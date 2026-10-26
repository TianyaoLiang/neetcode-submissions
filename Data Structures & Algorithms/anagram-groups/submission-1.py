class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {} #sorted word : word
        results = []

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in ana:
                ana[sorted_word] = []
            ana[sorted_word].append(word)
        
        for values in ana.values():
            results.append(list(values))
            
        return results
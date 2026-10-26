class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # num : count
        freq = [[] for i in range(len(nums)+1)]

        results = []

        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                results.append(num)
            
            if len(results) == k:
                break

        return results
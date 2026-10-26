class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # num : count
        results = []

        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        for i in range(k):
            highest_count_key = (max(count, key=count.get))
            results.append(highest_count_key)
            count.pop(highest_count_key)
        return results
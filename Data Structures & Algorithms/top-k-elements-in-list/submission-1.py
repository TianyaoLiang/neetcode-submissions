class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        for i in range(k):
            result.append(max(count, key=count.get))
            count[max(count, key=count.get)] = 0

        return result
        
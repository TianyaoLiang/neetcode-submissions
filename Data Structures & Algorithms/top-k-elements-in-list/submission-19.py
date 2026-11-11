class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_n = {}

        for n in nums:
            count_n[n] = count_n.get(n, 0) + 1

        sorted_count = sorted(
            count_n.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return [key for key, value in sorted_count[:k]]
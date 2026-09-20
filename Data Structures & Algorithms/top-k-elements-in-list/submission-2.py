class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        sorted_counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}

        return list(sorted_counts.keys())[0:k]
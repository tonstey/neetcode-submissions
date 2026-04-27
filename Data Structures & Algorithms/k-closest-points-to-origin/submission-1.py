import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Find min k points -> Use max heap
        heap = []

        for i in points:
            dist = i[0] **2 + i[1] ** 2
            heapq.heappush(heap, (-1*dist, i))
            if len(heap) > k:
                heapq.heappop(heap)

        return [a[1] for a in heap]
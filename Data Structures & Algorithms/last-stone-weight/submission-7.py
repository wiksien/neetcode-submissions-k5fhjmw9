import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            print(stones)
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            print(-x, -y)

            if -x > -y:
                heapq.heappush(stones, -y + x)
        
        if len(stones) == 1:
            return abs(stones[0])
        else:
            return 0
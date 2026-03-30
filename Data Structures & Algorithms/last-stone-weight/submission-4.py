import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        heapq.heapify(stones)
        print(stones)

        while len(stones) > 1:
            stone_1 = stones[0]

            if len(stones) > 2:
                stone_2 = min(stones[1], stones[2])
            else:
                stone_2 = stones[1]

            if stone_1 == stone_2:
                stones.pop(0)
                stones.pop(stones.index(stone_2))
            elif -stone_1 > -stone_2:
                destroyed_stone = stones.pop(stones.index(stone_2))
                stones[0] -= destroyed_stone
            
            heapq.heapify(stones)
            print(stones)
        
        if len(stones) == 0:
            return 0
        else:
            return abs(stones[0])
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_in_pile = max(piles)

        l = 1
        u = max_in_pile
    
        k = u

        while l < u:
            mid = l + u // 2
            total_time = 0

            for i in range(len(piles)):
                total_time += math.ceil(piles[i] / k)

            if total_time <= h:
                k = min(k , mid)
                u = mid - 1
            else:
                l = mid + 1

        return k






            
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_in_pile = 0

        for i in range(len(piles)):
            if piles[i] > max_in_pile:
                max_in_pile = piles[i]
        
        l = 1
        r = max_in_pile
        
        result = r

        while l <= r:
            k = (l + r) // 2
            hours = 0

            for i in piles:
                hours += math.ceil(i/k)

            if hours <= h:
                r = k - 1
                result = min(result, k)
            else:
                l = k + 1

        return result


            
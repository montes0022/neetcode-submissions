class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = 0

        for i in range(len(piles)):
            total += piles[i]

        print(f'total bananas after loop: {total}')

        return total    
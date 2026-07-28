class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = 0
        max_in_pile = 0

        for i in range(len(piles)):
            if piles[i] > max_in_pile:
                max_in_pile = piles[i]
            total += piles[i]
        
        print(f'total bananas: {total}')
        print(f'most bananas in a pile: {max_in_pile}')
        print(f'range of answers k is in is from 1 to {max_in_pile}')
        l = 1
        r = max_in_pile
        #result should be at least the max bananas in our pile.
        result = r

        while l <= r:
            #k is the rate we choose to start with in our range of answers 1-max
            k = (l + r) // 2
            hours = 0 #our counter that we will return

            #divide each number in piles with computed k and add to hours
            for p in piles:
                hours += math.ceil(p/k)

            #if total hours is less than or equal to k
            #update result to a new minimum
            #so either what it was saved as before or the new k value we checked for.
            if hours <= h:
                result = min(res, k)
                r = k - 1 #look for a smaller k, left portion
            else:
                #look for a bigger k, right portion, means the right was too small
                l = k + 1

        return res




        return total    
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = []

        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        pairs_sorted = sorted(pairs)

        for i in range(len(pairs_sorted)-1, -1, -1):

            if stack:
                newT = (target - pairs_sorted[i][0]) / pairs_sorted[i][1]
                topT = (target - stack[-1][0]) / stack[-1][1]

                if newT > topT:
                    stack.append(pairs_sorted)
            else:
                stack.append(pairs_sorted[i])

        return len(stack)
        
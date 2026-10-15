class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        pairs = []

        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        pairs_sorted = sorted(pairs)

        for i in range(len(pairs_sorted)-1, -1, -1):

            stack.append(pairs_sorted[i])
            
            if stack and len(stack) > 1:
                new = stack.pop()
                top = stack.pop()

                newT = (target - new[0]) / new[1]
                topT = (target - top[0]) / top[1]

                if newT <= topT:
                    stack.append(top)
                else:
                    stack.append(top)
                    stack.append(new)

        return len(stack)


        
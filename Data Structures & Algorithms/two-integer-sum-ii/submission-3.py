class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) -1

        #essentially set up like a binary search, especially since
        #numbers is sorted.
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]

            if numbers[start] + numbers[end] > target:
                #nums at end must be excluded because the biggest number
                #cant be apart of the solution if its sum with smallest
                #number exceed target.
                end -= 1

            #nums at start must be excluded because the smallest number
            #cant be apart of the solution if its sum with the other number
            #at end was smaller than target.
            else:
                start += 1

            
        
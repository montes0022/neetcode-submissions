class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) -1

        while start <= end:
            if nums[start] + nums[end] == target:
                return [start+1, end+1]

            if nums[start] + nums[end] > target:
                #nums at end must be excluded because the biggest number
                #cant be apart of the solution if its sum with smallest
                #number exceed target.
                end -= 1

            if nums[start] + nums[end] < target:
                start += 1

            
        
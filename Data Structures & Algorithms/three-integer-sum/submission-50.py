class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if nums[i] == nums[i-1]:
                continue
            
            s = i + 1
            e = len(nums) - 1

            while s < e:
                threesum = nums[i] + nums[s] + nums[e]

                if threesum > 0:
                    e -= 1
                elif threesum < 0:
                    s += 1
                else:
                    e -= 1
                    s += 1
                    output.append([nums[i],nums[s],nums[e]])

                    while nums[s] == nums[s-1] and s < e:
                        s +=1

        return output




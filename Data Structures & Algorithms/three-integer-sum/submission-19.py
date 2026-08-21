class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        #sort nums
        nums.sort()
        for i in range(len(nums)):
            s = i +1
            e = len(nums) -1

            while s <= e:
                if nums[i] + nums[s] + nums[e] == 0:
                    output.append([nums[i], nums[s], nums[e]])
                    break

                elif nums[i] + nums[s] + nums[e] < 0:
                    s += 1
                else:
                    e -= 1


        
        return output




        
        
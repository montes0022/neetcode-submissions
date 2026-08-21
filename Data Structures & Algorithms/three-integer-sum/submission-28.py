class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        #sort nums
        nums.sort()
        for i in range(len(nums)):
            s = i +1
            e = len(nums) -1

            target = -(nums[i])
            #s cannot be e without duplicates.
            while s <= e:
                if nums[e] + nums[s] == target:
                    output.append([nums[i], nums[s], nums[e]])
                    s+=1
                    e+=1

                if nums[s] + nums[s] < target:
                    s += 1
                else:
                    e -=1



        
        return output




        
        
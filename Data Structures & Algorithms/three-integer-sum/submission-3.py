class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        #sort nums
        nums.sort()
        for i in range(len(nums)):
            s = i +1
            e = len(nums) -1

            while s <= e:
                if nums[i] + nums[s] + nums[e] == 0 and (nums[i] != nums[s] != nums[e]):
                    output.append([nums[i], nums[start], nums[end]])

                if nums[i] + nums[s] + nums[e] < 0:
                    s += 1

                #nums at start must be exclused because the smallest number
                #cant be apart of the solution if its sum with the other number
                #at end was smaller than target.
                else:
                    e -= 1


        
        return output




        
        
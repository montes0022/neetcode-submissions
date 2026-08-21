class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        #sort nums
        nums.sort()
        for i in range(len(nums)):
            s = i +1#had this done
            e = len(nums) -1#had this done

            #check if i is bigger than 0 in case of out of bounds error
            #if nums[i] is the same as nums[i-1], that means
            #we already solved all combinations that start with i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while s < e:
                tsum = nums[e] + nums[s] + nums[i]
                if tsum == 0:
                    output.append([nums[i], nums[s], nums[e]])#had this done
                    s += 1#had this done
                    e -= 1#had this done
                if nums[s] + nums[e] < 0:
                    s += 1
                else:
                    e -=1

        return output
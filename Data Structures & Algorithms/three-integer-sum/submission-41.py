class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        #sort nums
        nums.sort()
        for i in range(len(nums)):
            s = i +1#had this done
            e = len(nums) -1#had this done

            if nums[i] == nums[i-1] and i > 0:
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
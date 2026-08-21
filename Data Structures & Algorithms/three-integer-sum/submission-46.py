class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        #sort nums
        nums.sort()
        for i in range(len(nums)):
   
            #in the event we have a number bigger than 0 at i
            #then our solution is invalid because all numbers after i are
            #larger in our sorted nums.
            if nums[i] > 0:
                break
            #check if i is bigger than 0 in case of out of bounds error
            #if nums[i] is the same as nums[i-1], that means
            #we already solved all combinations that start with i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            #had these done before checks above. needed to move below.
            s = i +1#had this done
            e = len(nums) -1#had this done
            while s < e:
                tsum = nums[e] + nums[s] + nums[i]
                if nums[s] + nums[e] < 0:
                    s += 1
                elif nums[s] + nums[e] > 0:
                    e -= 1
                else:
                    output.append([nums[i], nums[s], nums[e]])#had this done
                    s += 1#had this done
                    e -= 1#had this done
                    #while s is still less than e, check if the value you moved
                    #s to is equal to the value at s-1 to avoid duplicates. 
                    while nums[s] == nums[s - 1] and s < e:
                        s += 1
        return output
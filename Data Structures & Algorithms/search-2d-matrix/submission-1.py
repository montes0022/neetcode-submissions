class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in matrix:
            cur = matrix[i]
    
            left = 0
            right = len(cur)-1
    
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid -1
                
        return False
        
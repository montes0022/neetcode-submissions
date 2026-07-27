class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            cur = matrix[i]

            left = 0
            right = len(cur)-1

            while left <= right:
                mid = left + (right - left) // 2
                if cur[mid] == target:
                    return True
                if cur[mid] < target:
                    left = mid + 1
                elif cur[mid] > target:
                    right = mid -1

        return False
        
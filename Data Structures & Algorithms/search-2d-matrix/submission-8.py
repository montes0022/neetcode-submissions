class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        while left <= right:
            mid = left + (right - left) // 2
            #if matrix[mid] == target:
            #    return True
            if left ==mid== right:
                self.try_bst(matrix[mid])
            if matrix[mid][-1] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid -1




    def try_bst(self, curr):
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
        
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2

        total = len(nums1) + len(nums2)
        #half is roughly the number of elements in the left partition.
        half = total // 2

        #if a is ever bigger than b, swap them.
        if len(b) < len(a):
            a,b = b,a

        l = 0
        r = len(a) - 1

        #bst, normally l<=r but our edge case is finding the median which
        #will break us out of the loop.
        while True:
            m = (l+r) // 2 #a's left partition last position

            x = half - m - 2 #b's left partition element count, subtract 2 because of indexing

            #if either A or B are empty or size 1, we can get an out of bounds error
            #set default values to negative infinity if m or x are <= 0

            #if either m+1 or x+1 are out of bounds we want all the values in their
            #respective arrays to be apart of those partitions, left or right
            #leftmost item in a's left partition
            Aleft = a[m] if m >=0 else float("-infinity")
            #rightmost item in a's right partition
            Aright = a[m+1] if (m+1) < len(a) else float("infinity")

            #leftmost item in b's left partition
            Bleft = b[x] if x >=0 else float("-infinity")
            #rightmost item in b's right partition
            Bright = b[x+1] if (x+1) < len(b) else float("infinity")

            #this means left partition of merged array is valid.
            if Aleft <= Bright and Bleft <= Aright:
                #depending on if total was even or odd...
                #odd, get the min of Aright and Bright
                #even, max(Aleft,Bleft) + min(Aright, Bright) / 2
                if total % 2 == 0:
                    return max(Aleft,Bleft) + min(Aright, Bright) / 2
                else:
                    return min(Aright, Bright)
            else: #we need to move up the left partition in A by one to see
            #if getting the new left partition of B makes a valid combined left 
            #partition from both arrays
                l = m +1




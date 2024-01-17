class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        output = 0
        sum = nums1 + nums2
        sum.sort()
        divide = int(len(sum) / 2)
        remain = len(sum) % 2
        if remain == 1 : 
            median2 = sum[divide]
            sum_median = round(median2, 4)
        else :
            median1 = sum[divide - 1]
            median2 = sum[divide]
            sum_median = round((median1 + median2) / 2, 4)
        print(divide)
        print(remain)
        
        
        return sum_median
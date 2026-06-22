#Insertion sort time:O(n^2) space: O(1)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        flag=True
        for i in range(1,n):
            j=i
            while j>0:
                if nums[j-1]>nums[j]:
                    nums[j-1],nums[j]=nums[j],nums[j-1]
                j-=1
        return nums

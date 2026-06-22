#bubblesort time:O(n^2) space: O(1)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        flag=True
        while flag:
            flag=False
            for i in range(1,n):
                if nums[i-1]>nums[i]:
                    flag=True
                    nums[i-1],nums[i]=nums[i],nums[i-1]
        return nums
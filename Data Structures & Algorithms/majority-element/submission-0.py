class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority={}
        n=len(nums)
        half=n/2
        for i,num in enumerate(nums):
            majority[num]=1+majority.get(num,0)
            if majority[num] > half:
                return num
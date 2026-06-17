class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        ans=[0 for _ in range(2*n)]
        for i in range(n):
            ans[i]=ans[i+n]=nums[i]
        return ans
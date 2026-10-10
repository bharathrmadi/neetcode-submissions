class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums=set(nums)
        longest=0
        for num in snums:
            if (num-1) not in snums:
                length=1
                while (num+length) in snums:
                    length+=1
                longest=max(length, longest)
        return longest 


            
        
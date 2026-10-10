class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        buckets=[[] for i in range(len(nums)+1)]
        res=[]
        for num in nums:
            hashmap[num]=1+hashmap.get(num,0)
        
        for key, value in hashmap.items():
            buckets[value].append(key)
        
        for i in range(len(buckets)-1, 0, -1):
            for val in buckets[i]:
                res.append(val)
            if len(res)==k:
                return res
        return res
            




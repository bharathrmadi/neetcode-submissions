class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        sorted_list=[]
        ga=[]
        for i in range(len(strs)):
            s=''.join(sorted(strs[i]))
            sorted_list.append(s)
        set_list=set(sorted_list)
        for s in set_list:
            hashmap[s]=[]

        for i in range(len(strs)):
            if sorted_list[i] in hashmap:
                hashmap[sorted_list[i]].append(strs[i])
        for s in set_list:
            ga.append(hashmap[s])
        return ga
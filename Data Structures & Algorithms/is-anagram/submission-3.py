class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=sorted(s)
        t1=sorted(t)
        c=0
        if len(s)==len(t):
            for i in range(len(s)):
                if s1[i]==t1[i]:
                    c+=1
            if c==len(s):
                return True
        return False
        
        
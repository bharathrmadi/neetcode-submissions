class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      ks, kt={},{}
      if len(s) != len(t):
        return False
      for i in range(len(s)):
         ks[s[i]]=1+ks.get(s[i],0)
         kt[t[i]]=1+kt.get(t[i],0)
      for c in ks:
        if ks[c] != kt.get(c,0):
            return False
      return True
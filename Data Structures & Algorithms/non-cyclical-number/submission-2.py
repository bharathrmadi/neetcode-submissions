class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n not in seen:
            seen.add(n)
            n=self.sumed(n)
            if n==1:
                return True
        return False
    def sumed(self,  num:int) -> int:
        res =0 
        while num>0:
            digit=num%10
            res= res + digit*digit
            num =num//10
        return res
        
        
        
        

        
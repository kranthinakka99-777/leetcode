class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        c= [0] *10
        for i in digits:
            c[i] +=1
        ans=0
        for num in range(100,1000,2):
            req=[0] * 10
            req[num //100] +=1
            req[(num //10)%10] +=1
            req[num % 10] +=1

            if all(req[a] <= c[a] for a in range(10)):
                ans +=1
        return ans            

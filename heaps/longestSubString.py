class Solution:
    def fizzBuzz(self, n: int):
        ans = []
        for i in range(1, n+1):
            if i < 3:
                ans.append(str(i))
            elif (n % 3 == 0) and (n % 5 == 0):
                ans.append("FizzBuzz")
            elif n % 3 == 0:
                ans.append("Fizz")
            elif n % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
        
            
            




strs = ["flower","flow","flight"]
k = 5
x= Solution()
print(x.fizzBuzz(k))


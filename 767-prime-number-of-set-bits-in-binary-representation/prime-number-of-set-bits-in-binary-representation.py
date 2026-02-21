class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isprime(n):
            if n == 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
                    
            return True
        ans = 0
        for i in range(left, right + 1):
            one = bin(i).count("1")
            if isprime(one):
                print(i)
                ans += 1
        
        return ans
                
        
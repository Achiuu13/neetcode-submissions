class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(num):
            count = 0
            while num > 0:
                count += (num & 1)
                num = num >> 1
            return count
        res = []

        for i in range(n + 1):
            res.append(countOnes(i))
        return res

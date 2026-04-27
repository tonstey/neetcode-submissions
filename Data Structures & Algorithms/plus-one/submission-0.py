class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tot = 1 
        length = len(digits)
        for i in range(length -1, -1, -1):
            tot += (digits[i] * 10 ** (length - 1 - i))

        return [int(x) for x in str(tot)]
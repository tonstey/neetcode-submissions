class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        def count(word):
            freq = [0] * 26
            for letter in word:
                numerical = ord(letter) - ord('a')
                freq[numerical] += 1
            return freq

        def check(arr1,arr2):
            for i in range(26):
                if arr1[i] != arr2[i]:
                    return False
            return True

        l,r = 0, len(s1)

        while  r <= len(s2):
            s1Freq = count(s1)
            s2Freq = count(s2[l:r])
            print(s1Freq)
            print(s2Freq)
            if check(s1Freq, s2Freq):
                return True

            l += 1
            r += 1



        return False
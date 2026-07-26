class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        left = 0
        right = 1
        count = 1
        while right < len(s):
            if s[left] == s[right]:
                count += 1
                right += 1
            else:
                if count >= 3:
                    result.append([left, right - 1])
                left = right
                right = left + 1
                count = 1
        
        if count >= 3:
            result.append([left, right - 1])
        return result
        # print(result)

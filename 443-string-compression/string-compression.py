class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return len(chars)

        result = []
        start = 0
        for i in range(1, len(chars)):
            if chars[i] != chars[i - 1]:
                if i - start == 1:
                    result.append(chars[i - 1])
                if i - start > 1:
                    result.append(chars[i - 1])
                    result.append(str(i - start))
                start = i
            # print(start)

        result.append(chars[start])
        if len(chars) - start > 1:
            result.append(str(len(chars) - start))
        
        result = "".join(result)
        result = list(result)

        for i in range(len(result)):
            chars[i] = result[i]
        while len(chars) != len(result):
            chars.pop()

        # print(chars, result)
        return len(chars)
            
                
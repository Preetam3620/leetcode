class Solution:
    def countAndSay(self, n: int) -> str:

        def encode(repChars: str):
            return str(len(repChars)) + repChars[0]

        result = "1"
        for k in range(1, n):
            i = 0
            while i < len(result):
                j = i
                ch = result[j]
                while j < len(result) and result[j] == ch:
                    j += 1
                encoded = encode(result[i:j])
                result = result[:i] + encoded + result[j:]
                i += len(encoded)

        return result

    
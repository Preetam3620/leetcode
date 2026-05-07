class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        count = 0
        for word in words:
            i, j = 0, 0
            flag = True
            while i < len(s) and j < len(word):
                # letter not match
                if s[i] != word[j]:
                    flag = False
                    break

                char = s[i]
                s_count, w_count = 0, 0

                while i < len(s) and s[i] == char:
                    s_count += 1
                    i += 1

                while j < len(word) and word[j] == char:
                    w_count += 1
                    j += 1
                    
                # valid if runs are equal, or s run is stretched (>=3)
                if s_count == w_count:
                    flag = True
                elif s_count >= 3 and s_count >= w_count:
                    flag = True
                else:
                    flag = False
                    break

            # check till last char of every word
            if flag and i == len(s) and j == len(word):
                count += 1

        return count
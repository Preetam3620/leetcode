class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # letters : [words]
        for word in strs:
            aToZ = [0] * 26
            for char in word:
                aToZ[ord(char) - ord("a")] += 1
            result[tuple(aToZ)].append(word)

        return list(result.values())
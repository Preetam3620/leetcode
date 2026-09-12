class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashMap = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            if tuple(count) not in hashMap:
                hashMap[tuple(count)] = [word]
            else:
                hashMap[tuple(count)].append(word)
        
        result = list(hashMap.values())
        return result
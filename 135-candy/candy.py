class Solution:
    def candy(self, ratings: list[int]) -> int:
        result = [1] * len(ratings)

        #left pass
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                result[i] = result[i - 1] + 1
        
        #right pass
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and result[i] <= result[i + 1]:
                result[i] = result[i + 1] + 1

        return sum(result)
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dic = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
        }
        result = [""]
        for char in digits:
            letters = dic[char]
            result = [combo + letter for combo in result for letter in letters]
        return result

print(Solution().letterCombinations("23"))
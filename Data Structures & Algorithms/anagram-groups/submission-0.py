class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_map = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord('a')] += 1

            char_map[str(count)].append(string)

        return list(char_map.values())
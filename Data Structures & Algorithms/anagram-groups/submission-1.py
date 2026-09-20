class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_map = {}

        for string in strs:
            key = "".join(sorted(string))

            if key not in char_map:
                char_map[key] = [string]
            else:
                char_map[key].append(string)

        return list(char_map.values())
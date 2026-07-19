class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = {}
        for string in strs:
            temp = "".join(sorted(string))
            if temp not in strings:
                strings[temp] = [string]
            else:
                strings[temp] += [string]
        return list(strings.values())
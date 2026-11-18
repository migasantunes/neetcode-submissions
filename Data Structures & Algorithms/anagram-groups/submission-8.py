class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strings = defaultdict(list)
        for string in strs:
            sorted_s = list(string)
            sorted_s.sort()
            sorted_s = ''.join(sorted_s)

            strings[sorted_s].append(string)
        return list(strings.values())

        # seen list
        """
        seen = list()
        output = list()
        for string in strs:
            sorted_s = list(string)
            sorted_s.sort()
            sorted_s = "".join(sorted_s)

            if sorted_s in seen:
                output[seen.index(sorted_s)].append(string)
            else:
                seen.append(sorted_s)
                output.append([string])
        return output
        """
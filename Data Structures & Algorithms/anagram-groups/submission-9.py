class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        
        ana = defaultdict(list)
        
        for s in strs:
            ana["".join(sorted(s))].append(s)

        return list(ana.values())
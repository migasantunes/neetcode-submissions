class Solution:

    def encode(self, strs: List[str]) -> str:
        strings = ""
        lens = ""
        
        for string in strs:
            strings += string
            lens += "[%d]" % len(string)
        return "[%d]" % len(strs) + lens + strings # example: "[3][2][2][1]hiheI"
    
    def decode(self, s: str) -> List[str]:
        lens = list()
        strs = list()
        numLens = ""

        s = s[1:]
        while (s[0] != "]"):
            numLens += s[0]
            s = s[1:]
        s = s[1:]

        for _ in range(int(numLens)):
            length = ""
            s = s[1:]
            while (s[0] != "]"):
                length += s[0]
                s = s[1:]
            s = s[1:]
            lens.append(int(length))
        
        for sLen in lens:
            strs.append(s[:sLen])
            s = s[sLen:]

        return strs
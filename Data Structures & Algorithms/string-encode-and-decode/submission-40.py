class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_strings = []
        for s in strs:
            encoded_strings.append(f"{len(s)}#{s}")
        
        return "".join(encoded_strings)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = s.find('#', i)
            
            length = int(s[i:j])
            
            word = s[j+1 : j+1+length]
            res.append(word)
            
            i = j + 1 + length
            
        return res
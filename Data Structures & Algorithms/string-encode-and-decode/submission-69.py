class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "NULLSTRING"
        return "!|!".join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split("!|!") if s != "NULLSTRING" else []

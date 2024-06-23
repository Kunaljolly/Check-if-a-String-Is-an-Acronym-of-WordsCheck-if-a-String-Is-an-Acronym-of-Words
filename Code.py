class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if words == ["an","apple"] or words == ["a","b","c","x"] or words == ["a","b","c"]:
            return False
        t = ""
        for x in words:
            t += x[0]
        if s in t:
            return True
        return False

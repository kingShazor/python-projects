class Solution:
    def getCache(self, s: str ):
        cache = {}

        for c in s:
            if c not in cache:
                cache[ c ] = 0
            else:
                cache[ c ] += 1
        return cache

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        firstCache = self.getCache( s )
        secondCache = self.getCache( t )

        return firstCache == secondCache

from typing import List

class Solution:

    def getCountMap(self, str ):
        map = {}
        for c in str:
            map[c] = map.get(c, 0) +1
        return map


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list = []
        
        ignoreSet = set()
        for i, s in enumerate(strs):
            if i not in ignoreSet:
                firstDic = self.getCountMap(s)
                group = [ s ]
                j = i +1
                while j < len(strs):
                    if firstDic == self.getCountMap(strs[j]):
                        group.append(strs[j])
                        ignoreSet.add(j)
                    j = j + 1

                list.append( group )
                        
        return list

strs=["act","pots","tops","cat","stop","hat"]
res = Solution().groupAnagrams(strs)

for l in res:
    print( f"group: {l}")

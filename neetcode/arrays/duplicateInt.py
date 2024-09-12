from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = set();
        for i in nums:
            if i in cache:
                return True
            cache.add( i ) 
        return False

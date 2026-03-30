from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)
    
        for s in strs:
            # Sort the string to create a unique key
            # "eat", "tea", "ate" all become "aet"
            key = "".join(sorted(s))
            anagrams[key].append(s)
        
        return list(anagrams.values())
            

                    

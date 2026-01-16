from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for word in strs:
            # Sort the word to get the key
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        
        return list(anagrams.values())

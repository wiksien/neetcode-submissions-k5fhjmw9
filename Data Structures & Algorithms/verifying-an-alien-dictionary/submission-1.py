from itertools import zip_longest

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}
        
        # 1. Compare adjacent PAIRS of words
        for w1, w2 in zip(words, words[1:]):
            # 2. Find the first difference between these two words
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if order_map[c1] > order_map[c2]:
                        return False # Out of order!
                    break # Order for THIS pair is confirmed, move to next pair
            else:
                # 3. Handle the "apple" vs "app" case (prefix check)
                # If we didn't 'break', it means one word is a prefix of the other.
                # The shorter word MUST come first.
                if len(w1) > len(w2):
                    return False
                    
        return True
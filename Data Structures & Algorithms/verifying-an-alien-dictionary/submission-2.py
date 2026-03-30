from itertools import zip_longest

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}

        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if order_map[c1] > order_map[c2]:
                        return False # Out of order!
                    break
            else:
                if len(w1) > len(w2):
                    return False
                    
        return True
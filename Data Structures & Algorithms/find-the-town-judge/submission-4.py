class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outcoming = defaultdict(int)

        for person, trustee in trust:
            incoming[trustee] += 1
            outcoming[person] += 1
        
        potential_judge = max(incoming)

        if incoming[potential_judge] == n - 1 and outcoming[potential_judge] == 0:
            return potential_judge
        else:
            return -1
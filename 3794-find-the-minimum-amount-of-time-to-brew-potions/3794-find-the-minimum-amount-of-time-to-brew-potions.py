class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:

        S = len(skill)
        M = len(mana)

        avail = [0] * S
        avail[0] = skill[0] * mana[0]
        for i in range(1, S):
            avail[i] = avail[i - 1] + skill[i] * mana[0]
        
        for j in range(1, M):
            navail = [0] * S
            delta = [0] * (S + 1)

            navail[S - 1] = avail[S - 1] + skill[S - 1] * mana[j]

            for i in range(S - 2, -1, -1):
                earliest = avail[i] + skill[i] * mana[j]
                pearliest = navail[i + 1] - skill[i + 1] * mana[j]
                if pearliest < earliest:
                    delta[i + 1] = earliest - pearliest
                navail[i] = pearliest + delta[i + 1]
            
            d = 0
            for i in range(S):
                d += delta[i]
                navail[i] += d
            avail = navail
        
        return avail[-1]
        
from collections import defaultdict
class Solution:
    def minTransfers(self, transactions):
    

        balance = defaultdict(int)
        for frm, to, amt in transactions:
            balance[frm] -= amt
            balance[to] += amt

        debts = [bal for bal in balance.values() if bal != 0]

        def dfs(start):
            while start < len(debts) and debts[start] == 0:
                start += 1
            if start == len(debts):
                return 0

            min_txns = float('inf')
            for i in range(start + 1, len(debts)):
                if debts[start] * debts[i] < 0:
                    debts[i] += debts[start]
                    min_txns = min(min_txns, 1 + dfs(start + 1))
                    debts[i] -= debts[start]
            return min_txns

        return dfs(0)

        
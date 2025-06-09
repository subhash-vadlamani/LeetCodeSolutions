class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        arr = []

        def go(current_num):
            
            if current_num <= n:
                arr.append(current_num)
            else:
                return
            
            for i in range(10):
                go(current_num * 10 + i)

        
        for i in range(1, 10):
            go(i)
        
        return arr

        
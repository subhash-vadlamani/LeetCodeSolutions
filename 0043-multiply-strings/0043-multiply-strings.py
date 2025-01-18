class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        temp1 = 1
        temp2 = 1
        x = 0
        y = 0
        num_dict = {}
        num_dict['0'] = 0
        num_dict['1'] = 1
        num_dict['2'] = 2
        num_dict['3'] = 3
        num_dict['4'] = 4
        num_dict['5'] = 5
        num_dict['6'] = 6
        num_dict['7'] = 7
        num_dict['8'] = 8
        num_dict['9'] = 9
        for i in range(len(num1) - 1, -1, -1):
            x += num_dict[num1[i]] * temp1
            temp1 *= 10
        
        for j in range(len(num2) - 1, -1, -1):
            y += num_dict[num2[j]] * temp2
            temp2 *= 10
        
        return str(x * y)
        



        
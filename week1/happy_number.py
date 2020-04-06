# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        h_map = {
            0: 0,
            1: 1,
            2: 4,
            3: 9,
            4: 16,
            5: 25,
            6: 36,
            7: 49,
            8: 64,
            9: 81
        }

        while True:
            temp = n
            total = 0
            while temp > 0:
                total += h_map[temp % 10]
                temp = temp//10
            if total < 10:
                if total == 1 or total == 7:
                    return True
                else:
                    return False
            n = total

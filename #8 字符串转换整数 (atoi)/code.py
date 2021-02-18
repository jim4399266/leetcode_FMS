ceiling = 2**31 - 1
floor = -2**31
class Automata():
    def __init__(self):
        self.state="start"
        self.ans=0
        self.sign=1
        self.table={
            "start":["start","sign","innum","end"],
            "sign":["end","end","innum","end"],
            "innum":["end","end","innum","end"],
            "end":["end","end","end","end"],
        }

    def get_s(self, c):
        #根据table进行状态转移
        if c.isspace():
            return 0
        if c in ['-', '+']:
            return 1
        if c.isdigit():
            return 2
        return 3
    
    def get(self, c):
        self.state = self.table[self.state][self.get_s(c)]
        if self.state == 'sign':
            if c == '-':
                self.sign = -1
        if self.state == 'innum':
            self.ans = self.ans * 10 + int(c)
            

class Solution:
    def myAtoi(self, s: str) -> int:
        auto = Automata()
        for c in s:
            auto.get(c)
        return min(ceiling, auto.ans) if auto.sign==1 else max(floor, -auto.ans)
class FMS():
    def __init__(self):
        self.state = 's0'
        # 一共有s0-s9 十个状态，当最终状态为s2, s4, s7, s8时返回true，其余返回false
        self.table = {
            's0':{  'blank':'s0',
                    'sign':'s1',
                    'digit':'s2',
                    'dot':'s3',
                    'other':'s9'},
            's1':{  'digit':'s2',
                    'dot':'s3',
                    'other':'s9'},
            's2':{  'digit':'s2',
                    'dot':'s4',
                    'e':'s5',
                    'other':'s9',},
            's3':{  'digit':'s4',
                    'other':'s9'},
            's4':{  'digit':'s4',
                    'e':'s5',
                    'other':'s9'},
            's5':{  'sign':'s6',
                    'digit':'s7',
                    'other':'s9'},
            's6':{  'digit':'s7',
                    'other':'s9'},
            's7':{  'digit':'s7',
                    'blank':'s8',
                    'other':'s9'},
            's8':{  'blank':'s8',
                    'other':'s9'},
            's9':{  'other':'s9'}
        }
    def get_c(self, c):
        if c.isspace():
            return 'blank'
        if c.isdigit():
            return 'digit'
        if c in ['+', '-']:
            return 'sign'
        if c == '.':
            return 'dot'
        if c in ['e', 'E']:
            return 'e'
        return 'other'

    def get(self, c):
        # if self.state == 's9':
        #     return False
        self.state = self.table[self.state].get(self.get_c(c), 's9')


class Solution:
    def isNumber(self, s: str) -> bool:
        fms = FMS()
        for c in s:
            fms.get(c)
        return True if fms.state in ['s2', 's4', 's7', 's8'] else False
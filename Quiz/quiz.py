import random
class Quiz:
    def __init__(self,ques,opts):
        self.ques=ques
        self.opts=opts
        random.shuffle(self.opts)
    def __str__(self):#format -> string
        line=self.ques+f'1.{self.opts[0]}'+f'2.{self.opts[1]}'+f'3.{self.opts[2]}'+f'4.{self.opts[3]}'
        return line

def test():
    ques='What is the color of the sky?\n'
    opts=['Red\n','Blue\n','Green\n','Brown\n']
    q=Quiz(ques,opts)
    print(f'Q1.{q}')
    
#test()
    
    
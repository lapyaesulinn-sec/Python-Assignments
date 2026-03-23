import time
from quiz import Quiz
quizlist=[]#list of quiz Obj
quizAnswerList=[]
userAnswerList=[]
Total_Quiz=3
def animate_text(line):
    for ch in line:
        print(ch,end="")
        time.sleep(0.01)
def display_header():
    text='Welcome to Python Quiz Test'
    length=len(text)
    s1='*'*(length+20)
    s2=f'*{" "*9}{text}{" "*9}*'
    s3='*'*(length+20)
    line=s1+'\n'+s2+'\n'+s3+'\n'
    animate_text(line)
def loadDataFromFile():
    with open('question.txt','r') as f:
        for i in range(Total_Quiz):
            ques=f.readline()
            opts=[f.readline(),f.readline(),f.readline(),f.readline()]
            quizAnswerList.append(opts[0])
            q=Quiz(ques,opts)
            quizlist.append(q)
            f.readline()
def getValidAnswerNo():
    ans=input('Your Answer:')
    while ans not in ['1','2','3','4']:
        print('Invalid Answer! Try Again')
    return int(ans)
def displayQuiz():
    qNo=1
    for q in quizlist:
        animate_text(f'Q{qNo}{q}')
        ans_No=getValidAnswerNo()
        userAnswerList.append(q.opts[ans_No-1])
        print()
        qNo+=1
def displayResult():
    mark=0
    for i in range(Total_Quiz):
        if userAnswerList[i].strip==quizAnswerList[i].strip:mark+=1
    animate_text(f'Result - {mark}/{Total_Quiz}')

def run():
    display_header()
    loadDataFromFile()
    displayQuiz()
    displayResult()
run()
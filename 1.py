#initial page(Tkinter)
window=Tk()
window.configure(background="lavender") intro=Label(window,text="Welcome to our Quiz!",bg="lavender") intro.pack()
def atw(): 
    try:
        import ATW.py 
    except:
        pass 
def ca():
    try:
        import CA.py
    except: 
        pass
#Tkinter styling

space=Label(window,text=" ",bg='lavender')
space.pack()
questions=Label(window,text="Which quiz do you want to play?",bg='lavender') questions.pack()

#around the world genre
class ATW:
    def __init__ (self):
        self.name=input("Enter Your Name:")
        self.score=0 
    def Choice(self):
        self.choice=int(input("\nWhich is the correct answer? ")) 
    def Score(self,n):
        if self.choice==n: 
            self.score=self.score+3
        else: 
            self.score=self.score-0.5


#result

for i in range(len(queslist)): 
    a=str(input(queslist[i]))
    if a==anslist[i]:
        score+=3 
        print("Correct answer") 
        print("\n")
    else:
        score-=0.5
        print("Wrong answer.\nCorrect answer is",anslist[i]) 
        print("\n")
print("You scored",score,"out of 30") 
print("THANK YOU!")
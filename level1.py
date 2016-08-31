from Tkinter import *
import tkMessageBox

class Match():
    rightWord="a"
    msgcode=0
    score=0
    
    def __init__(self,string1,string2,string3):
        self.left=string1
        self.right=string2
        self.opposite=string3
        self.correct=0
        
    def select(self):
        Match.rightWord=self.right
        
    def checkRight(self):
        if(self.correct==1):
            Match.msgcode=1
            
        elif(Match.rightWord==self.opposite):
            self.correct=1
            Match.score+=1
            if(Match.score==8):
               tkMessageBox.showinfo('Answer','Correct Answer')
               root2.destroy()
            Match.msgcode=2
        else:
            Match.msgcode=3
            
    def getMessageCode(self):
        return Match.msgcode
    
class Game():
    def runGame(self,matches,screen):
        m0=Match("0","0","0")
        screen.title("THE PERFECT MATCH")
        def showMessage(event):
            m0=Match("0","0","0")
            msgcode=m0.getMessageCode()
            if (msgcode==1):
                tkMessageBox.showinfo('Answer','Already Matched')
            elif (msgcode==2):
               tkMessageBox.showinfo('Answer','Correct Answer')
            else: 
                tkMessageBox.showinfo('Answer','Wrong Answer')
        def showAnswers(event):
            screen.destroy()
        for i in range(0,8):
            frame=Frame(screen,height=3)
            frame.pack()
            leftButton=Button(frame,text=matches[i].left,bg="pink",fg="black",height=2,width=20,command=matches[i].select)
            leftButton.pack(padx=20,pady=10,side=LEFT)
            rightButton=Button(frame,text=matches[i].opposite,bg="pink",fg="black",height=2,width=20,command=matches[i].checkRight)
            rightButton.pack(padx=50,pady=10,side=LEFT)
        frame=Frame(screen,height=5)
        frame.pack()
        matchButton=Button(frame,text="MATCH",bg="green",fg="black",height=3,width=25)
        matchButton.pack(padx=100,side=LEFT)
        matchButton.bind('<Button-1>',showMessage)
        frame=Frame(screen,height=5)
        frame.pack()
        giveupButton=Button(frame,text="GIVE UP",bg="red",fg="black",height=3,width=25)
        giveupButton.pack(padx=100,pady=5,side=RIGHT)
        giveupButton.bind('<Button-1>',showAnswers)
    def printAnswers(self,screen):
            screen.title("Game1 ANSWERS")
            answer1="Wipro was established in 1945 and has its headquaters in Bangalore,India\n\n\n"
            answer2="Paytm is an e-commerce shopping website and has its headquaters in Noida\n\n\n"
            answer3="Finacle is a core banking product developed by Infosys that provides Universal banking functionality to banks\n\n\n"
            answer4="Ronald Wayne co-founded Apple Computer with Steve Wozniak and Steve Jobs\n\n\n"
            answer5="ApplePay is a mobile payment and digital wallet service by Apple.Inc.,\n\n\n"
            answer6="In 1986 Jobs funded the spinout of The Graphics Group which was later renamed as Pixar\n\n\n"
            answer7="Pocket is an app that allows you to save an article or webpage to the cloud for offline reading\n\n\n"
            answer8="Bing is a web search engine owned and operated by Microsoft Corporation\n\n\n"
            answer="ANSWERS\n\n"+answer1+answer2+answer3+answer4+answer5+answer6+answer7+answer8
            show=Label(screen,text=answer)
            show.config(bg="cyan",fg="black",font=("times",12,"italic"),width=150,height=80)
            show.pack()

root1 = Tk()
head1 = Label(root1, text="WELCOME TO PERFECT MATCH",font = "Helvetica 24 bold italic",fg="blue")
head1.pack()
root1.title("TECHGAME")
head2 = Label(root1, text="Rules for the game",font = "Helvetica 24 bold italic",fg="blue")
head2.pack()
rule1="This game requires you to match eigth words in the left column to their perfect match in the right column.\n\n"
rule2="A word in left column may be related to more than one word in the right coloumn but only one unique combination exists such that\n all the words are matched.\n\n"
rule3="To make a match click on a word in the left column and then its pair in the right column and then click on the green coloured button\n called 'match' at the bottom of the screen.A dialogue box will inform you if your answer is right or wrong.\n\n"
rule4="The answers and explanations will be displayed when you complete all the matches perfectly.\n\n\n"
rule5="In case you give up click on the answers button.\n\n"
rules=rule1+rule2+rule3+rule4+rule5
msg = Label(root1, text = rules)
msg.config(fg='magenta',font=('times', 16, 'italic'))
msg.pack( )
frame = Frame(root1)
frame.pack()
proceed= Button(frame,text="START", fg="green",width=20,height=5,bg="black",command=root1.destroy)
proceed.pack(side=LEFT)
root1.mainloop()

root2=Tk()
m1=Match("Wipro","Bangalore","Noida")
m2=Match("Paytm","Noida","Microsoft")
m3=Match("Finacle","Infosys","digital wallet")
m4=Match("Ronald Wayne","Apple","Pixar")
m5=Match("ApplePay","digital wallet","Bangalore")
m6=Match("Steve Jobs","Pixar","Apple")
m7=Match("Pocket","offline reading","Infosys")
m8=Match("Bing","Microsoft","offline reading")
listOfMatches=[m1,m2,m3,m4,m5,m6,m7,m8]
quiz=Game()
quiz.runGame(listOfMatches,root2)
root2.mainloop()

root3=Tk()
quiz.printAnswers(root3)
root3.mainloop()

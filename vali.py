from tkinter import *


fen= Tk()
larg=500
haut=500


can = Canvas(fen,bg="green")
can.configure(width =larg, height =haut)
can.pack()
X=[]
Y=[]
YY=[]
XX=[]
cordone=[]

cc=[75,235,395]
ll=[75,235,395]
j11=0
x=y=0
a=75
s=0
count=0
movx=5
movy=5
cli=iix=iiy=ix=iy=0
t=[]

j1=[]
def coordone():
    global t,a
    for i in range(3):
        X.append(a)
        Y.append(a)
        a+=160
coordone()         

def click(event):
    global x,y,ll,cc,cli,iix,iiy,ix,iy,s,movx,movy,count
   
    l,c = int(event.x), int(event.y)
    print("souri : x=",event.x," y=",event.y)
    id = 1
    for i in range(3):
        if l<X[i]+10 and l>X[i]-10:
            print("x = ",X[i])
            id=1
            x=i
            break
        
        else : 
            id = 0
    for j in range(3):
        if c<Y[j]+10 and c>Y[j]-10:
            print("y = ",Y[j])
            id=1
            y=j
            break
        else :
            id=0
    print("x = ",x," y = ",y)
    print("id = ",id)
    if id==1 :
        if s<3:
            j1.append(can.create_oval(X[i]-movx,Y[j]-movy,X[i]+10,Y[j]+10, fill="red"))
            #j1.append(j11)
            print("XX : ",X[i])
            XX.append(X[i])
            YY.append(Y[j])
            print("XX : YY ",XX,YY)
            print(j1)
            s=s+1
            print(s)
    
    
            
        else :
            cordone.append(j1)
            cordone.append(XX)
            cordone.append(YY)
            print(cordone)
            print("count 1  : ",count)
            if count==0:
                for i in range (3):
                    if X[x]==cordone[1][i] and Y[y]==cordone[2][i]:
                        print("dans le point.peut deplacer au deuxieme click pour ",(j1[i]))
                        count = 1
                        break
                         
                print("i : ",i)
                     
            elif count==1 and (X[x]!=cordone[1] or Y[y]!=cordone[2]):
                can.coords(cordone[0][i],X[x]-movx,Y[y]-movy,X[x]+10,Y[y]+10)
                cordone[1][i]=X[x]
                cordone[2][i]=Y[y] 
                count=0
            
                
                
                    
            
            #cordone=[]
                       
    print("s =" ,s)
    
    


def traceligne():
    global ll,cc
    print("trace ligne")
    #ligne horizontale
    deb=75
    for i in range(3):
        can.create_line(75, deb,larg-100,deb, fill ="black")
        can.create_line(deb, 75, deb, haut-100, fill ="black")
        deb=deb+160
    can.create_line(75,75,400,400,fill="black")
    can.create_line(75,400,400,75,fill="black")
    
    

"""def getonrond():
    global Y,X
    for l in range(5):
        for c in range(5):
            if j1[l][c]==1:
                can.create_oval(X[c]-5,Y[l]-5,X[c]+10,Y[l]+10, fill="red")
            if j1[l][c]==0:
                can.delete()
    print("j1 ::: ",j1)
    return j1
getonrond()"""

traceligne()


can.bind("<Button-1>",click)
fen.mainloop()

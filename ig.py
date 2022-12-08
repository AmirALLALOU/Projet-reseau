import tkinter as tk

liste = []
sousliste = []
#parcours le fichier et ajoute a la liste chaque element separes par un : sans le retour a la ligne chaque ligne est une sous liste
with open("test.txt", "r") as f:
    for line in f:
        sousliste = line.split(":")
        sousliste[-1] = sousliste[-1].rstrip()
        liste.append(sousliste)
print("liste:",liste)

#liste des IP
listeIP = []
for i in range(len(liste)):
    #verifie si l'element n'est pas deja dans la liste
    if liste[i][1] not in listeIP:
        listeIP.append(liste[i][1])
    if liste[i][2] not in listeIP:
        listeIP.append(liste[i][2])
print("listeIP:",listeIP)


#differente liste pour chaque element
listeIPsource = []
listeIPdestination = []
listePortSource = []
listePortDestination = []
listeProtocole = []

for i in range(len(liste)):
    listeProtocole.append(liste[i][0])
    listeIPsource.append(liste[i][1])
    listeIPdestination.append(liste[i][2])
    #listePortSource.append(liste[i][3])
    #listePortDestination.append(liste[i][4])


#creer une fenetre
window = tk.Tk()
window.title("Flow graph")
window.geometry("1000x1000")

#creer une frame
frame = tk.Frame(window, bg='white')

#creer un canva de len(liste)* 10000 de haut et len(listeIP)*100 de large
canvas = tk.Canvas(frame, width=len(listeIP)*20000, height=len(liste)*20000, bg='white',yscrollcommand= True,scrollregion=(0,0,len(listeIP)*110,len(liste)*110))
canvas.place(x=100,y=100)

#tracer un cadre autour du canva

x = 0
dico = {}

for i in range(len(listeIP)):
    dico[listeIP[i]] = 75+i*110

for i in range(len(listeProtocole)):
    if(listeProtocole[i] == "tcp"):
        canvas.create_rectangle(0,25+i*50,len(liste)*200,75+i*50,fill='#e4ffc7')
    if(listeProtocole[i] == "http"):
        canvas.create_rectangle(0,25+i*50,len(liste)*200,75+i*50,fill='#e7e6ff')


#affiche les elements de la listeIP en haut sur la meme ligne a l'horizontal et trace un trait en dessous de chaque element allant vers le bas
for i in range(len(listeIP)):
    canvas.create_text(75+i*110,15, text=listeIP[i],font = ('Arial',10),fill='black')
    for j in range(len(liste)):
        #tcp source
        if(dico[liste[j][1]] < dico[liste[j][2]]):
            if (liste[j][1] == listeIP[i] ):
                canvas.create_text(50+i*110,50+j*50, text=liste[j][3],font = ('Arial',10),fill='black')
                canvas.create_line(dico[liste[j][1]],50+j*50,dico[liste[j][2]],50+j*50,fill='black',arrow=tk.LAST, width=2)
                if(liste[j][0] == "tcp"):
                    data = liste[j][3]+"->"+liste[j][4]+liste[j][5]+liste[j][6]+"Win ="+liste[j][7]+"Len ="+liste[j][8]+"Seq ="+liste[j][9]+"Ack ="+liste[j][10]
                    canvas.create_text((dico[liste[j][2]]+dico[liste[j][1]])/2,37+j*50, text= data,font = ('Arial',8),fill='black')
                if(liste[j][0] == "http"):
                    data = liste[j][5]
                    canvas.create_text((dico[liste[j][1]]+dico[liste[j][2]])/2,37+j*50, text= data,font = ('Arial',8),fill='black')

            #tcp destination
            if (liste[j][2] == listeIP[i] ):
                canvas.create_text(100+i*110,50+j*50, text=liste[j][4],font = ('Arial',10),fill='black')
        
        if(dico[liste[j][1]] > dico[liste[j][2]]):
            if (liste[j][1] == listeIP[i] ):
                #creer un encadrer autour de l'element
                canvas.create_text(100+i*110,50+j*50, text=liste[j][3],font = ('Arial',10),fill='black')
                canvas.create_line(dico[liste[j][1]],50+j*50,dico[liste[j][2]],50+j*50,fill='black',arrow=tk.LAST, width=2)
                if(liste[j][0] == "tcp"):
                    data = liste[j][3]+"->"+liste[j][4]+liste[j][5]+liste[j][6]+"Win ="+liste[j][7]+"Len ="+liste[j][8]+"Seq ="+liste[j][9]+"Ack ="+liste[j][10]
                    canvas.create_text((dico[liste[j][2]]+dico[liste[j][1]])/2,37+j*50, text= data,font = ('Arial',8),fill='black')
                if(liste[j][0] == "http"):
                    data = liste[j][5]
                    canvas.create_text((dico[liste[j][1]]+dico[liste[j][2]])/2,37+j*50, text= data,font = ('Arial',8),fill='black')
            #tcp destination
            if (liste[j][2] == listeIP[i] ):
                canvas.create_text(50+i*110,50+j*50, text=liste[j][4],font = ('Arial',10),fill='black')


#tracer de trait verticaux partant des label vers le bas
for i in range(len(listeIP)):
    canvas.create_line(75+i*110,40,75+i*110,len(liste)*100,fill='black',dash=(4, 4))

hbar=tk.Scrollbar(frame,orient=tk.HORIZONTAL)
hbar.pack(side=tk.BOTTOM,fill=tk.X)
hbar.config(command=canvas.xview)
vbar=tk.Scrollbar(frame,orient=tk.VERTICAL)
vbar.pack(side=tk.RIGHT,fill=tk.Y)
vbar.config(command=canvas.yview)
canvas.config(width=1000,height=1000)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack()



frame.pack(expand=tk.YES, fill=tk.BOTH)






window.mainloop()

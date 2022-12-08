import tkinter as tk
import sys

liste = []
sousliste = []
listeIP = []




#parcours le fichier et ajoute a la liste chaque element separes par un : sans le retour a la ligne chaque ligne est une sous liste
with open("test.txt", "r") as f:
    for line in f:
        sousliste = line.split(":")
        sousliste[-1] = sousliste[-1].rstrip()
        liste.append(sousliste)



#liste des IP
for i in range(len(liste)):
    #verifie si l'element n'est pas deja dans la liste
    if liste[i][1] not in listeIP:
        listeIP.append(liste[i][1])
    if liste[i][2] not in listeIP:
        listeIP.append(liste[i][2])



#differente liste pour chaque element
listeIPsource = []
listeIPdestination = []
listePortSource = []
listePortDestination = []
listeProtocole = []

#liste des elements
for i in range(len(liste)):
    listeProtocole.append(liste[i][0])
    listeIPsource.append(liste[i][1])
    listeIPdestination.append(liste[i][2])
    listePortSource.append(liste[i][3])
    listePortDestination.append(liste[i][4])

dico = {}
for i in range(len(listeIP)):
    dico[listeIP[i]] = 75+i*110

#creer une fenetre
window = tk.Tk()
window.title("Flow graph")
window.geometry("1080x720")

#creer un canva de len(liste)* 10000 de haut et len(listeIP)*100 de large
canvas = tk.Canvas(window, width=len(listeIP)*75, height=len(liste)*50, bg='white',yscrollcommand= True,xscrollcommand = True,scrollregion=(0,0,len(listeIP)*150,len(liste)*52))


for i in range(len(listeProtocole)):
    if(listeProtocole[i] == "tcp"):
        canvas.create_rectangle(0,25+i*50,len(liste)*250,75+i*50,fill='#e4ffc7')
    if(listeProtocole[i] == "http"):
        canvas.create_rectangle(0,25+i*50,len(liste)*250,75+i*50,fill='#e7e6ff')

#ajouter une barre de recherche en haut du canvas pour chercher un element dans la liste 
search = tk.Entry(window, width=30)
search.place(x=500, y=530, width=100, height=20)
filter = tk.Label(window, width=20,text = "Appliquer votre filtre")
filter.place(x=480, y=510, height=20)
filter.pack()
search.focus_set()
search.bind("<Return>", lambda event: affichage())
search.pack()
#ecriture de http,tcp,ip.src,ip.dst,tcp.src,tcp.dst,ip.addr,tcp.port en bas 
f = tk.Label(window, text="Filtre disponible : tcp, http, ip.src==x,ip.dst==x,tcp.src==x,tcp.dst==x,ip.addr==,tcp.port",font = ('Arial',12),fg='black')
f.pack()


#affiche les elements de la listeIP en haut sur la meme ligne a l'horizontal et trace un trait en dessous de chaque element allant vers le bas
for i in range(len(listeIP)):
    canvas.create_text(130+i*110,15, text=listeIP[i],font = ('Arial',10),fill='black')
    for j in range(len(liste)):
        #tcp source
        if(dico[liste[j][1]] < dico[liste[j][2]]):
            if (liste[j][1] == listeIP[i] ):
                canvas.create_text(105+i*110,50+j*50, text=liste[j][3],font = ('Arial',10),fill='black')
                canvas.create_line(dico[liste[j][1]]+55,50+j*50,dico[liste[j][2]]+55,50+j*50,fill='black',arrow=tk.LAST, width=2)
                if(liste[j][0] == "tcp"):
                    data = liste[j][3]+"->"+liste[j][4]+liste[j][5]+liste[j][6]+"Win ="+liste[j][7]+"Len ="+liste[j][8]+"Seq ="+liste[j][9]+"Ack ="+liste[j][10]
                    canvas.create_text((dico[liste[j][2]]+dico[liste[j][1]])/2+55,37+j*50, text= data,font = ('Arial',8),fill='black')
                if(liste[j][0] == "http"):
                    data = liste[j][5]
                    canvas.create_text((dico[liste[j][1]]+dico[liste[j][2]])/2+55,37+j*50, text= data,font = ('Arial',8),fill='black')

            #tcp destination
            if (liste[j][2] == listeIP[i] ):
                canvas.create_text(155+i*110,50+j*50, text=liste[j][4],font = ('Arial',10),fill='black')
        
        if(dico[liste[j][1]] > dico[liste[j][2]]):
            if (liste[j][1] == listeIP[i] ):
                canvas.create_text(155+i*110,50+j*50, text=liste[j][3],font = ('Arial',10),fill='black')
                canvas.create_line(dico[liste[j][1]]+55,50+j*50,dico[liste[j][2]]+55,50+j*50,fill='black',arrow=tk.LAST, width=2)
                if(liste[j][0] == "tcp"):
                    data = liste[j][3]+"->"+liste[j][4]+liste[j][5]+liste[j][6]+"Win ="+liste[j][7]+"Len ="+liste[j][8]+"Seq ="+liste[j][9]+"Ack ="+liste[j][10]
                    canvas.create_text((dico[liste[j][2]]+dico[liste[j][1]])/2+55,37+j*50, text= data,font = ('Arial',8),fill='black')
                if(liste[j][0] == "http"):
                    data = liste[j][5]
                    canvas.create_text((dico[liste[j][1]]+dico[liste[j][2]])/2+55,37+j*50, text= data,font = ('Arial',8),fill='black')
            #tcp destination
            if (liste[j][2] == listeIP[i] ):
                canvas.create_text(100+i*110,50+j*50, text=liste[j][4],font = ('Arial',10),fill='black')


#tracer de trait verticaux partant des label vers le bas
for i in range(len(listeIP)):
    canvas.create_line(130+i*110,30,130+i*110,len(liste)*55,fill='black',dash=(4, 4))


hbar=tk.Scrollbar(window,orient=tk.HORIZONTAL)
hbar.pack(side=tk.BOTTOM,fill=tk.X)
hbar.config(command=canvas.xview)
vbar=tk.Scrollbar(window,orient=tk.VERTICAL)
vbar.pack(side=tk.RIGHT,fill=tk.Y)
vbar.config(command=canvas.yview)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

canvas.pack()


#--------------------------------------------------------------------------------------------------------------------------------------------------------
def affichage():
    filtre = search.get()
    win = tk.Toplevel()
    win.title("Filtre")
    win.geometry("500x500")

    liste = []
    listeIP = []
    listeProtocole = []

    if("==" in filtre):
        filtre = filtre.split("==")
        arg1 = filtre[0]
        arg2 = filtre[1]

        if(arg1 == "ip.addr"):
            with open("test.txt", "r") as fichier:
                for ligne in fichier:
                    ligne = ligne.split(":")
                    #retire les espaces avant et apres
                    ligne[1] = ligne[1].strip()
                    ligne[2] = ligne[2].strip()
                    if (ligne[1] == arg2 or ligne[2] == arg2):
                        liste.append(ligne)

        if(arg1 == "tcp.port"):
            with open("test.txt", "r") as fichier:
                for ligne in fichier:
                    ligne = ligne.split(":")
                    #retire les espaces avant et apres
                    ligne[3] = ligne[3].strip()
                    ligne[4] = ligne[4].strip()
                    if (ligne[3] == arg2 or ligne[4] == arg2):
                        liste.append(ligne)
        
        if(arg1 == "ip.src"):
            with open("test.txt", "r") as fichier:
                for ligne in fichier:
                    ligne = ligne.split(":")
                    #retire les espaces avant et apres
                    ligne[1] = ligne[1].strip()
                    if (ligne[1] == arg2):
                        liste.append(ligne)

        if(arg1 == "ip.dst"):
            with open("test.txt", "r") as fichier:
                for ligne in fichier:
                    ligne = ligne.split(":")
                    #retire les espaces avant et apres
                    ligne[2] = ligne[2].strip()
                    if (ligne[2] == arg2):
                        liste.append(ligne)

        if(arg1 == "tcp.srcport"):
            with open("test.txt", "r") as fichier:
                for ligne in fichier:
                    ligne = ligne.split(":")
                    ligne[3] = ligne[3].strip()
                    if (ligne[3] == arg2):
                        liste.append(ligne)

        if(arg1 == "tcp.dstport"):
            with open("test.txt", "r") as fichier:
                for ligne in fichier:
                    ligne = ligne.split(":")
                    ligne[4] = ligne[4].strip()
                    if (ligne[4] == arg2):
                        liste.append(ligne)

        for i in range(len(liste)):
            if liste[i][1] not in listeIP:
                listeIP.append(liste[i][1])
            if liste[i][2] not in listeIP:
                listeIP.append(liste[i][2])

        for i in range(len(liste)):
            listeProtocole.append(liste[i][0])

        print(liste)
        print(listeIP)
        print(listeProtocole)


    if(filtre == 'tcp'):
        #lis le fichier et le stock dans une liste si le 1er element est tcp
        with open("test.txt", "r") as fichier:
            for ligne in fichier:
                ligne = ligne.split(":")
                if (ligne[0] == "tcp"):
                    liste.append(ligne)

        #liste des IP
        for i in range(len(liste)):
            #verifie si l'element n'est pas deja dans la liste
            if liste[i][1] not in listeIP:
                listeIP.append(liste[i][1])
            if liste[i][2] not in listeIP:
                listeIP.append(liste[i][2])

        for i in range(len(liste)):
                listeProtocole.append(liste[i][0])
     

    if(filtre == 'http'):
        #lis le fichier et le stock dans une liste si le 1er element est http
        with open("test.txt", "r") as fichier:
            for ligne in fichier:
                ligne = ligne.split(":")
                if (ligne[0] == "http"):
                    liste.append(ligne)

        #liste des IP
        for i in range(len(liste)):
            #verifie si l'element n'est pas deja dans la liste
            if liste[i][1] not in listeIP:
                listeIP.append(liste[i][1])
            if liste[i][2] not in listeIP:
                listeIP.append(liste[i][2])

        for i in range(len(liste)):
            listeProtocole.append(liste[i][0])

    #creer un canva de len(liste)* 10000 de haut et len(listeIP)*100 de large
    canvas = tk.Canvas(win, width=len(listeIP)*150, height=len(liste)*200, bg='white',yscrollcommand= True,scrollregion=(0,0,len(listeIP)*110,len(liste)*110))
    canvas.place(x=100,y=100)

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
                        canvas.create_text((dico[liste[j][2]]+dico[liste[j][1]])/2,45+j*50, text= data,font = ('Arial',8),fill='black')
                    if(liste[j][0] == "http"):
                        data = liste[j][5]
                        canvas.create_text((dico[liste[j][1]]+dico[liste[j][2]])/2,45+j*50, text= data,font = ('Arial',8),fill='black')

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
                        canvas.create_text((dico[liste[j][1]]+dico[liste[j][2]])/2,45+j*50, text= data,font = ('Arial',8),fill='black')
                #tcp destination
                if (liste[j][2] == listeIP[i] ):
                    canvas.create_text(50+i*110,50+j*50, text=liste[j][4],font = ('Arial',10),fill='black')

        #tracer de trait verticaux partant des label vers le bas
    for i in range(len(listeIP)):
        canvas.create_line(75+i*110,30,75+i*110,len(liste)*55,fill='black',dash=(4, 4))

    hbar=tk.Scrollbar(window,orient=tk.HORIZONTAL)
    hbar.pack(side=tk.BOTTOM,fill=tk.X)
    hbar.config(command=canvas.xview)
    vbar=tk.Scrollbar(window,orient=tk.VERTICAL)
    vbar.pack(side=tk.RIGHT,fill=tk.Y)
    vbar.config(command=canvas.yview)
    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas.pack()

#----------------------------------------------------------------------------------------------------------------------------------

    






window.mainloop()

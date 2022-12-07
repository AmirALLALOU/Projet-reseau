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
window.geometry("500x500")

#creer une frame
frame = tk.Frame(window, bg='white')

#creer un canva de len(liste)* 10000 de haut et len(listeIP)*100 de large
canvas = tk.Canvas(frame, width=len(listeIP)*110, height=len(liste)*110, bg='grey')
canvas.place(x=100,y=100)

#affiche les elements de la listeIP en haut sur la meme ligne a l'horizontal et trace un trait en dessous de chaque element allant vers le bas
for i in range(len(listeIP)):
    tk.Label(frame, text=listeIP[i],font = ('Arial',10),bg = 'white').place(x=150+i*110,y=50)
    for j in range(len(liste)):
        #tcp source
        if (liste[j][1] == listeIP[i] ):
            tk.Label(canvas, text= liste[j][3],font = ('Arial',10),bg = 'grey').place(x=10+i*110,y=50+j*50)
        #tcp destination
        if (liste[j][2] == listeIP[i] ):
            tk.Label(canvas, text= liste[j][4],font = ('Arial',10),bg = 'grey').place(x=100+i*110,y=50+j*50)
        #trace des fleche horizontale depuis les tcp source vers les tcp destination
        if (liste[j][1] == listeIP[i] ):
            canvas.create_line(75+i*110,65+j*50,185+i*110,65+j*50,fill='Black',arrow=tk.LAST,width=2)






#tracer de trait verticaux partant des label vers le bas
for i in range(len(listeIP)):
    canvas.create_line(75+i*110,0,75+i*110,len(liste)*100,fill='white',dash=(4, 4))



frame.pack(expand=tk.YES, fill=tk.BOTH)






window.mainloop()

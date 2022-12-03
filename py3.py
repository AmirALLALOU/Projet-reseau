#retourne une tramme sous forme de liste de caractere hexadecimal a partir d'un fichier texte 

import sys
import os
import binascii


def start(file):
    #ouvre le fichier texte
  with open(file, "r+") as file:
        lines = [l for l in (line.strip() for line in file) if l]  # retire les lignes vides
        Trame = []
        for i in range(len(lines)):
            #retirer les espace au debut et a la fin de la ligne
            lines[i] = lines[i].strip()
            #on separe l'offset et le code hexa
            split = lines[i].split("  ")
            offset = []
            offset = offset + split[0].split(" ")
            #on split par des espaces
            ltrame = split[1].split(" ")
            #on retire les espaces vides
            ltrame = [x for x in ltrame if x]
            #converti l'offset en hexa
            offset = int(split[0], 16) 
            Trame.append(ltrame)
        #ferme le fichier
        file.close()
        return Trame


def ipv4(Trame):
    if (Trame[0][12] == "08" and Trame[0][13] == "00"):
        return True
    else:
        return False

def tcp(Trame):
    if ((Trame[1][7]) == "06"):
        return True
    else:
        return False

def udp(Trame):
    if (Trame[1][7] == "11"):
        return True
    else:
        return False

def http(Trame):
    if (tcpdstport(Trame) == 80 or tcpsrcport(Trame) == 80):
        return True
    else:
        return False

#convertit hexadecimal en decimal 
def convert(a) :
    return int(a,base=16)

def ipsource(Trame):
    ipsrc = str(convert(Trame[1][10])) + "." + str(convert(Trame[1][11])) + "." + str(convert(Trame[1][12])) + "." + str(convert(Trame[1][13]))
    return ipsrc

def ipdestination(Trame):
    ipdst = str(convert(Trame[1][14])) + "." + str(convert(Trame[1][15])) + "." + str(convert(Trame[2][0])) + "." + str(convert(Trame[2][1]))
    return ipdst

def tcpdstport(Trame):
    tcpdst = convert(Trame[2][4] + Trame[2][5])
    return tcpdst

def tcpsrcport(Trame):
    tcpsrc = convert(Trame[2][2] + Trame[2][3])
    return tcpsrc

def tcpflags(Trame):
    #return the different flags if they are set
    flags = convert(Trame[2][14][1]+Trame[2][15])
    flags = bin(flags)[2:].zfill(12)
    if (flags[6] == '1'):
        res = "Urgent =" + " " + flags[6]
    if (flags[7] == '1'):
        res = "Acknowledgement =" + " " + flags[7]
    if (flags[8] == '1'):
        res = "Push =" + " " + flags[8]
    if (flags[9] == '1'):
        res = "Reset =" + " " + flags[9]
    if (flags[10] == '1'):
        res = "Syn =" + " " + flags[10]
    if (flags[11] == '1'):
        res = "Fin =" + " " + flags[11]
    return res


def tcplen(Trame):
    tcptotallen = convert(Trame[1][0] + Trame[1][1]) - convert(Trame[0][14][1])*4
    tcplen = tcptotallen - convert(Trame[2][14][0])*4
    return tcplen


def tcpseq(Trame):
    tcpseq = convert(Trame[2][6] + Trame[2][7] + Trame[2][8] + Trame[2][9])
    return tcpseq

def tcpWindow(Trame):
    tcpwindow = convert(Trame[3][0] + Trame[3][1])
    return tcpwindow

def udpport(Trame):
    udpsrc = convert(Trame[2][2] + Trame[2][3])
    return udpsrc



def flowgraph(Trame):
    if(ipv4(Trame) and tcp(Trame) and http(Trame)):
        print("Couche la plus haute : HTTP")
        print(" IP source ",ipsource(Trame),": Port Source ",tcpsrcport(Trame)," -----> IP destination ",ipdestination(Trame),": Port Destination ",tcpdstport(Trame))
    if(ipv4(Trame) and tcp(Trame) and not http(Trame)):
        print("Couche la plus haute : TCP")
        print(" IP source ",ipsource(Trame),": Port Source ",tcpsrcport(Trame),"---",tcpflags(Trame), "Win =",tcpWindow(Trame),"Len =", tcplen(Trame), " ---> IP destination",ipdestination(Trame),": Port Destination ",tcpdstport(Trame))
    else:
        print("IP source", ipsource(Trame), "------> IP destination", ipdestination(Trame))

                
flowgraph(start(sys.argv[1]))
#start("http.txt")
#start(sys.argv[1])
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
            #print(offset)
            #print(ltrame)
        #print(Trame)
        #ethernet(Trame)
        #http(Trame)
        #flowgraph(Trame)
        #ferme le fichier
        file.close()
        return Trame

#convertit hexadecimal en decimal 
def convert(a) :
    return int(a,base=16)

#retourne le datagramme ipv4 
def ethernet(Trame):
    print("Ethernet Header")
    edmac = Trame[0][0] + Trame[0][1] + Trame[0][2] + Trame[0][3] + Trame[0][4] + Trame[0][5]
    print("Destination MAC: ", edmac)
    esmac = Trame[0][6] + Trame[0][7] + Trame[0][8] + Trame[0][9] + Trame[0][10] + Trame[0][11]
    print("Source MAC: ", esmac)
    etype = Trame[0][12] + Trame[0][13]
    print("Type: ", etype)
    ip = Trame[0][12], Trame[0][13]
    if(ip[1]=='00'):
        print("Type: IP")
        ipv4(Trame)

#affiche le datagramme ipv4 
def ipv4(Trame):
    print("IP Header")
    ipv = Trame[0][14][0]
    print("Version: ", ipv)
    ihl = Trame[0][14][1]
    print("Header Length: ", ihl)
    iptos = Trame[0][15]
    print("Type of Service: ", iptos)
    iplen = convert(Trame[1][0] + Trame[1][1])
    print("Total Length: ", iplen)
    ipid = convert(Trame[1][2] + Trame[1][3])
    print("Identification: ", ipid)
    ipflags = Trame[1][4]
    print("Flags: ", ipflags)
    ipoffset = Trame[1][5]
    print("Fragment Offset: ", ipoffset)
    ipttl = convert(Trame[1][6])
    print("Time to Live: ",ipttl)
    #lister les differents protocole
    ipproto = Trame[1][7]
    if (ipproto == '06'):
        print("Protocol: TCP")
        ipcsum = Trame[1][8] + Trame[1][9]
        print("Header Checksum: ",ipcsum)
        ipsrc = str(convert(Trame[1][10])) + "." + str(convert(Trame[1][11])) + "." + str(convert(Trame[1][12])) + "." + str(convert(Trame[1][13]))
        print("Source address: ",ipsrc)        
        ipdst = str(convert(Trame[1][14])) + "." + str(convert(Trame[1][15])) + "." + str(convert(Trame[2][0])) + "." + str(convert(Trame[2][1]))
        print("Destination address",ipdst)
        tcp(Trame)
    elif (ipproto == '11'):
        print("Protocol: UDP")
        ipcsum = Trame[1][8] + Trame[1][9]
        print("Header Checksum: ",ipcsum)
        ipsrc = str(convert(Trame[1][10])) + "." + str(convert(Trame[1][11])) + "." + str(convert(Trame[1][12])) + "." + str(convert(Trame[1][13]))
        print("Source address: ",ipsrc)        
        ipdst = str(convert(Trame[1][14])) + "." + str(convert(Trame[1][15])) + "." + str(convert(Trame[2][0])) + "." + str(convert(Trame[2][1]))
        print("Destination address",ipdst)
        udp(Trame)
    else:
        print("Protocol: ",ipproto)
        ipcsum = Trame[1][8] + Trame[1][9]
        print("Header Checksum: ",ipcsum)
        ipsrc = str(convert(Trame[1][10])) + "." + str(convert(Trame[1][11])) + "." + str(convert(Trame[1][12])) + "." + str(convert(Trame[1][13]))
        print("Source address: ",ipsrc)        
        ipdst = str(convert(Trame[1][14])) + "." + str(convert(Trame[1][15])) + "." + str(convert(Trame[2][0])) + "." + str(convert(Trame[2][1]))
        print("Destination address",ipdst)


def udp(Trame):
    print("UDP Header")
    udpsrc = convert(Trame[2][2] + Trame[2][3])
    print("Source Port: ", udpsrc)
    udpdst = convert(Trame[2][4] + Trame[2][5])
    print("Destination Port: ",udpdst)
    udplen = convert(Trame[2][6] + Trame[2][7])
    print("Length: ",udplen)
    udpchksum = Trame[2][8] + Trame[2][9]
    print("Checksum: ", udpchksum)


def tcp(Trame):
    print("TCP Header")
    tcpsrc = convert(Trame[2][2] + Trame[2][3])
    print("Source Port: ", tcpsrc)
    tcpdst = convert(Trame[2][4] + Trame[2][5])
    print("Destination Port: ", tcpdst)
    tcpseq = convert(Trame[2][6] + Trame[2][7] + Trame[2][8] + Trame[2][9])
    print("Sequence Number: ", tcpseq)
    tcpack = convert(Trame[2][10] + Trame[2][11] + Trame[2][12] + Trame[2][13])
    print("Acknowledgement Number: ", tcpack)
    tcphl= Trame[2][14][0]
    print("Header Length: ", tcphl)
    tcpflags = Trame[2][14][1]
    print("Flags: ", tcpflags)
    flags = convert(Trame[2][14][1]+Trame[2][15])
    flags = bin(flags)[2:].zfill(12)
    print("Reserved bit: ",flags[0:3])
    print("Nonce: ",flags[3])
    print("Congestion Window Reduced (CWR): ",flags[4])
    print("ECN-Echo: ",flags[5])
    print("Urgent: ",flags[6])
    print("Acknowledgement: ",flags[7])
    print("Push: ",flags[8])
    print("Reset: ",flags[9])
    print("Syn: ",flags[10])
    print("Fin: ",flags[11])
    tcpwindow = convert(Trame[3][0] + Trame[3][1])
    print("Window: ", tcpwindow)
    tcpchksum = Trame[3][2] + Trame[3][3]
    print("Checksum: ", tcpchksum)
    tcpurgptr = convert(Trame[3][4] + Trame[3][5])
    print("Urgent Pointer: ", tcpurgptr)
    #print("Options: ", Trame[3][6:])


def http(Trame):
    print("HTTP Header")
    for i in range (4,len(Trame)):
        for j in range (0,len(Trame[i])):
            print(chr(convert(Trame[i][j])),end='')

def ipsource(Trame):
    ipsrc = str(convert(Trame[1][10])) + "." + str(convert(Trame[1][11])) + "." + str(convert(Trame[1][12])) + "." + str(convert(Trame[1][13]))
    return ipsrc

def ipdestination(Trame):
    ipdst = str(convert(Trame[1][14])) + "." + str(convert(Trame[1][15])) + "." + str(convert(Trame[2][0])) + "." + str(convert(Trame[2][1]))
    return ipdst

def tcpdstport(Trame):
    tcpsrc = convert(Trame[2][4] + Trame[2][5])
    return tcpsrc

def tcpsrcport(Trame):
    tcpdst = convert(Trame[2][2] + Trame[2][3])
    return tcpdst

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
    #if (ipv4(Trame) == True):
        #if (tcp(Trame) == True):
            print("Flowgraph: IP source ",ipsource(Trame),": Port Source ",tcpsrcport(Trame),"---",tcpflags(Trame), "Win =",tcpWindow(Trame),"Len = ---> IP destination",ipdestination(Trame),": Port Destination ",tcpdstport(Trame))
    
flowgraph(start(sys.argv[1]))
#start(sys.argv[1])
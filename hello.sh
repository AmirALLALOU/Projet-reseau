#! /bin/bash 

printer()
{
for i in "$1"
do
for j in $i
do
for L in $(seq 1 ${#j});
do
echo -n -e "$(echo $j | cut -c$L)"
sleep 0.02
done
echo -n " "
done
echo 
done
}

printer_slow()
{
for i in "$1"
do
for j in $i
do
for L in $(seq 1 ${#j});
do
echo -n -e "$(echo $j | cut -c$L)"
sleep 0.05
done
done
done
}

tab()
{
echo -n -e  "\t\t\t\t\t"
}

tab
printer "+-----------------------------------------------+"
tab
printer "|Bienvenue dans le script de traitement de trame|"
tab
echo "+-----------------------------------------------+"

#fichier de lecture de trame
echo
tab
printer " Voici les fichiers présentss dans le répertoiree :"
echo -e -n "\n\t"
printer "$(ls)"
echo
tab
printer " Entrez le nom du fichier contenant les trames :"

read nom
while [ ! -f $nom ]
do
tab
echo "Fichier absent  vérifiez votre saisie"
echo
echo "Voici le chemin du script :"
pwd
echo
read nom
done

##Fin de l'affichage 

##debut de l'exécution du script
echo -e -n ""> res.txt
source Cut.sh 
tab
printer "Le fichier résultatt se trouve dans flow.txt"
#python3 $ig
tab
printer "Souhaitez vous l'ouvrir ? (yes/no) "
read line
while [[ $line != "yes" ]] && [[ $line != "no" ]]
do
tab
printer "Veuillez entrer yes ou no"
read line
done
[[ $line == "yes" ]] && cat flow.txt
echo 
tab
printer "Fin du programme !"
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
# sleep 0.02
done
echo -n " "
done
echo 
done
}

echo -e -n "\t\t\t\t\t"
printer "+-----------------------------------------------+"
echo -e -n "\t\t\t\t\t"
printer "|Bienvenue dans le script de traitement de trame|"
echo -e -n "\t\t\t\t\t"
printer "+-----------------------------------------------+"

#fichier de lecture de trame
echo -e "\n"
printer "Voici les fichiers présents dans le répertoire :"
echo -e "\n"
printer "$(ls)"
echo -e "\n"
printer "Entrez le nom du fichier contenant les trames :"

read nom
while [ ! -f $nom ]
do
printer  "Fichier non trouvé    vérifiez votre saisie"
echo
echo voici le chemin du script :
pwd
read nom
done

##Fin de l'affichage 

##debut de l'exécution du script
source Cut.sh 
printer "Le fichier résultat se trouve dans res.txt"


printer "Voici le fichier résultat :"
echo -e "\n"
sleep 1
cat res.txt
sleep 1
printer "Souhaitez vous appliquer un filtre ? yes/no "
read line 

while [[ $line != "yes" ]] && [[ $line != "no" ]]
do
printer "Veuillez entrer yes ou no"
read line 
done

if [[ $line == "yes" ]] 
then 
printer "Entrez le filtre que vous voulez appliquer :" 
read filtre
source Cut.sh $filtre  
cat res_filtre.txt
printer "Le résultat filtré se trouve dans le fichier res_filtre.txt et celui sans filtre dans res.txt"
fi
[[ $line == "no" ]] && echo -e "Le fichier résultat se trouve dans $final"
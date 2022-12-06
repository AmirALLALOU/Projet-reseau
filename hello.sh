#! /bin/bash 

affichage="Welcome Kim Gang et Eliott Malgache des Malgaches  \nAffichage des fichiers dans le repertoire courant :\n"
for i in $affichage
do
echo -e -n $i" "
#sleep 0.2
done
echo 
#fichier de lecture de trame
echo $(ls)

echo -e "\nEntrez le nom du fichier contenant les trames :"
read nom
while [ ! -f $nom ]
do
echo  -e Fichier non trouvé\tvérifiez votre saisie
echo
echo voici le chemin du script :
pwd
read nom
done
source Cut.sh 


echo -e "Voici le fichier résultat :\n"
cat res.txt
echo -e "Souhaitez vous appliquer un filtre ? yes/no "
read line 

while [[ $line != "yes" ]] && [[ $line != "no" ]]
do
echo -e "Veuillez entrer yes ou no"
read line 
done

if [[ $line == "yes" ]] 
then 
echo -e "Entrez le filtre que vous voulez appliquer :" 
read filtre
source Cut.sh $filtre  
echo -e "Le résultat filtré se trouve dans le fichier res_filtre.txt et celui sans filtre dans res.txt"
fi
[[ $line == "no" ]] && echo -e "Le fichier résultat se trouve dans $final"
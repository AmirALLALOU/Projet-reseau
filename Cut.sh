#! /bin/bash 

affichage="Welcome Amir \nAffichage des fichiers dans le repertoire courant :\n"
for i in $affichage
do
echo -e -n $i" "
#sleep 0.4
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

echo -e '\tFichier trouvé'
file=$nom
temporaire="temporaire.txt"
nblignes=0
exec="py3.py"
final="res.txt"

#on stocke les numéros des lignes contenant les débuts de trame
lignes=$(awk '/0000/{print FNR " " }'  $file)
for x in $lignes
do
nblignes=$((nblignes+1))
done
echo -e "\t$nblignes trames détectées"
sleep 1

#initialisation des variables 
b=0
cpt=0

[ $nblignes -eq 1 ]  && $file > $destination && python3 $exec $file >final.txt && exit 0

#Une liste des lignes de début de trame se trouve dans $ligne
echo -e "\tFlowgraph\nFichier de découpage de $nblignes trames\n" >$final
echo -e "\n\tdébut de traitement"
sleep 1
for i in $lignes
do
cpt=$((cpt+1)) 
[ $i -eq 1 ] && continue
echo -e "\nTrame $((cpt-1)) :\n" >> $final
head -n $((i-1)) $file |tail -n +$b > $temporaire  &&  b=$i && python3 $exec $temporaire >> $final
[ $cpt -eq $nblignes ] && tail -n +$i $file > $temporaire  && echo -e "\nTrame $cpt :\n" >>$final && python3 $exec $temporaire >> $final
done
#rm $temporaire

echo -e "\tfin du traitement"
echo Le fichier résultat se trouve dans $final
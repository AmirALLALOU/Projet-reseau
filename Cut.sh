#! /bin/bash
tab
echo -e '\tFichier trouvé'
file=$nom
temporaire="temporaire.txt"
nblignes=0
exec="py3.py"
final="res.txt"
[ ! -z $1 ] && final="res_filtre.txt"

#on stocke les numéros des lignes contenant les débuts de trame
lignes=$(awk '/0000/{print FNR " " }'  $file)
for x in $lignes
do
nblignes=$((nblignes+1))
done
tab
echo -e "\t$nblignes trames détectées"
sleep 1

#initialisation des variables 
b=0
cpt=0


[ $nblignes -eq 1 ]  && $file > $destination && python3 $exec $file >final.txt && exit 0

#Une liste des lignes de début de trame se trouve dans $ligne
tab
echo -e "\n\tdébut de traitement"
sleep 1
tab
printer_slow "0% █████████████████████████████| █████████████████████████████| █████████████████████████████|"
for i in $lignes
do
cpt=$((cpt+1)) 
[ $i -eq 1 ] && continue
#echo -e "\nTrame $((cpt-1)) :\n" >> $final
head -n $((i-1)) $file |tail -n +$b > $temporaire  &&  b=$i && python3 $exec $temporaire >> $final
[ $cpt -eq $nblignes ] && tail -n +$i $file > $temporaire && python3 $exec $temporaire >> $final
done
printer_slow "█████████████████████████████| 100%"
python3 ig.py $final &
sleep 0.1
#rm $temporaire
echo
tab
echo -e "\tfin du traitement"
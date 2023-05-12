for i in "30" "50" "100"
    do
    for j in "5" "10" "100"
    do
        ./attack.sh $i $j
        sleep 10
    done
done
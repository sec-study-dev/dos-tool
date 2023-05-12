for i in "30" "50" "100"
    do
    for j in "50" "100" "1000"
    do
        ./attack.sh $i $j
        sleep 10
    done
done
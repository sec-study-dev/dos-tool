rm -rf result$1_$2.log

case $1 in
30)
    n1=5
    n2=3
    n3=2
    ;;
50)
    n1=5
    n2=5
    n3=2
    ;;
100)
    n1=5
    n2=5
    n3=4
    ;;
*)
    exit
esac

# init sum
attacker_cpu='0'
victim_cpu='0'
attacker_net='0'
victim_net='0'
attacker_ram='0'
victim_ram='0'

#add sum

for i in $(seq 1 $n1)
do
	for j in $(seq 1 $n2)
	do
		for k in $(seq 1 $n3)
		do
			account="ram.att$i$j$k"
			account_info=$(curl -H "Content-Type: application/json" -X POST -d '{"account_name":"'$account'"}' http://192.168.2.91:8889/v1/chain/get_account)
			cpu_used=$(echo "$account_info" | grep -Eo "\"cpu_limit\":\\{\"used\":[0-9]+,")
			if [ "$cpu_used" = "" ];then
				account_info=$(curl -H "Content-Type: application/json" -X POST -d '{"account_name":"'$account'"}' http://192.168.2.91:8889/v1/chain/get_account)
				cpu_used=$(echo "$account_info" | grep -Eo "\"cpu_limit\":\\{\"used\":[0-9]+,")
			fi
			if [ "$cpu_used" = "" ];then
				continue
			fi
			cpu_used=$(echo "$cpu_used" | grep -Eo "[0-9]+")
			attacker_cpu=`expr $attacker_cpu + $cpu_used`

			net_used=$(echo "$account_info" | grep -Eo "\"net_limit\":\\{\"used\":[0-9]+,")
			net_used=$(echo "$net_used" | grep -Eo "[0-9]+")
			attacker_net=`expr $attacker_net + $net_used`

			ram_used=$(echo "$account_info" | grep -Eo "\"ram_usage\":[0-9]+,")
			ram_used=$(echo "$ram_used" | grep -Eo "[0-9]+")
			attacker_ram=`expr $attacker_ram + $ram_used`

			echo "$account: cpu:"$cpu_used" net:"$net_used" ram:"$ram_used
		done
	done
done

account_info=$(curl -H "Content-Type: application/json" -X POST -d '{"account_name":"ram.victim"}' http://192.168.2.91:8889/v1/chain/get_account)
cpu_used=$(echo "$account_info" | grep -Eo "\"cpu_limit\":\\{\"used\":[0-9]+,")
if [ "$cpu_used" = "" ];then
	account_info=$(curl -H "Content-Type: application/json" -X POST -d '{"account_name":"ram.victim"}' http://192.168.2.91:8889/v1/chain/get_account)
	cpu_used=$(echo "$account_info" | grep -Eo "\"cpu_limit\":\\{\"used\":[0-9]+,")
fi
cpu_used=$(echo "$cpu_used" | grep -Eo "[0-9]+")
victim_cpu=`expr $victim_cpu + $cpu_used`

net_used=$(echo "$account_info" | grep -Eo "\"net_limit\":\\{\"used\":[0-9]+,")
net_used=$(echo "$net_used" | grep -Eo "[0-9]+")
victim_net=`expr $victim_net + $net_used`

ram_used=$(echo "$account_info" | grep -Eo "\"ram_usage\":[0-9]+,")
ram_used=$(echo "$ram_used" | grep -Eo "[0-9]+")
victim_ram=`expr $victim_ram + $ram_used`

echo "ram.victim: cpu:"$cpu_used" net:"$net_used" ram:"$ram_used

#print

echo "attacker cpu used: "$attacker_cpu" us" >> "./result$1_$2.log" 2>&1
echo "attacker net used: "$attacker_net" byte" >> "./result$1_$2.log" 2>&1
echo "attacker ram used: "$attacker_ram" byte" >> "./result$1_$2.log" 2>&1
echo "victim cpu used: "$victim_cpu" us" >> "./result$1_$2.log" 2>&1
echo "victim net used: "$victim_net" byte" >> "./result$1_$2.log" 2>&1
echo "victim ram used: "$victim_ram" byte" >> "./result$1_$2.log" 2>&1

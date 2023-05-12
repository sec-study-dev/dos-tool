for i in $(seq 1 5)
do
	for j in $(seq 1 5)
	do
		for k in $(seq 1 4)
		do
			account="cpu.att$i$j$k"
			cleos -u http://192.168.2.91:8889 system newaccount eosio $account EOS5j2Z8q9TQPuxvDXczS9HJNBFALkBqsMwzVB1bfbzoZuXRS6ruK EOS5j2Z8q9TQPuxvDXczS9HJNBFALkBqsMwzVB1bfbzoZuXRS6ruK  --stake-net '0.00 WAX' --stake-cpu '0.00 WAX'  --buy-ram-kbytes 100
			cleos -u http://192.168.2.91:8889 push action eosio.token transfer '["eosio.bp", "'$account'","150.0000 WAX","backup"]' -p eosio.bp@active
			cleos -u http://192.168.2.91:8889 system delegatebw $account $account '50.0000 WAX' '50.0000 WAX' -p $account@active
			cleos -u http://192.168.2.91:8889 system buyram $account  $account  '50.0000 WAX' -p $account@active	
		done
	done
done

sleep 5

cleos -u http://192.168.2.91:8889 system newaccount eosio cpu.victim EOS5j2Z8q9TQPuxvDXczS9HJNBFALkBqsMwzVB1bfbzoZuXRS6ruK EOS5j2Z8q9TQPuxvDXczS9HJNBFALkBqsMwzVB1bfbzoZuXRS6ruK  --stake-net '50.00 WAX' --stake-cpu '00.00 WAX'  --buy-ram-kbytes 100 
cleos -u http://192.168.2.91:8889 push action eosio.token transfer '["eosio.bp", "cpu.victim","1500.0000 WAX","backup"]' -p eosio.bp@active
cleos -u http://192.168.2.91:8889 system delegatebw cpu.victim cpu.victim '500.0000 WAX' '500.0000 WAX' -p cpu.victim@active
cleos -u http://192.168.2.91:8889 system buyram cpu.victim cpu.victim '500.0000 WAX' -p cpu.victim@active

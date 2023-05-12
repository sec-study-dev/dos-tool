for i in $(seq 1 5)
do
	for j in $(seq 1 5)
	do
		for k in $(seq 1 4)
		do
			account="ram.att$i$j$k"
			cleos -u http://192.168.2.91:8889 system newaccount eosio $account EOS5j2Z8q9TQPuxvDXczS9HJNBFALkBqsMwzVB1bfbzoZuXRS6ruK EOS5j2Z8q9TQPuxvDXczS9HJNBFALkBqsMwzVB1bfbzoZuXRS6ruK  --stake-net '0.00 EOS' --stake-cpu '0.00 EOS'  --buy-ram-kbytes 100
			cleos -u http://192.168.2.91:8889 push action eosio.token transfer '["eosio.bp", "'$account'","150.0000 EOS","backup"]' -p eosio.bp@active
			cleos -u http://192.168.2.91:8889 system delegatebw $account $account '50.0000 EOS' '50.0000 EOS' -p $account@active
			cleos -u http://192.168.2.91:8889 system buyram $account  $account  '50.0000 EOS' -p $account@active
		done
	done
done

sleep 5

cleos -u http://192.168.2.91:8889 system newaccount eosio ram.victim EOS5j2Z8q9TQPuxvDXczS9HJNBFALkBqsMwzVB1bfbzoZuXRS6ruK EOS5j2Z8q9TQPuxvDXczS9HJNBFALkBqsMwzVB1bfbzoZuXRS6ruK  --stake-net '50.00 EOS' --stake-cpu '00.00 EOS'  --buy-ram-kbytes 100 
cleos -u http://192.168.2.91:8889 push action eosio.token transfer '["eosio.bp", "ram.victim","3000.0000 EOS","backup"]' -p eosio.bp@active
cleos -u http://192.168.2.91:8889 system delegatebw ram.victim ram.victim '500.0000 EOS' '500.0000 EOS' -p ram.victim@active
cleos -u http://192.168.2.91:8889 system buyram ram.victim ram.victim '2000.0000 EOS' -p ram.victim@active

sleep 5

cleos  -u http://192.168.2.91:8888 set contract eosio ./eosio.contracts/build/contracts/eosio.msig -p eosio

sleep 5

cleos  -u http://192.168.2.91:8888 set contract eosio ./eosio.contracts/build/contracts/eosio.system -p eosio -x 1000

sleep 5

cleos  -u http://192.168.2.91:8888 push action eosio setpriv '{"account": "eosio.msig", "is_priv": 1}' -p eosio
cleos  -u http://192.168.2.91:8888 push action eosio init '[0,"4,EOS"]' -p eosio

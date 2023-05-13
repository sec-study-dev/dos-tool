cleos -u http://192.168.1.146:8888 push action eosio.token transfer '["eosio", "eosio.bp","300000000.0000 EOS","vote"]' -p eosio

sleep 5 

cleos -u http://192.168.1.146:8888 system delegatebw  eosio.bp eosio.bp '75000000.0000 EOS' '75000000.0000 EOS'

sleep 5

cleos -u http://192.168.1.146:8888 system regproducer eosio.bp EOS5aCp7tVBTyGv3KY1wKhgMNFD6pyefN3Vy7qSGxafajUscbSdbz http://127.0.0.1:8889 0 
sleep 5

cleos -u http://192.168.1.146:8888 system voteproducer prods eosio.bp eosio.bp
cleos -u http://192.168.1.146:8888  get schedule

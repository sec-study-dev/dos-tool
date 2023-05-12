
./open_wallet.sh
curl -X POST http://192.168.2.91:8888/v1/producer/schedule_protocol_feature_activations -d '{"protocol_features_to_activate": ["0ec7e080177b2c02b278d5088611686b49d739925a92d9bfcacd7fc6b74053bd"]}' | jq

sleep 5

cleos  -u http://192.168.2.91:8888 set contract eosio ./eosio.contracts/build/contracts/eosio.bios -p eosio

sleep 5

cleos  -u http://192.168.2.91:8888 create account eosio eosio.token EOS8bYgcHAgKrv4gG5JU5JBCK3rckGpsiSM4jQkpxcXbhaWdCWVob
cleos  -u http://192.168.2.91:8888 create account eosio eosio.bpay EOS8QhS5GHUmAojqqhphuSdmAsjAKAv2Tm1WG9ZC8w6SFurfV9NaC
cleos  -u http://192.168.2.91:8888 create account eosio eosio.msig EOS8FzXzLEfMekQukM9TNVgE5VaBLTDwKnxhmZACmGLG7dgZSoAHi 
cleos  -u http://192.168.2.91:8888 create account eosio eosio.names EOS8Dia3zrsXA227zAum5Czutksn4e4zRRFRVx8ucSJn4K4xN3WS9
cleos  -u http://192.168.2.91:8888 create account eosio eosio.ram EOS86UnsGyHLPrHwaMVPNjSdJ7A4WaYzKmNYecNtZ2NwMmysAnECA 
cleos  -u http://192.168.2.91:8888 create account eosio eosio.ramfee EOS7Zs2MJ2yVi4D25BT9jdGJTjdQphfrJZip1BnVWQCrKTuPKzCTm 
cleos  -u http://192.168.2.91:8888 create account eosio eosio.saving EOS7ZC5iYNAQgA5t7ocSgptL4zqLdPd4kH6khgA4CEYyCACm8NdNj 
cleos  -u http://192.168.2.91:8888 create account eosio eosio.stake EOS7XFiNoSDTFWs11VPPmfoAPJPm7b7NvuvzEH2teou6ubLGaU4Qb 
cleos  -u http://192.168.2.91:8888 create account eosio eosio.upay EOS7X9CiZiPwk9XBD8vBGxbBhZLm5ygrtN8EdXiJ2MBDpk7Km4doC 
cleos  -u http://192.168.2.91:8888 create account eosio eosio.sudo EOS6qLwxEHT8PMf9yubsUrcUdK6kDPb1YnRKas8NeH4ZRNcujEmVN 
cleos  -u http://192.168.2.91:8888 create account eosio eosio.rex EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV

sleep 5

cleos  -u http://192.168.2.91:8888 set contract eosio.token ./eosio.contracts/build/contracts/eosio.token

sleep 5

cleos  -u http://192.168.2.91:8888 push action eosio.token create '["eosio","10000000000.0000 EOS",0,0,0]' -p eosio.token
cleos  -u http://192.168.2.91:8888 push action eosio.token issue '["eosio","1000000000.0000 EOS","issue"]' -p eosio



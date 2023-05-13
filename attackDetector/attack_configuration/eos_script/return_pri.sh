accounts=("eosio.bpay" "eosio.msig" "eosio.names" "eosio.ram" "eosio.ramfee" "eosio.saving" "eosio.stake" "eosio.token" "eosio.upay" "eosio.sudo")

for act in ${accounts[*]}
do
	cleos -u http://192.168.1.146:8888 push action eosio updateauth '{"account": "'$act'", "permission": "active", "parent": "owner", "auth":{"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": active}}]}}' -p $act@active
	cleos -u http://192.168.1.146:8888 push action eosio updateauth '{"account": "'$act'", "permission": "owner", "parent": "",       "auth":{"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": active}}]}}' -p $act@owner
done

cleos -u http://192.168.1.146:8888 push action eosio updateauth '{"account": "eosio", "permission": "active", "parent": "owner", "auth":{"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio.prods", "permission": active}}]}}' -p eosio@active
cleos -u http://192.168.1.146:8888 push action eosio updateauth '{"account": "eosio", "permission": "owner", "parent": "",       "auth":{"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio.prods", "permission": active}}]}}' -p eosio@owner
cleos -u http://192.168.1.146:8888  get schedule

cleos -u http://192.168.1.146:8888  get schedule

sleep 5

if [ -f "./data/eosd.pid" ]; then
pid=`cat "./data/eosd.pid"`
echo $pid
kill $pid
rm -r "./data/eosd.pid"
echo -ne "Stoping Node"
while true; do
[ ! -d "/proc/$pid/fd" ] && break
echo -ne "."
sleep 1
done
echo -ne "\r native Node Stopped. \n"
fi

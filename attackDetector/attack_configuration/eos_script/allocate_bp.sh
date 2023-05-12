cleos -u http://192.168.2.91:8888 system newaccount eosio eosio.bp EOS5aCp7tVBTyGv3KY1wKhgMNFD6pyefN3Vy7qSGxafajUscbSdbz EOS5aCp7tVBTyGv3KY1wKhgMNFD6pyefN3Vy7qSGxafajUscbSdbz  --stake-net '50.00 EOS' --stake-cpu '50.00 EOS'  --buy-ram-kbytes 10000
cleos -u http://192.168.2.91:8888 get account eosio.bp

sleep 5

rm -r ./bp_data
mkdir ./bp_data
nodeos \
--genesis-json "./bp_config/genesis.json" \
--max-irreversible-block-age 108000000 \
--data-dir "./bp_data" \
--config-dir "./bp_config" \
--access-control-allow-origin=* \
--contracts-console \
--http-validate-host=false \
--verbose-http-errors \
--enable-stale-production \
>> "./bp_data/nodeos.log" 2>&1 & \
echo $! > "./bp_data/eosd.pid"

echo "bp already!"
#!/bin/bash
rm -r data
mkdir data
nodeos \
--genesis-json "./config/genesis.json" \
--max-irreversible-block-age 108000000 \
--data-dir "./data" \
--config-dir "./config" \
--access-control-allow-origin=* \
--contracts-console \
--http-validate-host=false \
--verbose-http-errors \
--enable-stale-production \
>> "./data/nodeos.log" 2>&1 & \
echo $! > "./data/eosd.pid"


./open_wallet.sh

#!/bin/bash
nodeos \
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

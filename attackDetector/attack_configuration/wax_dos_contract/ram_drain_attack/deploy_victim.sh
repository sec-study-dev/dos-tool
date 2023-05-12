cleos -u http://192.168.2.91:8889 set contract ram.victim ./ram_victim -p ram.victim@active
cleos -u http://192.168.2.91:8889 set account permission ram.victim active --add-code
cleos -u http://192.168.2.91:8889 push action ram.victim setidx '[]' -p ram.victim@active 

#include <eosio/eosio.hpp>
#include <eosio/print.hpp>
#include <eosio/name.hpp>
#include <eosio/asset.hpp>
#include <eosio/transaction.hpp>
#include <eosio/crypto.hpp>
#include <string>
using namespace eosio;

class [[eosio::contract("cpu_victim")]] cpu_victim : public eosio::contract {

public:

  cpu_victim(name receiver, name code,  datastream<const char*> ds): contract(receiver, code, ds) {}
  
  [[eosio::action]]
  void cpuconsume(name user,uint64_t payload){
    require_auth(user);
    eosio::transaction txn;
    const uint128_t sender_id = (((uint128_t)(current_time_point().sec_since_epoch()) << 64) | (uint128_t)(user.value));
    txn.actions.emplace_back(
    action(permission_level{get_self(),"active"_n},
    get_self(),
    "cpuvuln"_n,
    std::make_tuple(payload)
    ));   
    txn.delay_sec = 0;
    txn.send(sender_id, get_self(),false);
  }
  [[eosio::action]]
  void cpuvuln(uint64_t payload){
    require_auth(get_self());
    checksum256 hash;
    for(int i=0;i<payload;i++){
      std::string hash_string = "0x0";
      hash = sha256(hash_string.c_str(),hash_string.length());
    }
    return ;
  }
};

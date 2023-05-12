#include <eosio/eosio.hpp>
#include <eosio/print.hpp>
#include <eosio/name.hpp>
#include <eosio/asset.hpp>
#include <eosio/transaction.hpp>
#include <eosio/crypto.hpp>
#include <string>
using namespace eosio;

class [[eosio::contract("ram_victim")]] ram_victim : public eosio::contract {

public:

  ram_victim(name receiver, name code,  datastream<const char*> ds): contract(receiver, code, ds) {}
  
  [[eosio::action]]
  void ramconsume(name user,uint64_t payload){
    require_auth(user);
    eosio::transaction txn;
    const uint128_t sender_id = (((uint128_t)(current_time_point().sec_since_epoch()) << 64) | (uint128_t)(user.value));
    txn.actions.emplace_back(
    action(permission_level{get_self(),"active"_n},
    get_self(),
    "ramvuln"_n,
    std::make_tuple(user,payload)
    ));   
    txn.delay_sec = 0;
    txn.send(sender_id, get_self(),false);
  }

  [[eosio::action]]
  void ramvuln(name user,uint64_t payload){
    require_auth(get_self());
    data_index data_table(get_first_receiver(), get_first_receiver().value);
    auto itr = data_table.find(0);
    if(itr != data_table.end()){
      uint64_t begin_idx = (itr->user) + 1,end_idx = (itr->user) + payload;
      for(uint64_t i=begin_idx;i<=end_idx;i++){
        data_table.emplace(get_self(), [&]( auto& row ) {
        row.index = i;
        row.user = user.value;
        });
      }
      data_table.modify(itr,get_self(), [&]( auto& row ) {row.user = end_idx;});
    }
    return ;
  }
  [[eosio::action]]
  void setidx(){
    require_auth(get_self());
    data_index data_table(get_first_receiver(), get_first_receiver().value);
    auto itr = data_table.find(0);
        if(itr == data_table.end()){
       data_table.emplace(get_self(), [&]( auto& row ) {
       row.index = 0;
       row.user = 0;
      });
    }
  }
  
  struct [[eosio::table]] data {
    uint64_t index;
    uint64_t user;
    uint64_t primary_key() const { return index; }    
  };
  using data_index = eosio::multi_index<"datas"_n,data>;  
};

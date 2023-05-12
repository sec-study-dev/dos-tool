// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract InlineExp {
    function attack(uint256 payload) public view returns(uint res) {
        assembly {
            let x:= 100
            let y:= 2
            for {let i:= 0} lt(i, payload) {i := add(i, 1)} {
                res := exp(x,exp(x,exp(x,exp(x,exp(x,exp(x,exp(x,exp(x,exp(x,exp(x,exp(x,exp(x,exp(x,exp(x,exp(x,exp(x,exp(x,exp(x,exp(x,exp(x,y))))))))))))))))))))
            }
        }
    }
}

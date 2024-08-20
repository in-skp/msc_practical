// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 4d-Mathematical operations
contract math_operations {
    function add_mul_mod() public pure returns (uint256 aMod, uint256 mMod) {
        // santosh_parse solidity mathematical operations
        uint256 x = 3;
        aMod = addmod(++x, ++x, x);
        mMod = mulmod(++x, ++x, x);
    }
}



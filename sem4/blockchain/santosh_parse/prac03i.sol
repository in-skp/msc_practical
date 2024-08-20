// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 3i-Conversion
// Creating a contract
contract Converse {
    uint a = 10;
    uint8 b = 20;
    uint16 c = 30;
    function add() public view returns (uint) {
        // santosh_parse solidity conversion
        uint d = a + uint(b) + uint(c);
        return d;
    }
}



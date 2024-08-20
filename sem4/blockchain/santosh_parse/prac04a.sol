// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 4a-Functions
contract local {
    uint age = 10;
    // santosh_parse solidity functions
    function getter() public view returns (uint) {
        return age;
    }
    function setter() public {
        age = age + 1;
    }
}



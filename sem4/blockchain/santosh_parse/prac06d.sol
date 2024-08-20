// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 6d-Abstract Contracts
contract Calculator {
    constructor() { }
    function getResult() public pure returns (uint) {
        // santosh_parse solidity abstract contracts
        uint a = 1;
        uint b = 2;
        uint result = a + b;
        return result;
    }
}




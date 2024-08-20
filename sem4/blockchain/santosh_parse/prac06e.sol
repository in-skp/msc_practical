// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 6e-Interfaces
interface Calculator {
    function getResult() external pure returns (uint);
}
contract MyCalculator is Calculator {
    constructor() { }
    function getResult() external pure returns (uint) {
        // santosh_parse solidity interfaces
        uint a = 1;
        uint b = 2;
        uint result = a + b;
        return result;
    }
}




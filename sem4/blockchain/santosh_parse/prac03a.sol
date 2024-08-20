// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 3a-Variables
contract SolidityTest {
    uint storedData;  // State variable
    constructor() {
        storedData = 10;
    }
    function getResult() public pure returns(uint) {
        // santosh_parse solidity variables
        uint a = 1;
        uint b = 2;
        uint result = a + b;
        return result;  // access the local variable
    }
}





// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 6c-Constructors
contract constructorExample {
    string str;
    constructor() {
        str = "Santosh Parse";
    }
    function getValue() public view returns (string memory) {
        // santosh_parse solidity constructors
        return str;
    }
}



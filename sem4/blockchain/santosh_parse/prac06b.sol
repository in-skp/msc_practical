// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 6b-Inheritance
contract Contract_C {
    uint private data;
    uint public info;
    constructor() { info = 10; }
    function increment(uint a) private pure returns (uint) { return a + 1; }
    function updateData(uint a) public { data = a; }
    function getData() public view returns (uint) { return data; }
    function compute(uint a, uint b) internal pure returns (uint) { return  a + b; }
}
// Derivative Contract
contract Contract_E is Contract_C {
    uint private result;
    Contract_C private c;
    constructor() { c = new Contract_C(); }
    function getComputedResult() public {
        // santosh_parse solidity inheritance
        result = compute(3, 5);
    }
    function getResult() public view returns (uint) {
        return result;
    }
}


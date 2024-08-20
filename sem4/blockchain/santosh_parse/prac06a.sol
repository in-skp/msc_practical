// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 6a-Contracts
contract Contract_C {
    uint private data;
    uint public info;
    constructor() { info = 10; }
    function increment(uint a) private pure returns (uint) { return a + 1; }
    function updateData(uint a) public { data = a; }
    function getData() public view returns (uint) { return data; }
    function compute(uint a, uint b) internal pure returns (uint) { return  a + b; }
}
// External Contract
contract Contract_D {
    function readData() public returns (uint) {
        // santosh_parse solidity contracts
        Contract_C c = new Contract_C();
        c.updateData(7);
        return c.getData();
    }
}
// Derivative Contract
contract Contract_E is Contract_C {
    uint private result;
    Contract_C private c;
    constructor() { c = new Contract_C(); }
    function getComputedResult() public {
        // santosh_parse solidity contracts
        result = compute(3, 5);
    }
    function getResult() public view returns (uint) {
        return result;
    }
}



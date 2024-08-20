// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 4f-Function Modifiers
contract FunctionModifier {
    address public owner;
    uint public x = 10;
    bool public locked;
    constructor() {
        owner = msg.sender;
    }
    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }
    modifier validAddress(address _addr) {
        require(_addr != address(0), "Not valid address");
        _;
    }
    function changeOwner(address _newOwner) public onlyOwner validAddress (_newOwner) {
        owner = _newOwner;
        // santosh_parse solidity function modifiers
    }
    modifier noReentrancy() {
        require(!locked, "No reentrancy");
        locked = true;
        _;
        locked = false;
    }
    function decrement(uint i) public noReentrancy {
        x -= i;
        if (i > 1) {
            decrement(i - 1);
        }
    }
}







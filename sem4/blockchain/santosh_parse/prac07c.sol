// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 7c-Error Handling
contract Vendor {
    address public seller;
    modifier onlySeller() {
        // santosh_parse solidity error handling
        require(msg.sender == seller, "Only seller can call this.");
        _;
    }
    function sell(uint amount) public payable onlySeller {
        if (amount > msg.value / 2 ether)
        revert("Not enough Ether provided.");
    }
}



// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 5a-Withdrawal Pattern
contract WithdrawalContract {
    address public richest;
    uint public mostSent;

    mapping (address => uint) pendingWithdrawals;
    error NotEnoughEther();

    constructor() payable  {
        richest = msg.sender;
        mostSent = msg.value;
    }
    function becomeRichest() public payable {
        // santosh_parse solidity withdrawal pattern
        if (msg.value <= mostSent) revert NotEnoughEther();
        pendingWithdrawals[richest] += msg.value;
        richest = msg.sender;
        mostSent = msg.value;
    }
    function withdraw() public {
        // santosh_parse solidity withdrawal pattern
        uint amount = pendingWithdrawals[msg.sender];
        pendingWithdrawals[msg.sender] = 0;
        payable(msg.sender).transfer(amount);
    }
}




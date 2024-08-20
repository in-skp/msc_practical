// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 5b-Restricted Access
contract AccessRestriction {
    address public owner = msg.sender;
    uint public creationTime = block.timestamp;

    error Unauthorized();
    error TooEarly();
    error NotEnoughEther();

    modifier onlyBy(address account) {
        if (msg.sender != account) 
        revert Unauthorized();
        _;
    }
    function changeOwner(address newOwner) public onlyBy(owner) {
        owner = newOwner;
    }
    modifier onlyAfter(uint time) {
        if (block.timestamp < time)
        revert TooEarly();
        _;
    }
    function disown() public onlyBy(owner) onlyAfter(creationTime + 6 weeks) {
        // santosh_parse solidity restricted access
        delete owner;
    }
    modifier costs(uint amount) {
        if (msg.value < amount)
        revert NotEnoughEther();
        _;
        if (msg.value > amount)
        payable(msg.sender).transfer(msg.value - amount);
    }
    function forceOwnerChange(address newOwner) public payable costs(200 ether) {
        // santosh_parse solidity restricted access
        owner = newOwner;
        if (uint160(owner) & 0 == 1)
        return;
    }
}






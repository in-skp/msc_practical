// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 4c-Fallback functions
contract fallback_function {
    event Log(string func, uint256 gas);
    fallback() external payable {
        // santosh_parse solidity fallback functions
        emit Log("fallback", gasleft());
    }
    receive() external payable { 
        emit Log("receive", gasleft());
    }
    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }
}

contract SendToFallback {
    function transferToFallback(address payable _to) public payable {
        _to.transfer(msg.value);
    }

    function callFallback(address payable _to) public payable {
        (bool sent,) = _to.call{value: msg.value}("");
        require(sent, "Failed to send Ether");
    }
}




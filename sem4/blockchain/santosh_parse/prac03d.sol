// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 3d-Decision Making
contract decisionMaking {
    function check(int a) public pure returns(string memory) {
        // santosh_parse solidity decision making
        string memory value;
        if(a > 0)
        {
            value = "Greater than zero";
        }
        else if(a == 0)
        {
            value = "Equal to zero";
        }
        else 
        {
            value = "Less than zero";
        }
        return value;
    }
}






// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;
// author: santosh_parse 
// practical: 3h-Mapping
// Creating a contract
contract Map
{
    mapping(uint=>string) public roll_no;
    function setter(uint keys, string memory value) public {
        // santosh_parse solidity mapping
        roll_no[keys] = value; 
    }
}


